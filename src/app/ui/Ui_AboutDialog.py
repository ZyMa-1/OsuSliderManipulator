# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(321, 207)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_label = QLabel(AboutDialog)
        self.name_label.setObjectName(u"name_label")
        font = QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name_label)

        self.version_label = QLabel(AboutDialog)
        self.version_label.setObjectName(u"version_label")

        self.verticalLayout.addWidget(self.version_label)

        self.label = QLabel(AboutDialog)
        self.label.setObjectName(u"label")
        self.label.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(AboutDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_box = QDialogButtonBox(AboutDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(AboutDialog)
        self.button_box.rejected.connect(AboutDialog.reject)
        self.button_box.accepted.connect(AboutDialog.accept)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.name_label.setText(QCoreApplication.translate("AboutDialog", u"#####", None))
        self.version_label.setText(QCoreApplication.translate("AboutDialog", u"- Version ### or something", None))
        self.label.setText(QCoreApplication.translate("AboutDialog", u"- Created by <a href=\"https://osu.ppy.sh/u/16357858\">meaningoflife</a>", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"- Project created using Pyside6", None))
    # retranslateUi

