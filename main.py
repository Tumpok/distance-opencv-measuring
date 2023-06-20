from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import cv2
import math
import numpy as np
from imutils.video import VideoStream
import imutils
from time import sleep
from threading import Thread
import sys

def thread1(threadname):
    #global h_min
    #global h_max
    global x1
    global y1


    global x2
    global y2
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    ang1 = 0
    ang2 = 0
    ang3 = 0
    cmof = 13
    bs = 0
    cs = 0
    ms = 0
    sin1 = 0
    sin2 = 0
    sin3 = 0

    app = QApplication(sys.argv)
    window = QMainWindow()

    main_text = QtWidgets.QLabel(window)
    main_text.setText("x1 =")
    main_text.move(10, 5)

    main_text2 = QtWidgets.QLabel(window)
    main_text2.setText("y1 =")
    main_text2.move(10, 20)

    main_text3 = QtWidgets.QLabel(window)
    main_text3.setText("x2 =")
    main_text3.move(10, 35)
    
    main_text4 = QtWidgets.QLabel(window)
    main_text4.setText("y2 =")
    main_text4.move(10, 50)
    
    main_text5 = QtWidgets.QLabel(window)
    main_text5.setText("ang1 =")
    main_text5.move(10, 65)

    main_text6 = QtWidgets.QLabel(window)
    main_text6.setText("ang 2 =")
    main_text6.move(10, 80)

    main_text7 = QtWidgets.QLabel(window)
    main_text7.setText("ang3 =")
    main_text7.move(10, 95)

    main_text8 = QtWidgets.QLabel(window)
    main_text8.setText("c =")
    main_text8.move(10, 110)

    main_text9 = QtWidgets.QLabel(window)
    main_text9.setText("b =")
    main_text9.move(10, 125)

    main_text10 = QtWidgets.QLabel(window)
    main_text10.setText("m =")
    main_text10.move(10, 140)

    window.setWindowTitle("Координаты")
    window.setGeometry(350, 350, 250, 170)

    window.show()
    
    main_text.setText("x1 = " + str(x1))
    main_text2.setText("y1 = " + str(y1))
    main_text3.setText("x2 = " + str(x2))
    main_text4.setText("y2 = " + str(y2)) 
    main_text5.setText("ang1 = " + str(0))
    main_text6.setText("ang2 = " + str(0))
    main_text7.setText("ang3 = " + str(0))
    main_text8.setText("c = " + str(0))
    main_text9.setText("b = " + str(0))
    main_text10.setText("m = " + str(0))


    # название окна подстройки
    WINDOWNAME = "Tone1"

    # минимальный размер контуров пятна
    BLOBSIZE = 1500

    # константы насыщенности и яркости
    S_MIN = 29
    S_MAX = 255
    V_MIN = 148
    V_MAX = 255

    # цвет прямоугольника (B, G, R)
    RECTCOLOR = (0, 255, 0)

    # толщина линии прямоугольника
    RTHICK = 2

    # определяем функцию проверки размера пятна
    def checkSize(w, h):
        if w * h > BLOBSIZE:
            return True
        else:
            return False

    # определяем пустую функцию
    def empty(a):
        pass

    # определяем размеры кадра
    frameSize = (50, 50)

    # создаём объект видео потока
    vs = VideoStream(src=2, usePiCamera=False, resolution=frameSize, framerate=32).start()

    # ждём окончания инициализации видеопотока
    sleep(2)

    # создаём окно с ползунком
    cv2.namedWindow(WINDOWNAME)
    cv2.resizeWindow(WINDOWNAME, 500, 100)
    cv2.createTrackbar("Hue", WINDOWNAME, 0, 180, empty)

    while True:

        # получаем кадр изображения
        image = vs.read()

        # получаем максимальный и минимальный тон из значения ползунка
        h_min = cv2.getTrackbarPos("Hue", WINDOWNAME) - 10
        h_max = cv2.getTrackbarPos("Hue", WINDOWNAME) + 10

        # определяем границы цвета в HSV
        lower_range = np.array([h_min, S_MIN, V_MIN])
        upper_range = np.array([h_max, S_MAX, V_MAX])

        # конвертируем изображение в HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # создаём маску выбранного цвета
        thresh = cv2.inRange(hsv, lower_range, upper_range)

        # побитово складываем оригинальную картинку и маску
        bitwise = cv2.bitwise_and(image, image, mask=thresh)

        # показываем картинку маски цвета
        #cv2.imshow("bitwise", bitwise)

        # удаляем цвет из маски
        gray = cv2.cvtColor(bitwise, cv2.COLOR_BGR2GRAY)

        # ищем контуры в картинке
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # если контуры найдены...
        if len(contours) != 0:


            # выводим найденные контуры
            #cv2.drawContours(image, contours, -1, 255, 1)

            # находим контуры бОльшего размера
            c = max(contours, key = cv2.contourArea)

            # получаем координаты прямоугольника, в который они вписаны
            x,y,w,h = cv2.boundingRect(c)

            x1 = x
            y1 = y
            #print(x)
            main_text.setText("x1 = " + str(x1))
            main_text2.setText("y1 = " + str(y1))
            main_text3.setText("x2 = " + str(x2))
            main_text4.setText("y2 = " + str(y2)) 
            main_text5.setText("ang1 = " + str(ang1))
            main_text6.setText("ang2 = " + str(ang2))
            main_text7.setText("ang3 = " + str(ang3))
            main_text8.setText("c = " + str(cs))
            main_text9.setText("b = " + str(bs))
            main_text10.setText("m = " + str(ms))
            ang1 = x1 * 0.06875 + 68
            ang2 = (640 - x2) * 0.065625 + 69
            ang3 = 180 - ang1 - ang2
            sin1 = math.sin(math.radians(ang1))
            sin2 = math.sin(math.radians(ang2))
            sin3 = math.sin(math.radians(ang3))
            bs = 26 * sin1 / sin3
            cs = 26 * sin1 / sin3
            ms = 0.5 * math.sqrt(2*(bs**2) + 2*(cs**2) - 26**2)
            #ms = 1250 / ang3
            # если прямоугольник достаточного размера...
            if checkSize(w, h):

                # выводим его
                cv2.rectangle(image, (x, y), (x+w, y+h), RECTCOLOR, RTHICK)

        # Показываем картинку с квадратом выделения
        cv2.imshow("Image1", image)

        # Если была нажата клавиша ESC
        k = cv2.waitKey(1)
        if k == 27:

            # прерываем выполнение цикла
            #break
            #os._exit()
            sys.exit()

    # закрываем все окна
    cv2.destroyAllWindows()

    # останавливаем видео поток
    vs.stop()


