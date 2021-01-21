import pyautogui

while True:
    x,y = pyautogui.position()
    print ("当前鼠标的X轴的位置为：{}，Y轴的位置为：{}".format(x,y))