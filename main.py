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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")
        
        # 메뉴바 만들기
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("파일")
        exit = QAction("나가기", self, triggered=qApp.quit)
        self.menu_file.addAction(exit)

        save = QAction("저장", self)
        self.menu_file.addAction(save)
        
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
        print(image.shape)
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    # 흑백
    def black(self):
        # image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        # print(image.shape)
        # h, w = image.shape
        # bytes_per_line = 3 * w
        # image = QImage(
        #     image.data, w, h, bytes_per_line, QImage.Format_RGB888
        # ).rgbSwapped()
        # pixmap = QPixmap(image)
        # self.label2.setPixmap(pixmap)

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

    # 이미지 흑백
    # def filter(self):
    #     image = image.filter(ImageFilter.GaussianBlur(10))

    # original = cv2.imread(fname, cv2.IMREAD_COLOR)
    # gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    # unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

    # def filter(self):
    #     img = cv2.imread("sudoku.jpg")
    #     img = img[..., ::-1]

    #     gx_kernel = np.array([-1, 1])
    #     gy_kernel = np.array([[-1], [1]])

    #     edge_gx = cv2.filter2D(img, -1, gx_kernel)
    #     edge_gy = cv2.filter2D(img, -1, gy_kernel)

    # 이미지 저장
    # def save(self):
    #     image = cv2.imread('./cat_save.jpg', cv2.IMREAD_GRAYSCALE)
    #     cv2.imwrite('./cat_save.jpg', image)



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

