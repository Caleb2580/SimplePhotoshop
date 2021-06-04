from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect, QPropertyAnimation, QTimeLine, QTimer, QThread, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QTransform
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog, QLabel, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QSpinBox

from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt

import functools
import threading
from math import *

from photoshop import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.brush_size = 20

        self.MinusSizeButton.clicked.connect(self.decrease_brush_size)
        self.PlusSizeButton.clicked.connect(self.increase_brush_size)

        self.widget_layers = []
        self.button_layers = []
        self.layers = []
        self.locations = []
        self.selected_layer = -1

        self.color = (255, 255, 255)
        self.selected_tool = ''
        self.update_picture()

        self.showing_popup = False

        self.canvas_pressed = False
        self.start_loc = None
        self.canvas.mousePressEvent = functools.partial(self.canvas_clicked)
        self.canvas.mouseReleaseEvent = functools.partial(self.canvas_stop_click)

        self.Brush.clicked.connect(lambda state, new_t='Brush': self.set_tool(new_t))
        self.Eraser.clicked.connect(lambda state, new_t='Eraser': self.set_tool(new_t))
        self.Move.clicked.connect(lambda state, new_t='Move': self.set_tool(new_t))
        self.Smooth.clicked.connect(lambda state, new_t='Smooth': self.set_tool(new_t))

        self.AddLayerButton.clicked.connect(self.add_layer_button_clicked)

        self.DeleteLayerButton.clicked.connect(self.delete_layer_button_clicked)

        self.SaveButton.clicked.connect(self.save_image)

        self.ColorExample.clicked.connect(self.show_popup)

        # QPushButton[objectName = "ColorExample"] {
        #     background - color: rgb(255, 0, 0);
        #     border - width: 0px;
        #     border - style: solid;
        #     border - color: rgb(20, 20, 20);
        # }
        #
        # QPushButton[objectName = "ColorExample"]::pressed
        # {
        #     border - width: 2px;
        # }
        self.ColorExample.setStyleSheet('QPushButton[objectName = "ColorExample"] {\n'
                                        '   background-color: rgb' + str(self.color) + ';\n'
                                        '   border-width: 0px;\n'
                                        '   border-style: solid;\n'
                                        '   border-color: rgb(20, 20, 20);\n'
                                        '}\n'
                                        'QPushButton[objectName = "ColorExample"]::pressed\n'
                                        '{\n'
                                        '   border-width: 2px;\n'
                                        '}')

    def save_image(self):
        if len(self.layers) > 0:
            im = self.layers[0].copy().convert('RGBA')
            for i in range(1, len(self.layers)):
                new_im = self.layers[i].copy().convert('RGBA')
                im.paste(new_im, self.locations[i], new_im)
            self.canvas.setPixmap(QtGui.QPixmap.fromImage(ImageQt(im)))
            im.save('SavedImage.png')

    def delete_layer_button_clicked(self):
        self.widget_layers[self.selected_layer].deleteLater()
        ind = self.widget_layers.index(self.widget_layers[self.selected_layer])
        self.widget_layers.pop(ind)
        self.layers.pop(self.layers.index(self.layers[self.selected_layer]))
        self.button_layers.pop(self.button_layers.index(self.button_layers[self.selected_layer]))

        for i in range(0, len(self.button_layers)):
            self.button_layers[i].clicked.disconnect()
            self.button_layers[i].clicked.connect(lambda state, x=i: self.on_layer_clicked(i))

        self.selected_layer = -1
        self.update_picture()

    def add_layer_button_clicked(self):
        filename = QFileDialog.getOpenFileName()
        try:
            self.add_layer(Image.open(filename[0]), '')
        except:
            pass

    def add_layer(self, im, nm):
        im.convert('RGBA')

        if 700 < im.size[0]:
            percent = 700 / float(im.size[0])
            im = im.resize((700, int(float(im.size[1]) * float(float(percent)))), Image.NEAREST)
        if 500 < im.size[1]:
            percent = 500 / float(im.size[0])
            im = im.resize((500, int(float(im.size[1]) * float(float(percent)))), Image.NEAREST)

        if -1 < self.selected_layer < len(self.layers):
            if self.layers[self.selected_layer].size[0] < im.size[0]:
                percent = self.layers[self.selected_layer].size[0] / float(im.size[0])
                im = im.resize((int(self.layers[self.selected_layer].size[0]), int(float(im.size[1]) * float(float(percent)))), Image.NEAREST)
            if self.layers[self.selected_layer].size[1] < im.size[1]:
                percent = self.layers[self.selected_layer].size[1] / float(im.size[0])
                im = im.resize((int(self.layers[self.selected_layer].size[0]), int(float(im.size[1]) * float(float(percent)))), Image.NEAREST)

        layer = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        layer.setMinimumSize(QtCore.QSize(0, 50))
        layer.setMaximumSize(QtCore.QSize(16777215, 50))
        layer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        layer.setFrameShadow(QtWidgets.QFrame.Raised)
        layer.setObjectName("layer")
        but = QtWidgets.QPushButton(layer)
        but.setGeometry(QtCore.QRect(0, 5, 40, 40))
        but.setText("")
        but.setObjectName("but")
        but.setStyleSheet('background-color: transparent;\n'
                          'border-width: 0px;\n'
                          'border-style: solid;')
        but.setIcon(QIcon(QtGui.QPixmap.fromImage(ImageQt(im))))
        but.setIconSize(QSize(35, 35))
        label = QtWidgets.QLabel(layer)
        label.setGeometry(QtCore.QRect(50, 17, 60, 15))
        label.setObjectName("label")
        label.setStyleSheet('background-color: transparent;\n'
                            'color: white;')
        if nm != "":
            label.setText(nm)
        else:
            label.setText(f'Layer {str(len(self.layers))}')

        but.clicked.connect(lambda state, x=len(self.layers): self.on_layer_clicked(x))

        if self.selected_layer >= 0:
            self.widget_layers[self.selected_layer].setStyleSheet('background-color: transparent;\n'
                                                                  'color: white;')

        self.selected_layer = len(self.layers)
        self.layers.append(im.convert('RGBA'))
        self.widget_layers.append(layer)
        self.button_layers.append(but)
        self.LayersLayout.addWidget(layer)
        self.locations.append((0, 0))

        self.widget_layers[self.selected_layer].setStyleSheet('background-color: rgb(75, 75, 75);\n'
                                                              'color: white;')

        self.update_picture()

    def on_layer_clicked(self, lay_num):
        self.widget_layers[self.selected_layer].setStyleSheet('background-color: transparent;\n'
                                                              'color: white;')
        print(lay_num)
        self.selected_layer = lay_num
        self.widget_layers[lay_num].setStyleSheet('background-color: rgb(75, 75, 75);\n'
                                                  'color: white;')


    def set_tool(self, new_tool):
        self.selected_tool = new_tool

    def canvas_stop_click(self, event):
        self.canvas.setMouseTracking(False)
        self.canvas_pressed = False
        self.start_loc = None

    def canvas_clicked(self, event):
        self.canvas.setMouseTracking(True)
        th = threading.Thread(target=self.draw_on_picture, args=(event.pos().x(), event.pos().y(),))
        th.start()
        th.join()
        self.canvas_pressed = True
        self.start_loc = [(event.pos().x(), event.pos().y()), self.locations[self.selected_layer]]

    def mouseMoveEvent(self, event):
        if self.canvas_pressed and (event.pos().x() - self.canvas.x()) >= 0 <= (event.pos().y() - self.canvas.y()) and (event.pos().x() - self.canvas.x()) <= self.canvas.width() and (event.pos().y() - self.canvas.y()) <= self.canvas.height():
            th = threading.Thread(target=self.draw_on_picture, args=(event.pos().x() - self.canvas.x(), event.pos().y() - self.canvas.y(),))
            th.start()
            th.join()

    def smooth_pixel(self, x, y):
        if 0 <= self.selected_layer < len(self.layers) and x < self.canvas.width() and y < self.canvas.height():
            pixels = self.layers[self.selected_layer].load()
            reds = []
            greens = []
            blues = []
            alpha = 0
            for i in range(x-1, x+1):
                try:
                    if i == x:
                        try:
                            col = pixels[x, y + 1]
                            if col[3] > 0:
                                alpha = col[3]
                                reds.append(col[0])
                                greens.append(col[1])
                                blues.append(col[2])
                        except:
                            pass
                        try:
                            col = pixels[x, y - 1]
                            if col[3] > 0:
                                alpha = col[3]
                                reds.append(col[0])
                                greens.append(col[1])
                                blues.append(col[2])
                        except:
                            pass
                    else:
                        col = pixels[x, y]
                        if col[3] > 0:
                            alpha = col[3]
                            reds.append(col[0])
                            greens.append(col[1])
                            blues.append(col[2])
                except:
                    pass

            if len(reds) > 0 and alpha > 0:
                pixels[x, y] = (int(sum(reds) / len(reds)), int(sum(greens) / len(greens)), int(sum(blues) / len(blues)), alpha)

    def draw_on_picture(self, x, y):
        if 0 <= self.selected_layer < len(self.layers) and x < self.canvas.width() and y < self.canvas.height():
            pixels = self.layers[self.selected_layer].load()

            if self.selected_tool == 'Brush':
                x -= self.locations[self.selected_layer][0]
                y -= self.locations[self.selected_layer][1]
                try:
                    pixels[x, y] = self.color
                except:
                    pass
                for i in range(x-self.brush_size, x + 1):
                    for q in range(0, (x - i - self.brush_size) * -1):
                        try:
                            pixels[i, y + q] = self.color
                        except:
                            pass
                        try:
                            pixels[i, y - q] = self.color
                        except:
                            pass
                for i in range(x - 1, x + self.brush_size):
                    for q in range(0, (i - x - self.brush_size) * -1):
                        try:
                            pixels[i, y + q] = self.color
                        except:
                            pass
                        try:
                            pixels[i, y - q] = self.color
                        except:
                            pass
            elif self.selected_tool == 'Eraser':
                x -= self.locations[self.selected_layer][0]
                y -= self.locations[self.selected_layer][1]
                try:
                    pixels[x, y] = (255, 255, 255, 1)
                except:
                    pass
                for i in range(x-self.brush_size, x + 1):
                    for q in range(0, (x - i - self.brush_size) * -1):
                        try:
                            pixels[i, y + q] = (255, 255, 255, 0)
                        except:
                            pass
                        try:
                            pixels[i, y - q] = (255, 255, 255, 0)
                        except:
                            pass
                for i in range(x - 1, x + self.brush_size):
                    for q in range(0, (i - x - self.brush_size) * -1):
                        try:
                            pixels[i, y + q] = (255, 255, 255, 0)
                        except:
                            pass
                        try:
                            pixels[i, y - q] = (255, 255, 255, 0)
                        except:
                            pass
            elif self.selected_tool == 'Move':
                if self.start_loc is not None and self.selected_layer > 0:
                    try:
                        past_loc = self.locations[self.selected_layer]
                        new_loc = (self.start_loc[1][0] + (x - self.start_loc[0][0]), self.start_loc[1][0] + (y - self.start_loc[0][1]))
                        self.locations[self.selected_layer] = new_loc
                        try:
                            self.update_picture()
                        except:
                            self.locations[self.selected_layer] = past_loc
                    except:
                        pass
                elif self.start_loc is not None and self.selected_layer == 0:
                    print("Can't move background image!")
                    self.canvas_pressed = False
                    self.start_loc = None
            elif self.selected_tool == 'Smooth':
                x -= self.locations[self.selected_layer][0]
                y -= self.locations[self.selected_layer][1]
                for i in range(x-self.brush_size, x + 1):
                    for q in range(0, (x - i - self.brush_size) * -1):
                        try:
                            self.smooth_pixel(i, y + q)
                        except:
                            pass
                        try:
                            self.smooth_pixel(i, y - q)
                        except:
                            pass
                for i in range(x - 1, x + self.brush_size):
                    for q in range(0, (i - x - self.brush_size) * -1):
                        try:
                            self.smooth_pixel(i, y + q)
                        except:
                            pass
                        try:
                            self.smooth_pixel(i, y - q)
                        except:
                            pass
            try:
                self.update_picture()
            except:
                print("Couldn't update")
        else:
            print('No selected layer')

    def show_popup(self):
        pop = ColorPopup(self, self.color)
        pop.show()

    def set_color(self, colors):
        self.color = colors
        self.ColorExample.setStyleSheet('QPushButton[objectName = "ColorExample"] {\n'
                                        '   background-color: rgb' + str(self.color) + ';\n'
                                                                                       '   border-width: 0px;\n'
                                                                                       '   border-style: solid;\n'
                                                                                       '   border-color: rgb(20, 20, 20);\n'
                                                                                       '}\n'
                                                                                       'QPushButton[objectName = "ColorExample"]::pressed\n'
                                                                                       '{\n'
                                                                                       '   border-width: 2px;\n'
                                                                                       '}')

    def update_picture(self):
        if 0 <= self.selected_layer < len(self.layers):
            self.button_layers[self.selected_layer].setIcon(QIcon(QtGui.QPixmap.fromImage(ImageQt(self.layers[self.selected_layer]))))
            self.button_layers[self.selected_layer].setIconSize(QSize(35, 35))
        else:
            print('No selected layer')

        if len(self.layers) > 0:
            im = self.layers[0].copy().convert('RGBA')
            for i in range(1, len(self.layers)):
                new_im = self.layers[i].copy().convert('RGBA')
                im.paste(new_im, self.locations[i], new_im)
            self.canvas.setPixmap(QtGui.QPixmap.fromImage(ImageQt(im)))
        else:
            self.canvas.clear()


    def decrease_brush_size(self):
        if self.brush_size - 3 > 0:
            self.brush_size -= 3
        else:
            self.brush_size = 0

    def increase_brush_size(self):
        if self.brush_size + 3 < 50:
            self.brush_size += 3
        else:
            self.brush_size = 50


