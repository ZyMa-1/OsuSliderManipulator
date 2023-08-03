# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(554, 560)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.actionHow_to_use_it = QAction(MainWindow)
        self.actionHow_to_use_it.setObjectName(u"actionHow_to_use_it")
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.action_always_stay_on_top = QAction(MainWindow)
        self.action_always_stay_on_top.setObjectName(u"action_always_stay_on_top")
        self.action_always_stay_on_top.setCheckable(True)
        self.action_how_to_use_this = QAction(MainWindow)
        self.action_how_to_use_this.setObjectName(u"action_how_to_use_this")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)

        self.slider_tick_rate_line_edit = QLineEdit(self.tab_2)
        self.slider_tick_rate_line_edit.setObjectName(u"slider_tick_rate_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_tick_rate_line_edit.sizePolicy().hasHeightForWidth())
        self.slider_tick_rate_line_edit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.slider_tick_rate_line_edit, 0, 1, 1, 1)

        self.destination_line_edit = QLineEdit(self.tab_2)
        self.destination_line_edit.setObjectName(u"destination_line_edit")
        sizePolicy.setHeightForWidth(self.destination_line_edit.sizePolicy().hasHeightForWidth())
        self.destination_line_edit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.destination_line_edit, 8, 1, 1, 1)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_16, 12, 0, 1, 1)

        self.sliders_text_edit = QTextEdit(self.tab_2)
        self.sliders_text_edit.setObjectName(u"sliders_text_edit")
        self.sliders_text_edit.setAcceptRichText(False)

        self.gridLayout_3.addWidget(self.sliders_text_edit, 10, 1, 1, 1)

        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 7, 0, 1, 1)

        self.beatmap_sv_line_edit = QLineEdit(self.tab_2)
        self.beatmap_sv_line_edit.setObjectName(u"beatmap_sv_line_edit")
        sizePolicy.setHeightForWidth(self.beatmap_sv_line_edit.sizePolicy().hasHeightForWidth())
        self.beatmap_sv_line_edit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.beatmap_sv_line_edit, 7, 1, 1, 1)

        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 8, 0, 1, 1)

        self.result_timing_text_edit = QTextEdit(self.tab_2)
        self.result_timing_text_edit.setObjectName(u"result_timing_text_edit")
        self.result_timing_text_edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.result_timing_text_edit, 12, 1, 1, 1)

        self.beat_length_line_edit = QLineEdit(self.tab_2)
        self.beat_length_line_edit.setObjectName(u"beat_length_line_edit")
        sizePolicy.setHeightForWidth(self.beat_length_line_edit.sizePolicy().hasHeightForWidth())
        self.beat_length_line_edit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.beat_length_line_edit, 2, 1, 1, 1)

        self.do_stuff_button = QPushButton(self.tab_2)
        self.do_stuff_button.setObjectName(u"do_stuff_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.do_stuff_button.sizePolicy().hasHeightForWidth())
        self.do_stuff_button.setSizePolicy(sizePolicy1)
        self.do_stuff_button.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.do_stuff_button, 11, 1, 1, 1)

        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 10, 0, 1, 1)

        self.current_sv_multiplier_line_edit = QLineEdit(self.tab_2)
        self.current_sv_multiplier_line_edit.setObjectName(u"current_sv_multiplier_line_edit")
        sizePolicy.setHeightForWidth(self.current_sv_multiplier_line_edit.sizePolicy().hasHeightForWidth())
        self.current_sv_multiplier_line_edit.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.current_sv_multiplier_line_edit, 3, 1, 1, 1)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 9, 0, 1, 1)

        self.timing_example_data_line_edit = QLineEdit(self.tab_2)
        self.timing_example_data_line_edit.setObjectName(u"timing_example_data_line_edit")

        self.gridLayout_3.addWidget(self.timing_example_data_line_edit, 9, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout = QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, 10, -1)
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 8, 0, 1, 1)

        self.destination_line_edit_2 = QLineEdit(self.tab_3)
        self.destination_line_edit_2.setObjectName(u"destination_line_edit_2")
        sizePolicy.setHeightForWidth(self.destination_line_edit_2.sizePolicy().hasHeightForWidth())
        self.destination_line_edit_2.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.destination_line_edit_2, 8, 1, 1, 1)

        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_21, 11, 0, 1, 1)

        self.do_stuff_button_2 = QPushButton(self.tab_3)
        self.do_stuff_button_2.setObjectName(u"do_stuff_button_2")
        sizePolicy1.setHeightForWidth(self.do_stuff_button_2.sizePolicy().hasHeightForWidth())
        self.do_stuff_button_2.setSizePolicy(sizePolicy1)
        self.do_stuff_button_2.setMinimumSize(QSize(0, 45))

        self.gridLayout_4.addWidget(self.do_stuff_button_2, 10, 1, 1, 1)

        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 9, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.choose_osu_file_line_edit_2 = QLineEdit(self.tab_3)
        self.choose_osu_file_line_edit_2.setObjectName(u"choose_osu_file_line_edit_2")
        self.choose_osu_file_line_edit_2.setMinimumSize(QSize(100, 0))
        self.choose_osu_file_line_edit_2.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.choose_osu_file_line_edit_2)

        self.open_osu_file_button_2 = QPushButton(self.tab_3)
        self.open_osu_file_button_2.setObjectName(u"open_osu_file_button_2")

        self.horizontalLayout_3.addWidget(self.open_osu_file_button_2)

        self.choose_osu_file_button_2 = QPushButton(self.tab_3)
        self.choose_osu_file_button_2.setObjectName(u"choose_osu_file_button_2")
        self.choose_osu_file_button_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.choose_osu_file_button_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.result_timing_text_edit_2 = QTextEdit(self.tab_3)
        self.result_timing_text_edit_2.setObjectName(u"result_timing_text_edit_2")
        self.result_timing_text_edit_2.setReadOnly(True)

        self.gridLayout_4.addWidget(self.result_timing_text_edit_2, 11, 1, 1, 1)

        self.sliders_text_edit_2 = QTextEdit(self.tab_3)
        self.sliders_text_edit_2.setObjectName(u"sliders_text_edit_2")
        self.sliders_text_edit_2.setAcceptRichText(False)

        self.gridLayout_4.addWidget(self.sliders_text_edit_2, 9, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_4)

        self.tab_widget.addTab(self.tab_3, "")

        self.horizontalLayout_2.addWidget(self.tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 554, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.action_how_to_use_this)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.action_about)
        self.menuSettings.addAction(self.action_settings)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"{}", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHow_to_use_it.setText(QCoreApplication.translate("MainWindow", u"How to use it", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"Settings...", None))
        self.action_always_stay_on_top.setText(QCoreApplication.translate("MainWindow", u"Always stay on top", None))
        self.action_how_to_use_this.setText(QCoreApplication.translate("MainWindow", u"How to use this", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Current SV mulitplier (float):", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Beat Length (float) (ms):", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Result timing:</p><p align=\"center\">If timing example data not specified: </p><p align=\"center\">(time, beat length, uninherited)</p><p align=\"center\">If timing example data is specified: </p><p align=\"center\">(full timing point)</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Beatmap SV (float):", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Slider tick rate (float):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destination (int) (ms):", None))
        self.do_stuff_button.setText(QCoreApplication.translate("MainWindow", u"Do stuff", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sliders (hitobjects from .osu file):</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timing example (OPTIONAL):\n"
"(one timing point from .osu file, \n"
"doesn't matter inherited or uninherited)", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sliders v1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destination (int) (ms):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Result timing:</p><p align=\"center\">(full timing point)</p></body></html>", None))
        self.do_stuff_button_2.setText(QCoreApplication.translate("MainWindow", u"Do stuff", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Sliders (hitobjects from .osu file):</p></body></html>", None))
        self.open_osu_file_button_2.setText(QCoreApplication.translate("MainWindow", u"open in notepad", None))
        self.choose_osu_file_button_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose .osu file:", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Sliders v2", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

