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

#                ffmpeg -f dshow -i video="@device_pnp_\\?\usb#vid_04f2&pid_b67c&mi_00#6&26fcf372&1&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -f flv rtmp://localhost:1935/live/STREAM_NAME

cmd("node D://node//index.js")