class ColorPopup(QDialog):
    def __init__(self, parent, colors):
        super().__init__(parent)
        self.par = parent
        self.resize(300, 200)
        self.setStyleSheet('background-color: black;\n'
                           'color: white;')

        self.red = colors[0]
        self.green = colors[1]
        self.blue = colors[2]

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 281, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.redBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.redBox.setMinimumSize(QtCore.QSize(50, 20))
        self.redBox.setMaximumSize(QtCore.QSize(50, 20))
        self.redBox.setMaximum(255)
        self.redBox.setObjectName("redBox")
        self.horizontalLayout.addWidget(self.redBox)
        self.blueBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.blueBox.setMinimumSize(QtCore.QSize(50, 20))
        self.blueBox.setMaximumSize(QtCore.QSize(50, 20))
        self.blueBox.setMaximum(255)
        self.blueBox.setObjectName("blueBox")
        self.horizontalLayout.addWidget(self.blueBox)
        self.greenBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.greenBox.setMinimumSize(QtCore.QSize(50, 20))
        self.greenBox.setMaximumSize(QtCore.QSize(50, 20))
        self.greenBox.setMaximum(255)
        self.greenBox.setObjectName("greenBox")
        self.horizontalLayout.addWidget(self.greenBox)
        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setGeometry(QtCore.QRect(100, 120, 100, 25))
        self.saveButton.setText('Save')
        self.saveButton.setStyleSheet('background-color: black;\n'
                                      'color: white;\n'
                                      'border-width: 2px;\n'
                                      'border-style: solid;\n'
                                      'border-color: white;')
        self.saveButton.setObjectName("saveButton")

        self.saveButton.clicked.connect(self.save_colors)

    def save_colors(self):
        print('Saved')
        self.par.set_color((int(self.redBox.value()), int(self.blueBox.value()), int(self.greenBox.value())))
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open('style.css', 'r') as style:
        app.setStyleSheet(style.read())
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())










