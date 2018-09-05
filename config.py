# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
@author: shi
@file: main_server.py
@time: 18-5-8 下午3:29
'''



def get_labels_dict(password='',mode='tongyi'):
    if password == 'startdt_umc_520':
        if mode == 'yufa':
            return {
                      "0": {"weight":-1,"chinese_name":"空盒子","name":"box","online_code": -1},
                      "1": {"weight":539,"chinese_name":"营养快线","name":"yingyangkuaixian","online_code": 1003733},
                      "2": {"weight":482,"chinese_name":"蜂蜜米露","name":"fengmimilu","online_code": 1003740},
                      "3": {"weight":646,"chinese_name":"脉动水蜜桃","name":"maidong","online_code": 1003734},
                      "4": {"weight":460,"chinese_name":"美汁源","name":"meizhiyuan","online_code": 1003742},
                      "5": {"weight":560,"chinese_name":"农夫果园","name":"nongfuguoyuan","online_code": 1003735},
                      "6": {"weight":385,"chinese_name":"苏打水","name":"sudashui","online_code": 1003737},
                      "7": {"weight":1054,"chinese_name":"绿茶","name":"lvcha","online_code": 1003736}
                    }
        elif mode == 'test':
            return {
                      "0": {"weight":-1,"chinese_name":"空盒子","name":"box","online_code": -1},
                      "1": {"weight":539,"chinese_name":"营养快线","name":"yingyangkuaixian","online_code": 1005825},
                      "2": {"weight":482,"chinese_name":"蜂蜜米露","name":"fengmimilu","online_code": 1005819},
                      "3": {"weight":646,"chinese_name":"脉动水蜜桃","name":"maidong","online_code": 1005824},
                      "4": {"weight":460,"chinese_name":"美汁源","name":"meizhiyuan","online_code": 1005818},
                      "5": {"weight":560,"chinese_name":"农夫果园","name":"nongfuguoyuan","online_code": 1005823},
                      "6": {"weight":385,"chinese_name":"苏打水","name":"sudashui","online_code": 1005821},
                      "7": {"weight":1054,"chinese_name":"绿茶","name":"lvcha","online_code": 1005822}
                    }
        elif mode == 'tongyi':
            return {
                      "0": {"weight":-1,"chinese_name":"空盒子","name":"box","online_code": -1},
                      "1": {"weight":554.8,"chinese_name":"统一冰红茶柠檬","name":"TongYiBingHongChaNingMeng","online_code": 1006133},
                      "2": {"weight":538.8,"chinese_name":"统一绿茶茉莉","name":"TongYiLvChaMoLi","online_code": 1006148},
                      "3": {"weight":498.5,"chinese_name":"雅哈冰咖啡","name":"YaHaBingKaFei","online_code": 1006134},
                      "4": {"weight":549.6,"chinese_name":"小茗同学青柠红茶","name":"XiaoMingTongXueQingNingHongCha","online_code": 1006149},
                      "5": {"weight":500.7,"chinese_name":"统一鲜橙多","name":"TongYiXianChengDuo","online_code": 1006150},
                      "6": {"weight":116.2,"chinese_name":"汤达人日式豚骨拉面杯","name":"TangDaRenRiShiTunGuLaMianBei","online_code": 1000001},
                      "7": {"weight":123.2,"chinese_name":"汤达人酸酸辣辣豚骨拉面杯","name":"TangDaRenSuanSuanLaLaTunGuLaMianBei","online_code": 1006151},
                      "8": {"weight":551,"chinese_name":"统一阿萨姆奶茶原味","name":"TongYiASaMuNaiChaYuanWei","online_code": 1006135},
                      "9": {"weight":312.5,"chinese_name":"雅哈意式经典","name":"YaHaYiShiJingDian","online_code": 1006136},
                      "10": {"weight":547.8,"chinese_name":"小茗同学溜溜哒茶","name":"XiaoMingTongXueLiuLiuDaCha","online_code": 1006153},
                      "11": {"weight":271.3,"chinese_name":"统一奶茶草莓","name":"TongYiNaiChaCaoMei","online_code": 1006137},
                      "12": {"weight":270.6,"chinese_name":"统一奶茶巧克力","name":"TongYiNaiChaQiaoKeLi","online_code": 1006138},
                      "13": {"weight":270.1,"chinese_name":"统一奶茶麦香","name":"TongYiNaiChaMaiXiang","online_code": 1006139},
                      "14": {"weight":449.6,"chinese_name":"茶瞬鲜柠檬绿茶","name":"ChaShunXianNingMengLvCha","online_code": 1006154},
                      "15": {"weight":285,"chinese_name":"REMIX爱混牛乳布丁奶茶","name":"REMIXAiHunNiuRuBuDingNaiCha","online_code": 1006140},
                      "16": {"weight":449.4,"chinese_name":"茶瞬鲜青桔乌龙茶","name":"ChaShunXianQingJuWuLongCha","online_code": 1006155}
                    }
    else:
        return ''



def get_sensor_config(password='',mode='4573'):
    if password == 'startdt_umc_520':
        if mode == '41537':
            return {
                "cam_config": [

                    {"id": 0,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:4.1:1.0-video-index0",
                     "knew_index": 0.8,
                     "crop_area": [0,-30, 20,-20]
                     },
                    {"id": 1,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:5:1.0-video-index0",
                     "knew_index": 0.7,
                     "crop_area": [0,-30, 20,-20]
                     },
                    {"id": 2,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:3:1.0-video-index0",
                     "knew_index": 0.7,
                     "crop_area": [0,-30, 40,-40]
                     },
                    {"id": 3,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:7:1.0-video-index0",
                     "knew_index": 1.1,
                     "crop_area": [0,-30, 20,-20]
                     }

                ],
                "weight_config": {"weight_ip":'http://192.168.70.200:8001/localserver/sensor/getSensorInfo',
                                  "weight_config_path": 'weight_config.json',
                                  "weight_sensor_list":["g_sensor_1","g_sensor_2","g_sensor_3","g_sensor_4"]},
                "weight_server_address": ['http://192.168.70.10:8888'],
                "K": [[407.43665432, 0., 639.5],
                      [0., 407.43665432, 479.5],
                      [0., 0., 1.]],
                "D": [[0.], [0.], [0.], [0.]],
                "confidence_threshold": 0.5,
                "weight_correct_threshold": 3,
                "tiny_box_threshold": 0.006,
                "tiny_box_location_x_limited": 0.2,
                "tiny_box_location_y_limited": 0.1,
                "intra_class_iou_threshold": 0.9,
                "inter_class_iou_threshold": 0.7,
                "raw_pic_dir_path": 'raw_pic/',
                "recalibrate_pic_dir_path": 'recalibrate_pic/',
                "recalibrate_detect_pic_dir_path": 'recalibrate_detect_pic/',
                "recalibrate_anos_dir_path": 'recalibrate_anos/'

            }
        elif mode == '4573':
            return {
                "cam_config": [

                    {"id": 0,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:4:1.0-video-index0",
                     "knew_index": 0.8,
                     "crop_area": [0,-80, 20,-20]
                     },
                    {"id": 1,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:5:1.0-video-index0",
                     "knew_index": 1.1,
                     "crop_area": [0,-30, 20,-20]
                     },
                    {"id": 2,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:7:1.0-video-index0",
                     "knew_index": 1.1,
                     "crop_area": [0,-30, 80,-40]
                     },
                    {"id": 3,
                     "path": "/dev/v4l/by-path/pci-0000:00:14.0-usb-0:3:1.0-video-index0",
                     "knew_index": 0.95,
                     "crop_area": [0,-150, 20,-20]
                     }

                ],
                "weight_config": {"weight_ip":'http://192.168.70.200:8001/localserver/sensor/getSensorInfo',
                                  "weight_config_path": 'weight_config.json',
                                  "weight_sensor_list":["g_sensor_1","g_sensor_2","g_sensor_3","g_sensor_4"],
                                  "request_address_wl":['0.0.0.0','127.0.0.1','192.168.70.200','::ffff:0.0.0.0','::ffff:127.0.0.1','::ffff:192.168.70.200'],
                                  "request_password":'startdt@!@#!',
                                  "usbstatus_log_path":'log/usb.log'},
                "weight_server_address": ['http://192.168.70.200:8102'],
                "K": [[407.43665432, 0., 639.5],
                      [0., 407.43665432, 479.5],
                      [0., 0., 1.]],
                "D": [[0.], [0.], [0.], [0.]],
                "confidence_threshold": 0.45,
                "weight_correct_threshold": 3,
                "tiny_box_threshold": 0.006,
                "tiny_box_location_x_limited": 0.2,
                "tiny_box_location_y_limited": 0.1,
                "intra_class_iou_threshold": 0.9,
                "inter_class_iou_threshold": 0.7,
                "raw_pic_dir_path": 'raw_pic/',
                "recalibrate_pic_dir_path": 'recalibrate_pic/',
                "recalibrate_detect_pic_dir_path": 'recalibrate_detect_pic/',
                "recalibrate_anos_dir_path": 'recalibrate_anos/',
                "PATH_TO_CKPT":'tongyi_2w_v21_15w/frozen_inference_graph.pb'

            }
    else:
        return ''



def get_umc_config(password=''):
    if password == 'startdt_umc_520':
        return {
                  "ipcam_per_layer":1,
                  "weight_per_layer":1,
                  "cache_len":3,
                  "weightchanging_percentage_threshold":0.1,
                  "weightchanging_value_threshold":20,
                  "empty_dish_threshold":10,
                  "weight_toleration_percentage_threshold":0.0075,
                  "weight_toleration_percentage_value":30,
                  "gamma":0.7,
                  "iou_score_threshold":0.9,
                  "hist_sim_threshold":0.9,
                  "local_ip":'http://192.168.70.200',
                  "pred_forced_path":'log'


                }
    else:
        return ''
