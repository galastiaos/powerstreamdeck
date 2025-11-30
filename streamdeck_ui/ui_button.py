
################################################################################
## FIXED version of ui_button.py
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)
from streamdeck_ui import resources_rc

class Ui_ButtonForm(object):
    def setupUi(self, ButtonForm):
        if not ButtonForm.objectName():
            ButtonForm.setObjectName(u"ButtonForm")
        ButtonForm.resize(568, 778)
        self.formLayout = QFormLayout(ButtonForm)

        self.label = QLabel(ButtonForm)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.add_image = QPushButton(ButtonForm)
        self.horizontalLayout_2.addWidget(self.add_image)
        self.remove_image = QPushButton(ButtonForm)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.remove_image.setSizePolicy(sizePolicy)
        self.remove_image.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_image.setIcon(icon)
        self.horizontalLayout_2.addWidget(self.remove_image)
        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.label_9 = QLabel(ButtonForm)
        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.background_color = QPushButton(ButtonForm)
        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.background_color)

        self.label_2 = QLabel(ButtonForm)
        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.text = QTextEdit(ButtonForm)
        self.horizontalLayout_3.addWidget(self.text)

        self.verticalLayout_4 = QVBoxLayout()
        self.text_v_align = QPushButton(ButtonForm)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/vertical-align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_v_align.setIcon(icon1)
        self.verticalLayout_4.addWidget(self.text_v_align)
        self.text_h_align = QPushButton(ButtonForm)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/vertical-align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_h_align.setIcon(icon2)
        self.verticalLayout_4.addWidget(self.text_h_align)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)

        self.label_4 = QLabel(ButtonForm)
        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.text_font = QComboBox(ButtonForm)
        self.horizontalLayout.addWidget(self.text_font)
        self.text_font_style = QComboBox(ButtonForm)
        self.horizontalLayout.addWidget(self.text_font_style)
        self.text_font_size = QSpinBox(ButtonForm)
        self.text_font_size.setMinimum(12)
        self.text_font_size.setMaximum(72)
        self.horizontalLayout.addWidget(self.text_font_size)
        self.text_color = QPushButton(ButtonForm)
        self.horizontalLayout.addWidget(self.text_color)
        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.label_3 = QLabel(ButtonForm)
        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.command = QLineEdit(ButtonForm)
        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.command)

        self.label_5 = QLabel(ButtonForm)
        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.keys = QLineEdit(ButtonForm)
        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.keys)

        self.label_8 = QLabel(ButtonForm)
        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.switch_page = QSpinBox(ButtonForm)
        self.switch_page.setMinimum(0)
        self.switch_page.setMaximum(999999999)
        self.switch_page.setValue(0)
        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.switch_page)

        self.label_10 = QLabel(ButtonForm)
        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.switch_state = QSpinBox(ButtonForm)
        self.switch_state.setMaximum(999999999)
        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.switch_state)

        self.label_1 = QLabel(ButtonForm)
        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_1)

        self.globlstat = QCheckBox(ButtonForm)
        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.globlstat)

        self.exmpt = QPushButton(ButtonForm)
        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.exmpt)

        # FIXED BUTTON ROW
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.setexmpt = QPushButton(ButtonForm)
        self.setexmpt.setSizePolicy(sizePolicy5)
        self.setexmpt.setStyleSheet(u"padding: 2px 6px;")
        self.cancexmpt = QPushButton(ButtonForm)
        self.cancexmpt.setSizePolicy(sizePolicy5)
        self.cancexmpt.setStyleSheet(u"padding: 2px 6px;")
        self.setexmpt.setVisible(False)
        self.cancexmpt.setVisible(False)
        self.exmpt.setVisible(False)
        btn_row = QHBoxLayout()
        btn_row.addWidget(self.setexmpt)
        btn_row.addWidget(self.cancexmpt)
        self.formLayout.setLayout(11, QFormLayout.ItemRole.FieldRole, btn_row)

        self.label_7 = QLabel(ButtonForm)
        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.change_brightness = QSpinBox(ButtonForm)
        self.change_brightness.setMinimum(-99)
        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.change_brightness)

        self.label_6 = QLabel(ButtonForm)
        self.formLayout.setWidget(13, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.write = QPlainTextEdit(ButtonForm)
        self.formLayout.setWidget(13, QFormLayout.ItemRole.FieldRole, self.write)

        self.retranslateUi(ButtonForm)
        QMetaObject.connectSlotsByName(ButtonForm)

    def retranslateUi(self, ButtonForm):
        ButtonForm.setWindowTitle("Form")
        self.label.setText("Image:")
        self.add_image.setText("Image...")
        self.remove_image.setToolTip("Remove the image from the button")
        self.label_9.setText("Background")
        self.label_2.setText("Label:")
        self.text_v_align.setToolTip("Text vertical alignment")
        self.text_h_align.setToolTip("Text horizontal alignment")
        self.label_4.setText("Label Font:")
        self.text_color.setToolTip("Text Color")
        self.label_3.setText("Command:")
        self.label_5.setText("Press Keys:")
        self.label_8.setText("Switch Page:")
        self.label_10.setText("Switch state")
        self.label_1.setText("Global state")
        self.exmpt.setText("Exempt")
        self.setexmpt.setText("v")
        self.setexmpt.setToolTip("Confirm exempt selection")
        self.cancexmpt.setText("x")
        self.cancexmpt.setToolTip("Cancel exempt selection")
        self.label_7.setText("Brightness +/-:")
        self.label_6.setText("Write Text:")
