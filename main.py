import sys
import cv2
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
    QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)
from cv2 import COLOR_BGR2GRAY

# import numpy as np
# from PIL import ImageFilter
# from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")
        
        # 메뉴바 만들기
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("파일")
        exit = QAction("나가기", self, triggered=qApp.quit)
        self.menu_file.addAction(exit)
        self.tmp_image = None


        # save = QAction("저장", cv2.imwrite(self.tmp_image))
        # self.menu_file.addAction(save)

        # 메인화면 레이아웃
        main_layout = QHBoxLayout()

        #사이드바 메뉴버튼
        sidebar = QVBoxLayout()
        button1 = QPushButton("이미지 열기")
        button2 = QPushButton("좌우반전")
        button3 = QPushButton("새로고침")
        button1.clicked.connect(self.show_file_dialog)
        button2.clicked.connect(self.flip_image)
        button3.clicked.connect(self.clear_label)
        sidebar.addWidget(button1)
        sidebar.addWidget(button2)
        sidebar.addWidget(button3)

        button4 = QPushButton("확대")
        button4.clicked.connect(self.size)
        sidebar.addWidget(button4)

        button5 = QPushButton("시계방향 회전")
        button5.clicked.connect(self.rotate)
        sidebar.addWidget(button5)

        button6 = QPushButton("반시계방향 회전")
        button6.clicked.connect(self.drotate)
        sidebar.addWidget(button6)

        button7 = QPushButton("상하반전")
        button7.clicked.connect(self.flop)
        sidebar.addWidget(button7)

        button8 = QPushButton("흑백")
        button8.clicked.connect(self.black)
        sidebar.addWidget(button8)

        button9 = QPushButton("축소")
        button9.clicked.connect(self.dsize)
        sidebar.addWidget(button9)

        button10 = QPushButton("이미지 합치기")
        button10.clicked.connect(self.add)
        sidebar.addWidget(button10)

        button11 = QPushButton("이미지 저장")
        button11.clicked.connect(self.save_file_dialog)
        sidebar.addWidget(button11)

        button12 = QPushButton("모자이크")
        button12.clicked.connect(self.mosaic)
        sidebar.addWidget(button12)

        main_layout.addLayout(sidebar)

        self.label1 = QLabel(self)
        self.label1.setFixedSize(640, 480)
        main_layout.addWidget(self.label1)

        self.label2 = QLabel(self)
        self.label2.setFixedSize(640, 480)
        main_layout.addWidget(self.label2)

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


    # def save_file_dialog(self):
    #     fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
    #     if fpath:
    #         self.image.save(fpath)

    def save_file_dialog(self):
        cv2.imwrite("./new.jpg", self.tmp_image)



    def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        print(file_name)
        self.image = cv2.imread(file_name[0])
        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image = QImage(
            self.image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)

    def flip_image(self):
        image = cv2.flip(self.image, 1)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    def clear_label(self):
        self.label2.clear()

    # 이미지 확대
    def size(self):
        image = cv2.resize(self.image, (1920, 1280))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        # 이미지 축소
    def dsize(self):
        image = cv2.resize(self.image, (100, 100))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)



    #  오른쪽 90도 회전
    def rotate(self):
        image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        # 계속 회전되게 하려면 for문을 써야할까 아니면 각도를 내가 정할 순 없을까


    # 왼쪽 90도 회전
    def drotate(self):
        image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)


    #  180도 회전
    # def rotate(self):
    #     image = cv2.rotate(self.image, cv2.ROTATE_180)
    #     h, w, _ = image.shape
    #     bytes_per_line = 3 * w
    #     image = QImage(
    #         image.data, w, h, bytes_per_line, QImage.Format_RGB888
    #     ).rgbSwapped()
    #     pixmap = QPixmap(image)
    #     self.label2.setPixmap(pixmap)


    #  상하반전
    def flop(self):
        image = cv2.flip(self.image, 0)
        h, w, _ = image.shape
        # print(image.shape)
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    # 흑백
    def black(self):
        gray_image = self.image.copy()
        image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
        h, w = image.shape
        # bytes_per_line = w

        image = QImage(
            image.data, w, h, QImage.Format_Grayscale8
        )

        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        # gray = cv2.imread(self.image, cv2.IMREAD_GRAYSCALE)
        # gray = QImage(self.image, QImage.IMREAD_GRAYSCALE)
        # gray = QImage(self.image, QImage.Format_RGB888)
        # gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        # grayscale

    # 카피떠서 저장
    # 수정된 이미지 저장
    # 타 기능들로 원본 사진에 효과를 적용시킨 사진(toolbar를 기준으로 오른쪽에 출력되는 이미지)을 현재 위치에
    # newimagefile 이란 이름으로 저장하는 기능


    # 이미지 합치기
    def add(self):
        # image = cv2.add(self.image, cv2.IMREAD_COLOR)
        # image = cv2.imread(self.image, cv2.IMREAD_COLOR)
        # image2 = cv2.imread("opencv.png", cv2.IMREAD_COLOR)
        # h, w, _ = image.shape
        # bytes_per_line = 3 * w
        # image = QImage(
        #     image.data, w, h, bytes_per_line, QImage.Format_RGB888
        # ).rgbSwapped()
        # pixmap = QPixmap(image)
        # self.label2.setPixmap(pixmap)

        image = cv2.imread(self.image, cv2.IMREAD_COLOR)
        image2 = cv2.imread("opencv.png", cv2.IMREAD_COLOR)
        image3 = cv2.add(image, image2)

        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image3)
        self.label2.setPixmap(pixmap)

# img_fg = cv2.imread("opencv_logo.png", cv2.IMREAD_UNCHANGED)  # 4채널 RGBA opencv BGRA
# img_bg = cv2.imread("cat-01.jpg")  # 3채널 RGB -> BGR
# img_bg = cv2.cvtColor(img_bg, cv2.COLOR_BGR2RGB)
# fig, axes = plt.subplots(ncols=2)
# axes[0].imshow(img_fg)
# axes[1].imshow(img_bg)
# resized_img_fg = cv2.resize(img_fg, (int(487*0.5), int(600*0.5)))
# print(f"원본 로고 이미지의 높이: {img_fg.shape[0]} 너비: {img_fg.shape[1]}")
# print(f"처리된 로고 이미지의 높이: {resized_img_fg.shape[0]} 너비: {resized_img_fg.shape[1]}")
# _, mask = cv2.threshold(resized_img_fg[:, :, 3], 1, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
# print(mask.shape)
# print(mask)
# print(mask_inv)
# print(resized_img_fg.shape)
# resized_img_fg = cv2.cvtColor(resized_img_fg, cv2.COLOR_BGRA2BGR)
# print(resized_img_fg.shape)
# h, w, _ = resized_img_fg.shape
# print(f"높이: {h} 너비: {w}")
# print(f"배경사진 높이: {img_bg.shape[0]} 너비: {img_bg.shape[1]}")
# roi = img_bg[10:10+h, 10:10+w]
# print(f"관심영역 높이: {roi.shape[0]} 너비: {roi.shape[1]}")
# resized_img_fg = cv2.cvtColor(resized_img_fg, cv2.COLOR_BGR2RGB)
# masked_fg = cv2.bitwise_and(resized_img_fg, resized_img_fg, mask=mask)
# masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# added = masked_fg + masked_bg
# plt.imshow(added)

    # 모자이크
    def mosaic(self):
        small = cv2.resize(self.image, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
        image =  cv2.resize(small, self.image.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
        self.tmp_image = image

        h, w, c = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

