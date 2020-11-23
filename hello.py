import pyautogui
import time
import os
import cv2
import numpy
import matplotlib
import matplotlib.image as mpimg
import sys
from PyQt5.QtGui import QIcon
from threading import Thread
from PyQt5.QtWidgets import QApplication, QWidget
#import screenshot


# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
print("分辨率：", screenWidth, screenHeight)
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()


# 构建函数
def start():
    "开始函数，检测方舟图标【fangzhou.png】"
    # 获取屏幕快照
    #im = pyautogui.screenshot()
    # 打开方舟，自动识别\
    pyStarttime = time.time()
    pyicon = pyautogui.locateOnScreen('fangzhou.png')
    pyEndtime = time.time()
    print("pyautogui识别消耗时间【方舟】:", pyEndtime-pyStarttime)
    # 获取方舟图标xy
    x, y = pyautogui.center(pyicon)
    # log打印xy
    print("方舟图标位置：", x, y)
    # 点击左键一次 打开方舟
    pyautogui.click(x, y)
    print("已点击方舟坐标：", x, y)
    time.sleep(20)
    print("点击屏幕中心点")
    pyautogui.click(960, 540)
    time.sleep(0.8)
    print("容错，第二次点击屏幕中心点")
    pyautogui.click(960, 540)
    time.sleep(18)
    print("start()函数执行完毕")
    return


def huanxing():
    "开始唤醒函数，启动唤醒进入主界面"
    # 开始唤醒
    print("开始执行唤醒")
    py2Starttime = time.time()
    pyicon_huanxing = pyautogui.locateOnScreen('huanxing.png')
    py2Endtime = time.time()
    print("pyautogui识别消耗时间【唤醒】:", py2Endtime-py2Starttime)
    # 获取方舟图标xy
    x, y = pyautogui.center(pyicon_huanxing)
    # log打印xy
    pyautogui.moveTo(x, y, duration=0.1, tween=pyautogui.linear)
    pyautogui.click()
    return


def find_ganyuanxunfang(target, template):
    """
    寻找target图片在template中的位置，返回应该点击的坐标。
    """
    #target = mping.imread('干员寻访.png')
    theight, twidth = target.shape[:2]
    cvStarttime = time.time()
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    cvEndtime = time.time()
    print("cv识别消耗时间:", cvEndtime-cvStarttime)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("min_val    max_val    min_loc    max_loc")
    print(min_val, max_val, min_loc, max_loc)
    # 如果匹配度小于99%，就认为没有找到。
    # 0.00001
    if min_val > 0.01:
        return None
    strmin_val = str(min_val)
    # print(strmin_val)
    # 绘制矩形边框，将匹配区域标注出来

    #cv2.rectangle(template, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2)
    #cv2.imshow("MatchResult----MatchingValue="+strmin_val, template)
    #cv2.imwrite('1.png', template, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    #
    x = min_loc[0] + twidth//3
    y = min_loc[1] + theight//3
    return (x, y)


def fun():
    "主要暂时调用：调用寻访干员()"
    temp = pyautogui.screenshot("screen.png")
    # 这里图片需要英文 中文报错
    target = cv2.imread("xunfang.png", 2 | 4)
    temp = cv2.imread("screen.png", 2 | 4)
    find_ganyuanxunfang(target, temp)
    pos = find_ganyuanxunfang(target, temp)
    print("fun()，pos变量：", pos)
    # 鼠标·移动到指定target图片位置（xunfang.png）
    print("输出pos", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1], duration=0.1, tween=pyautogui.linear)
    return


start()
huanxing()
time.sleep(15)
fun()

# class windowExample(QWidget):
#   def __init__(self):
#      super().__init__()
#     self.initUI()
#
#   def inintUI():


# if __name__ == '__main__':
#     # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
#     # 创建application对象
#     app = QApplication(sys.argv)
#     # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
#     # 创建窗体对象
#     w = QWidget()
#     # resize()方法调整窗口的大小。这离是250px宽150px高
#     w.resize(500, 300)
#     # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#     w.move(10, 10)
#     w.setWindowIcon(QIcon('fangzhou.png'))
#     # 设置窗口的标题
#     w.setWindowTitle('Simple')
#     # 显示在屏幕上
#     w.show()
#     # 系统exit()方法确保应用程序干净的退出
#     # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
#     sys.exit(app.exec_())


# 2秒钟鼠标移动坐标为100,100位置  绝对移动
# pyautogui.moveTo(100, 100,2)
#pyautogui.moveTo(x=300, y=300, duration=0.1, tween=pyautogui.linear)

#print("屏幕中心点", screenWidth / 2, screenHeight / 2)
# 鼠标移到屏幕中央。
#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
# 鼠标左击一次
# pyautogui.click()
# x
# y
# clicks 点击次数
# interval点击之间的间隔
# button 'left', 'middle', 'right' 对应鼠标 左 中 右或者取值(1, 2, or 3)
# tween 渐变函数
#
# pyautogui.click(x=None, y=None, clicks=1, interval=0.0,
#                button='left', duration=0.0, tween=pyautogui.linear)

# 鼠标相对移动 ,向下移动
# pyautogui.moveRel(None, 10)
# pyautogui.moveRel(xOffset=None, yOffset=10,
#                  duration=0.0, tween=pyautogui.linear)


# 鼠标当前位置0间隔双击
# pyautogui.doubleClick()
# pyautogui.doubleClick(x=None, y=None, interval=0.0,
#                      button = 'left', duration = 0.0, tween = pyautogui.linear)

# 鼠标当前位置3击
# pyautogui.tripleClick()
# pyautogui.tripleClick(x=None, y=None, interval=0.0,
#                      button='left', duration=0.0, tween=pyautogui.linear)

# 右击
# pyautogui.rightClick()

# 中击
# pyautogui.middleClick()

#  用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
#  use tweening/easing function to move mouse over 2 seconds.
# pyautogui.moveTo(x=500, y=500, duration=2, tween=pyautogui.easeInOutQuad)

# 鼠标拖拽
# pyautogui.dragTo(x=427, y=535, duration=3, button='left')

# 鼠标相对拖拽
# pyautogui.dragRel(xOffset=100, yOffset=100, duration=, button='left', mouseDownUp=False)

# 鼠标移动到x=1796, y=778位置按下
# pyautogui.mouseDown(x=1796, y=778, button='left')

# 鼠标移动到x=2745, y=778位置松开（与mouseDown组合使用选中）
# pyautogui.mouseUp(x=2745, y=778, button='left', duration=5)

# 鼠标当前位置滚轮滚动
# pyautogui.scroll()
# 鼠标水平滚动（Linux）
# pyautogui.hscroll()
# 鼠标左右滚动（Linux）
# pyautogui.vscroll()
