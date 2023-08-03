# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(497, 313)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setMinimumSize(QSize(0, 0))
        SettingsDialog.setBaseSize(QSize(0, 0))
        SettingsDialog.setAutoFillBackground(False)
        SettingsDialog.setSizeGripEnabled(False)
        SettingsDialog.setModal(False)
        self.gridLayout_3 = QGridLayout(SettingsDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 10)
        self.side_menu_list = QListWidget(SettingsDialog)
        QListWidgetItem(self.side_menu_list)
        QListWidgetItem(self.side_menu_list)
        QListWidgetItem(self.side_menu_list)
        self.side_menu_list.setObjectName(u"side_menu_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_menu_list.sizePolicy().hasHeightForWidth())
        self.side_menu_list.setSizePolicy(sizePolicy1)
        self.side_menu_list.setMinimumSize(QSize(100, 0))
        self.side_menu_list.setMaximumSize(QSize(100, 16777215))
        self.side_menu_list.setSortingEnabled(False)

        self.gridLayout.addWidget(self.side_menu_list, 0, 0, 1, 1)

        self.stacked_widget = QStackedWidget(SettingsDialog)
        self.stacked_widget.setObjectName(u"stacked_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stacked_widget.sizePolicy().hasHeightForWidth())
        self.stacked_widget.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        self.stacked_widget.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(8)
        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.osu_folder_path_line_edit = QLineEdit(self.page)
        self.osu_folder_path_line_edit.setObjectName(u"osu_folder_path_line_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.osu_folder_path_line_edit.sizePolicy().hasHeightForWidth())
        self.osu_folder_path_line_edit.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(9)
        self.osu_folder_path_line_edit.setFont(font1)
        self.osu_folder_path_line_edit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.osu_folder_path_line_edit)

        self.choose_osu_folder_btn = QPushButton(self.page)
        self.choose_osu_folder_btn.setObjectName(u"choose_osu_folder_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.choose_osu_folder_btn.sizePolicy().hasHeightForWidth())
        self.choose_osu_folder_btn.setSizePolicy(sizePolicy4)
        self.choose_osu_folder_btn.setMinimumSize(QSize(0, 0))
        self.choose_osu_folder_btn.setMaximumSize(QSize(35, 16777215))
        self.choose_osu_folder_btn.setFont(font1)
        self.choose_osu_folder_btn.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.choose_osu_folder_btn)


        self.gridLayout_6.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_6.addWidget(self.label_2, 3, 0, 1, 1)

        self.line_2 = QFrame(self.page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_2, 1, 0, 1, 1)

        self.always_stay_on_top_check_box = QCheckBox(self.page)
        self.always_stay_on_top_check_box.setObjectName(u"always_stay_on_top_check_box")
        font2 = QFont()
        font2.setPointSize(16)
        self.always_stay_on_top_check_box.setFont(font2)

        self.gridLayout_6.addWidget(self.always_stay_on_top_check_box, 4, 1, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_6.addWidget(self.label, 4, 0, 1, 1)

        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        self.label_16.setFont(font3)

        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stacked_widget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_8.setVerticalSpacing(8)
        self.label_18 = QLabel(self.page_3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setFont(font3)

        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slidesrv1_save_fields_yes_radio_button = QRadioButton(self.page_3)
        self.slidesrv1_save_fields_yes_radio_button.setObjectName(u"slidesrv1_save_fields_yes_radio_button")
        self.slidesrv1_save_fields_yes_radio_button.setFont(font1)

        self.horizontalLayout_5.addWidget(self.slidesrv1_save_fields_yes_radio_button)

        self.slidersv1_save_fields_no_radio_button = QRadioButton(self.page_3)
        self.slidersv1_save_fields_no_radio_button.setObjectName(u"slidersv1_save_fields_no_radio_button")
        self.slidersv1_save_fields_no_radio_button.setFont(font1)

        self.horizontalLayout_5.addWidget(self.slidersv1_save_fields_no_radio_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout_8.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.line_4 = QFrame(self.page_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_4, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 4, 0, 1, 2)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_8.addWidget(self.label_4, 3, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.stacked_widget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_9.setVerticalSpacing(8)
        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setFont(font3)

        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slidesrv2_save_fields_yes_radio_button = QRadioButton(self.page_2)
        self.slidesrv2_save_fields_yes_radio_button.setObjectName(u"slidesrv2_save_fields_yes_radio_button")
        self.slidesrv2_save_fields_yes_radio_button.setFont(font1)

        self.horizontalLayout_7.addWidget(self.slidesrv2_save_fields_yes_radio_button)

        self.slidersv2_save_fields_no_radio_button = QRadioButton(self.page_2)
        self.slidersv2_save_fields_no_radio_button.setObjectName(u"slidersv2_save_fields_no_radio_button")
        self.slidersv2_save_fields_no_radio_button.setFont(font1)

        self.horizontalLayout_7.addWidget(self.slidersv2_save_fields_no_radio_button)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)


        self.gridLayout_9.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)

        self.line_5 = QFrame(self.page_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_5, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 4, 0, 1, 2)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_9.addWidget(self.label_5, 3, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.stacked_widget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stacked_widget, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.button_box = QDialogButtonBox(SettingsDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.button_box, 1, 0, 1, 1)


        self.retranslateUi(SettingsDialog)

        self.side_menu_list.setCurrentRow(0)
        self.stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))

        __sortingEnabled = self.side_menu_list.isSortingEnabled()
        self.side_menu_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.side_menu_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("SettingsDialog", u"General", None));
        ___qlistwidgetitem1 = self.side_menu_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("SettingsDialog", u"Sliders v1", None));
        ___qlistwidgetitem2 = self.side_menu_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("SettingsDialog", u"Sliders v2", None));
        self.side_menu_list.setSortingEnabled(__sortingEnabled)

        self.choose_osu_folder_btn.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Osu folder path:", None))
        self.always_stay_on_top_check_box.setText("")
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Main widget always stay on top:", None))
        self.label_16.setText(QCoreApplication.translate("SettingsDialog", u"General", None))
        self.label_18.setText(QCoreApplication.translate("SettingsDialog", u"Sliders v1", None))
        self.slidesrv1_save_fields_yes_radio_button.setText(QCoreApplication.translate("SettingsDialog", u"Yikes", None))
        self.slidersv1_save_fields_no_radio_button.setText(QCoreApplication.translate("SettingsDialog", u"Nein", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Save fields:", None))
        self.label_19.setText(QCoreApplication.translate("SettingsDialog", u"Sliders v2", None))
        self.slidesrv2_save_fields_yes_radio_button.setText(QCoreApplication.translate("SettingsDialog", u"Yikes", None))
        self.slidersv2_save_fields_no_radio_button.setText(QCoreApplication.translate("SettingsDialog", u"Nein", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Save fields:", None))
    # retranslateUi

