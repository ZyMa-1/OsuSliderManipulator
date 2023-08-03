# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HowToUseThisDialog.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_HowToUseThisDialog(object):
    def setupUi(self, HowToUseThisDialog):
        if not HowToUseThisDialog.objectName():
            HowToUseThisDialog.setObjectName(u"HowToUseThisDialog")
        HowToUseThisDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(HowToUseThisDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.web_engine_view = QWebEngineView(HowToUseThisDialog)
        self.web_engine_view.setObjectName(u"web_engine_view")
        self.web_engine_view.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.web_engine_view)

        self.button_box = QDialogButtonBox(HowToUseThisDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(HowToUseThisDialog)

        QMetaObject.connectSlotsByName(HowToUseThisDialog)
    # setupUi

    def retranslateUi(self, HowToUseThisDialog):
        HowToUseThisDialog.setWindowTitle(QCoreApplication.translate("HowToUseThisDialog", u"Dialog", None))
    # retranslateUi

