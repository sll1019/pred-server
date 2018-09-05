
# -*- coding: utf-8 -*-
# !/usr/bin/env python
'''
@author: shi
@file: img_server.py.py
@time: 18-6-14 下午9:00


'''

import os, sys, cv2, json, multiprocessing, time, logging, traceback, copy, requests,base64,datetime
import tensorflow as tf
from gevent.pywsgi import WSGIServer
import numpy as np
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, request, jsonify
from config import *


if os.path.exists('log') == False:
    os.mkdir('log')


# set logger
log_file_handler = TimedRotatingFileHandler(filename="log/pred_server.log",
                                            when="D", interval=1, backupCount=10)
log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
formatter = logging.Formatter(log_fmt)
log_file_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
log.addHandler(log_file_handler)


def get_iou(box1,box2):
    h1_1,h2_1,w1_1,w2_1 = box1
    box1_s = (h2_1 - h1_1) * (w2_1 - w1_1)
    h1_2,h2_2,w1_2,w2_2 = box2
    box2_s = (h2_2 - h1_2) * (w2_2 - w1_2)

    if h1_1 > h2_2 or h2_1 < h1_2:
        h1 = 0
        h2 = 0
    else:
        h1 = max(h1_1, h1_2)
        h2 = min(h2_1, h2_2)

    if w1_1 > w2_2 or w2_1 < w1_2:
        w1=0
        w2=0
    else:
        w1 = max(w1_1,w1_2)
        w2 = min(w2_1,w2_2)


    box_s = (h2-h1) * (w2-w1)

    # print(box1_s,box2_s,box_s)
    return [h1,h2,w1,w2],(box_s/(box1_s+box2_s-box_s))


