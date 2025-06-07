import os
import time

def schedule_shutdown(minutes):
    """
    定时关机函数
    :param minutes: 关机延迟时间（分钟）
    """
    if minutes <= 0:
        raise ValueError("分钟数必须大于0")
    seconds = minutes * 60
    time.sleep(seconds)
    os.system("shutdown /s /t 1")  # Windows系统

def cancel_shutdown():
    """
    取消关机函数
    """
    os.system("shutdown /a")  # Windows系统