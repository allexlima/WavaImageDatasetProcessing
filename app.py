#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import os
import cv2
import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import interface_design
from scipy.interpolate import splprep, splev


class WIBIC(QMainWindow, interface_design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.path_button.clicked.connect(self.path_bt_action)
        self.next_bt.clicked.connect(self.next_action)
        self.previous_bt.clicked.connect(self.previous_action)
        self.save_bt.clicked.connect(self.save_action)
        self.apply_bt.clicked.connect(self.apply_action)
        self.next_bt.setDisabled(True)
        self.previous_bt.setDisabled(True)
        self.save_bt.setDisabled(True)
        self.apply_bt.setDisabled(True)

        self.spin_h_min.valueChanged.connect(self.cv_hsv)
        self.spin_s_min.valueChanged.connect(self.cv_hsv)
        self.spin_v_min.valueChanged.connect(self.cv_hsv)
        self.spin_h_max.valueChanged.connect(self.cv_hsv)
        self.spin_s_max.valueChanged.connect(self.cv_hsv)
        self.spin_v_max.valueChanged.connect(self.cv_hsv)

        self.fit_screen.stateChanged.connect(self.options_check)
        self.keep_size.stateChanged.connect(self.options_check)
        self.morphological_operations.stateChanged.connect(self.apply_action)
        self.blur.stateChanged.connect(self.apply_action)

        self.image = None
        self.original_image = None
        self.img_list = []
        self.img_list_count = 0
        self.hsv_max = []
        self.hsv_min = []
        self.size = ()
        self.mt = []

        self.alert("This software was designed to improve the time of manual digital images processing of big image datasets \n\n By Allex Lima <allexlima@unn.edu.br> - http://allexlima.com", "Well Come!")

    def alert(self, text, title="Alert", code=2):
        message = QMessageBox(self)
        message.setIcon(code)
        message.setText(unicode(text))
        message.setWindowTitle(title)
        message.setWindowModality(Qt.ApplicationModal)
        message.exec_()

    def load_img(self):

        if self.keep_size.isChecked():
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            self.size = (self.size_w.value(), self.size_h.value())
            self.cv_resize()

        self.size = (self.image.shape[1], self.image.shape[0])
        self.size_h.setValue(self.size[1])
        self.size_w.setValue(self.size[0])

        byte_value = self.image.shape[2]
        byte_value = byte_value * self.size[0]

        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        image_preview = QImage(self.image, self.size[0], self.size[1], byte_value, QImage.Format_RGB888)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        if self.fit_screen.isChecked():
            self.img.setPixmap(QPixmap.fromImage(image_preview).scaledToWidth(400))
        else:
            self.img.setPixmap(QPixmap.fromImage(image_preview))

    def show_img(self, keep_object_image=None):
        index = self.img_list_count

        filename = str(self.img_list[index]).split("/")[-1] + "*"

        if keep_object_image is None:
            self.original_image = self.image = cv2.imread(self.img_list[index])
            filename = str(self.img_list[index]).split("/")[-1]

        self.file_text.setText(filename)
        self.setWindowTitle("Wava Image Dataset Processing - " + filename)
        self.load_img()

    def path_bt_action(self):
        self.path_text.setText(str(QFileDialog.getExistingDirectory(QFileDialog(), "Select Directory")))
        self.run()

    def run(self):
        self.img_list = []

        try:
            for filename in os.listdir(str(self.path_text.text())):
                if filename.endswith(".jpg"):
                    self.img_list.append(os.path.join(str(self.path_text.text()), filename))

        except OSError, e:
            self.alert(u"Error: " + e.message, code=3)

        self.img_list.sort()
        self.img_list_count = -1
        self.next_bt.setDisabled(False)
        self.previous_bt.setDisabled(False)
        self.save_bt.setDisabled(False)
        self.apply_bt.setDisabled(False)
        self.next_action()

    def next_action(self):
        if self.img_list_count < len(self.img_list):
            self.img_list_count += 1
            self.show_img()
        else:
            self.alert(u"This was the last file. Restarting counter...")
            self.img_list_count = -1

    def previous_action(self):
        self.img_list_count -= 1
        self.show_img()

    def cv_hsv(self):
        self.image = self.original_image
        self.hsv_min = [self.spin_h_min.value(), self.spin_s_min.value(), self.spin_v_min.value()]
        self.hsv_max = [self.spin_h_max.value(), self.spin_s_max.value(), self.spin_v_max.value()]
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower_blue = np.array(self.hsv_min)
        upper_blue = np.array(self.hsv_max)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        self.image = cv2.bitwise_and(self.image, self.image, mask=mask)
        self.options_check()
        self.show_img(True)

    def cv_morph_op(self):
        kernel = np.ones((5, 5), np.uint8)
        self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)

    def cv_blur(self):
        self.image = cv2.blur(self.image, (2, 2))

    def cv_resize(self):
        self.size = (self.size_w.value(), self.size_h.value())
        self.image = cv2.resize(cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR), self.size, interpolation=cv2.INTER_LANCZOS4)

    def options_check(self):
        if self.morphological_operations.isChecked():
            self.cv_morph_op()
        if self.blur.isChecked():
            self.cv_blur()
        self.load_img()

    def apply_action(self):
        self.cv_hsv()
        self.cv_resize()
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        self.show_img(True)

    def save_action(self):
        confirm = False
        self.apply_action()
        
        if confirm:
            reply = QMessageBox.question(QMessageBox(), 'Have you sure?', "Be"
                                         "careful! The opened image will be"
                                         "replaced with the new settings. Have"
                                         "you sure?", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                cv2.imwrite(self.img_list[self.img_list_count], self.image)
                self.alert("Image saved successfully!")
        else:
            cv2.imwrite(self.img_list[self.img_list_count], self.image)

if __name__ == "__main__":
        app = QApplication(['Wava Image Dataset Processing - WADP'])
        window = WIBIC()
        window.show()
        app.exec_()