class Detector():
    def __init__(self):

        sensor_config = get_sensor_config('startdt_umc_520')


        # raw_model_dir_path = '/tmp/m'
        # now_model_dir_path = '/tmp/m_a'
        # bk_model_dir_path = '/tmp/m_a_bk'
        #
        # if os.path.exists(raw_model_dir_path) == False:
        #     os.mkdir(raw_model_dir_path)
        #
        # if os.path.exists(now_model_dir_path) == False:
        #     os.mkdir(now_model_dir_path)
        #
        # if os.path.exists(bk_model_dir_path) == False:
        #     os.mkdir(bk_model_dir_path)




        # PATH_TO_CKPT = '/tmp/frozen_inference_graph.pb'
        #
        # if os.path.exists(PATH_TO_CKPT):
        #     os.remove("/tmp/frozen_inference_graph.pb")
        #
        # os.system("unzip -P jglHVqCTcW0E -d /tmp/m_a model.zip")
        # print('unzip ok,')




        PATH_TO_CKPT = sensor_config['PATH_TO_CKPT']

        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            self.sess = tf.Session()
            # Get handles to input and output tensors
            ops = tf.get_default_graph().get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            self.tensor_dict = {}
            for key in ['num_detections', 'detection_boxes', 'detection_scores', 'detection_classes']:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    self.tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)
            self.imame_np_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

        # if os.path.exists(PATH_TO_CKPT):
        #     os.remove("/tmp/frozen_inference_graph.pb")
        print('model init done.')

        self.confidence_threshold = sensor_config['confidence_threshold']
        self.tiny_box_threshold = sensor_config['tiny_box_threshold']
        self.tiny_box_location_x_limited = sensor_config['tiny_box_location_x_limited']
        self.tiny_box_location_y_limited = sensor_config['tiny_box_location_y_limited']
        self.intra_class_iou_threshold = sensor_config['intra_class_iou_threshold']
        self.inter_class_iou_threshold = sensor_config['inter_class_iou_threshold']


    def detect(self,img_list,):
        # img_list = [cv2.cvtColor(i, cv2.COLOR_BGR2RGB) for i in img_list]

        t_str = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

        img_array = np.array(img_list)

        tmp_classes_list = []
        tmp_boxes_list = []
        tmp_score_list = []
        tmp_boxes_hist_list = []
        output_dict = self.sess.run(self.tensor_dict, feed_dict={self.imame_np_tensor: img_array})


        for idx in range(len(img_array)):
            detection_classes = output_dict['detection_classes'][idx].astype(np.uint8)
            detection_boxes = output_dict['detection_boxes'][idx]
            detection_scores = output_dict['detection_scores'][idx]

            img = img_list[idx].copy()
            # img_raw = img.copy()
            h, w, c = img.shape

            boxes=[];classes=[];scores=[];boxes_hist=[]
            for i in range(len(detection_scores)):
                if detection_scores[i] > self.confidence_threshold:
                    y1, x1, y2, x2 = detection_boxes[i]
                    x1 = int(w * x1)
                    x2 = int(w * x2)
                    y1 = int(h * y1)
                    y2 = int(h * y2)
                    tmp_box = [y1,y2,x1,x2]

                    is_passed = 0

                    if boxes == []:
                        pass
                    else:
                        while True:
                            iou_ok = 1
                            for box_idx in range(len(boxes)):

                                iou_area,iou_score = get_iou(tmp_box,boxes[box_idx])



                                # print(tmp_box,boxes[box_idx],iou_score)


                                if detection_classes[i] == classes[box_idx] and iou_score >self.intra_class_iou_threshold:
                                    if detection_scores[i] >= scores[box_idx]:
                                        del classes[box_idx]
                                        del boxes[box_idx]
                                        del scores[box_idx]
                                        iou_ok -= 1
                                        break
                                    else:
                                        is_passed = 1
                                        break
                                elif detection_classes[i] != classes[box_idx] and iou_score >self.inter_class_iou_threshold:
                                    if detection_scores[i] >= scores[box_idx]:
                                        del classes[box_idx]
                                        del boxes[box_idx]
                                        del scores[box_idx]
                                        iou_ok -= 1
                                        break
                                    else:
                                        is_passed = 1
                                        break
                            if iou_ok == 1:
                                break

                    if is_passed == 1:
                        continue



                    # area_s = (x2 - x1) * (y2 - y1)
                    # area_s_ratio = area_s / w / h
                    # area_centerx_ratio = (x2+x1) /2 / w
                    # area_centery_ratio = 1 - (y2+y1) /2 / h
                    # if area_centerx_ratio > 0.5:
                    #     area_centerx_ratio = 1 - area_centerx_ratio
                    # if area_s_ratio < self.tiny_box_threshold and (area_centerx_ratio > self.tiny_box_location_x_limited or area_centery_ratio < self.tiny_box_location_y_limited ):
                    #     continue


                    # img = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                    # img = cv2.putText(img,str(int(detection_classes[i])),(x1,y1),1,2,(255,0,0),2)


                    boxes.append([y1,y2,x1,x2])
                    classes.append(int(detection_classes[i]))
                    scores.append(float(detection_scores[i]))
                    # boxes_hist.append(hist_norm_list)

            tmp_classes_list.append(classes)
            tmp_boxes_list.append(boxes)
            tmp_score_list.append(scores)
            # tmp_boxes_hist_list.append(boxes_hist)

        #     cv2.imwrite('raw_pic/%s.jpg'%t_str,cv2.cvtColor(img_raw,cv2.COLOR_RGB2BGR))
        #     cv2.imwrite('pred_pic/%s.jpg'%t_str,cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
        #
        #
        # with open('pred_resualt/%s.json'%t_str,'w')as f:
        #     f.write(json.dumps([tmp_classes_list,tmp_boxes_list,tmp_score_list]))


        return tmp_classes_list,tmp_boxes_list,tmp_score_list
        # return tmp_classes_list,tmp_boxes_list,tmp_score_list,tmp_boxes_hist_list


class DetectAPI():
    def __init__(self):
        self.app = Flask(__name__)
        self._detector = Detector()
        self.app.add_url_rule(rule="/detect", view_func=self.detect_api, methods=["GET", "POST"])
        self.app.add_url_rule(rule="/", view_func=self.index, methods=["GET", "POST"])

    def index(self):
        try:
            return json.dumps({'success': True})
        except:
            return json.dumps({'success': False})



    def detect_api(self):
        info = {"success": False,"resualt":[]}

        # try:
        headers = ['data:image/jpeg;base64', 'data:image/png;base64']
        req_json = request.get_json()
        # print req_json
        img_list = []
        detect_img_b64_list = req_json['img']
        for detect_img_b64 in detect_img_b64_list:
            for header in headers:
                if header in detect_img_b64:
                    detect_img_b64 = detect_img_b64.replace(header, '')


            img = base64.b64decode(detect_img_b64)
            img = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_COLOR)
            img_list.append(img)

        info['resualt'] = self._detector.detect(img_list)
        # print(info['resualt'],type(['resualt']))
        info['success'] = True

        return jsonify(info)

        # except Exception as e:
        #     return jsonify(info)



def wsgi_api(app):
    print("[pred_server 8101]: Start gevent WSGI server")
    http = WSGIServer(('', 8101), app.wsgi_app)
    http.serve_forever()


if __name__ == '__main__':
    wsgi_api(DetectAPI().app)