def thread2(threadname):
    #global h_min
    #global h_max
    global x2
    global y2
    sleep(3)
    # название окна подстройки
    WINDOWNAME = "Tone2"

    # минимальный размер контуров пятна
    BLOBSIZE = 1500

    # константы насыщенности и яркости
    S_MIN = 29
    S_MAX = 255
    V_MIN = 148
    V_MAX = 255

    # цвет прямоугольника (B, G, R)
    RECTCOLOR = (0, 255, 0)

    # толщина линии прямоугольника
    RTHICK = 2

    # определяем функцию проверки размера пятна
    def checkSize(w, h):
        if w * h > BLOBSIZE:
            return True
        else:
            return False

    # определяем пустую функцию
    def empty(a):
        pass

    # определяем размеры кадра
    frameSize = (50, 50)

    # создаём объект видео потока
    vs = VideoStream(src=1, usePiCamera=False, resolution=frameSize, framerate=32).start()
    #vs = cv2.VideoCapture(2)
    #vs.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #vs.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # ждём окончания инициализации видеопотока
    sleep(2)

    # создаём окно с ползунком
    cv2.namedWindow(WINDOWNAME)
    cv2.resizeWindow(WINDOWNAME, 500, 100)
    cv2.createTrackbar("Hue", WINDOWNAME, 0, 180, empty)

    while True:

        # получаем кадр изображения
        image = vs.read()

        # получаем максимальный и минимальный тон из значения ползунка
        h_min = cv2.getTrackbarPos("Hue", WINDOWNAME) - 10
        h_max = cv2.getTrackbarPos("Hue", WINDOWNAME) + 10

        # определяем границы цвета в HSV
        lower_range = np.array([h_min, S_MIN, V_MIN])
        upper_range = np.array([h_max, S_MAX, V_MAX])

        # конвертируем изображение в HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # создаём маску выбранного цвета
        thresh = cv2.inRange(hsv, lower_range, upper_range)

        # побитово складываем оригинальную картинку и маску
        bitwise = cv2.bitwise_and(image, image, mask=thresh)

        # показываем картинку маски цвета
        #cv2.imshow("bitwise", bitwise)

        # удаляем цвет из маски
        gray = cv2.cvtColor(bitwise, cv2.COLOR_BGR2GRAY)

        # ищем контуры в картинке
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # если контуры найдены...
        if len(contours) != 0:


            # выводим найденные контуры
            cv2.drawContours(image, contours, -1, 255, 1)

            # находим контуры бОльшего размера
            c = max(contours, key = cv2.contourArea)

            # получаем координаты прямоугольника, в который они вписаны
            x,y,w,h = cv2.boundingRect(c)
            x2 = x
            y2 = y
            #print(x)

            # если прямоугольник достаточного размера...
            if checkSize(w, h):

                # выводим его
                cv2.rectangle(image, (x, y), (x+w, y+h), RECTCOLOR, RTHICK)

        # Показываем картинку с квадратом выделения
        cv2.imshow("Image2", image)

        # Если была нажата клавиша ESC
        k = cv2.waitKey(1)
        if k == 27:

            # прерываем выполнение цикла
            #break
            sys.exit()

    # закрываем все окна
    cv2.destroyAllWindows()

    # останавливаем видео поток
    vs.stop()

