from threading import *
import cv2
from time import time, sleep
import logging
import subprocess

def cmd(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值，python调试界面输出返回值
    :param cmd_string: cmd命令，如：'adb devices'
    :return:
    """
    print('COMMAND：{}'.format(cmd_string))
    subprocess.Popen(cmd_string, shell=True)

# 打开直播流

# ffmpeg -f dshow -i video='@device_pnp_\\?\usb#vid_04f2&pid_b67c&mi_00#6&26fcf372&1&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global' -f dshow -i audio='@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{4AEC28D7-6B71-40EA-9CE2-8BED96C1541C}' -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv                                             rtmp://localhost:1935/live/STREAM_NAME

# cmd("".join(lst))
lst = [
    "ffmpeg ",
    "-f dshow -i video='Integrated Camera' ",
    "-f dshow -i audio='麦克风阵列 (英特尔® 智音技术)' ",
    "-vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv ",
    "rtmp://localhost:1935/live/STREAM_NAME"
]
# ffmpeg -list_devices true -f dshow -i dummy
# cap = cv2.VideoCapture("rtsp://127.0.0.1:8554/test")

# fps = 30  # 直播流帧率
# maxDelay = 0.5  # 最大容许延时
# startTime = time()  # 开始时间
# frames = 0
# logging.info("已连接")
# while True:
#     frames += 1
#     ret, frame = cap.read()
#     # 延时小于最大容许延时才进行识别
#     # if frames > (time()-startTime-maxDelay)*fps:
#     cv2.imshow("frame", frame)
#     # else:
#     #     logging.info(f"已跳过一帧，当前{frames}，期望{int((time()-startTime-maxDelay)*fps)}")
#     # 按q退出
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()
# cap.release()