def thread3(threadname):
    global x2
    global y2
    global x1
    global y1
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    app = QApplication(sys.argv)
    window = QMainWindow()

    main_text = QtWidgets.QLabel(window)
    main_text.setText("x1 =")
    main_text.move(10, 5)

    main_text2 = QtWidgets.QLabel(window)
    main_text2.setText("y1 =")
    main_text2.move(10, 20)

    main_text3 = QtWidgets.QLabel(window)
    main_text3.setText("x2 =")
    main_text3.move(10, 35)
    
    main_text4 = QtWidgets.QLabel(window)
    main_text4.setText("y2 =")
    main_text4.move(10, 50)
    
    main_text5 = QtWidgets.QLabel(window)
    main_text5.setText("z =")
    main_text5.move(10, 65)

    window.setWindowTitle("Координаты")
    window.setGeometry(350, 350, 250, 100)

    window.show()
    
    main_text.setText("x1 = " + str(x1))
    main_text2.setText("y1 = " + str(y1))
    main_text3.setText("x2 = " + str(x2))
    main_text4.setText("y2 = " + str(y2)) 
    main_text5.setText("z = " + str(1))

def thread4(threadname):
    global x2
    global y2
    global x1
    global y1
    
    
    while True:
        main_text.setText("x1 = " + str(x1))
        main_text2.setText("y1 = " + str(y1))
        main_text3.setText("x2 = " + str(x2))
        main_text4.setText("y2 = " + str(y2)) 
        main_text5.setText("z = " + str(1))


if __name__ == '__main__':
    thread1 = Thread(target=thread1, args=("Thread1",))
    thread2 = Thread(target=thread2, args=("Thread2",))
    #thread3 = Thread(target=thread3, args=("Thread3",))
    #thread4 = Thread(target=thread4, args=("Thread4",))
    thread1.start()
    thread2.start()
    #thread3.start()
    #thread4.start()
    