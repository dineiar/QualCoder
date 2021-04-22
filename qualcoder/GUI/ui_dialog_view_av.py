# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_view_av.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_view_av(object):
    def setupUi(self, Dialog_view_av):
        Dialog_view_av.setObjectName("Dialog_view_av")
        Dialog_view_av.resize(1021, 450)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_view_av)
        self.gridLayout.setObjectName("gridLayout")
        self.label_transcription = QtWidgets.QLabel(Dialog_view_av)
        self.label_transcription.setObjectName("label_transcription")
        self.gridLayout.addWidget(self.label_transcription, 4, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(Dialog_view_av)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 0, 0, 1, 1)
        self.label_speakers = QtWidgets.QLabel(Dialog_view_av)
        self.label_speakers.setMinimumSize(QtCore.QSize(0, 40))
        self.label_speakers.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_speakers.setObjectName("label_speakers")
        self.gridLayout.addWidget(self.label_speakers, 7, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog_view_av)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 9, 0, 1, 1)
        self.textEdit_transcription = QtWidgets.QTextEdit(Dialog_view_av)
        self.textEdit_transcription.setMinimumSize(QtCore.QSize(0, 40))
        self.textEdit_transcription.setMaximumSize(QtCore.QSize(16777215, 167700))
        self.textEdit_transcription.setTabChangesFocus(True)
        self.textEdit_transcription.setObjectName("textEdit_transcription")
        self.gridLayout.addWidget(self.textEdit_transcription, 5, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_view_av)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play.setGeometry(QtCore.QRect(10, 12, 36, 36))
        self.pushButton_play.setText("")
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalSlider_vol = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_vol.setGeometry(QtCore.QRect(590, 27, 160, 18))
        self.horizontalSlider_vol.setMaximum(100)
        self.horizontalSlider_vol.setProperty("value", 100)
        self.horizontalSlider_vol.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vol.setObjectName("horizontalSlider_vol")
        self.label_volume = QtWidgets.QLabel(self.groupBox_2)
        self.label_volume.setGeometry(QtCore.QRect(540, 16, 32, 32))
        self.label_volume.setText("")
        self.label_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_volume.setObjectName("label_volume")
        self.label_time = QtWidgets.QLabel(self.groupBox_2)
        self.label_time.setGeometry(QtCore.QRect(220, 22, 171, 21))
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")
        self.comboBox_tracks = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_tracks.setGeometry(QtCore.QRect(830, 20, 61, 28))
        self.comboBox_tracks.setObjectName("comboBox_tracks")
        self.label_audio = QtWidgets.QLabel(self.groupBox_2)
        self.label_audio.setGeometry(QtCore.QRect(760, 23, 61, 20))
        self.label_audio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_audio.setObjectName("label_audio")
        self.checkBox_scroll_transcript = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_scroll_transcript.setGeometry(QtCore.QRect(10, 50, 511, 22))
        self.checkBox_scroll_transcript.setObjectName("checkBox_scroll_transcript")
        self.label_rate = QtWidgets.QLabel(self.groupBox_2)
        self.label_rate.setGeometry(QtCore.QRect(448, 23, 41, 20))
        self.label_rate.setObjectName("label_rate")
        self.label_time_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_time_3.setGeometry(QtCore.QRect(180, 17, 32, 32))
        self.label_time_3.setText("")
        self.label_time_3.setObjectName("label_time_3")
        self.pushButton_rate_down = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_rate_down.setGeometry(QtCore.QRect(408, 12, 36, 36))
        self.pushButton_rate_down.setText("")
        self.pushButton_rate_down.setObjectName("pushButton_rate_down")
        self.pushButton_rate_up = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_rate_up.setGeometry(QtCore.QRect(490, 12, 36, 36))
        self.pushButton_rate_up.setText("")
        self.pushButton_rate_up.setObjectName("pushButton_rate_up")
        self.pushButton_rewind_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_rewind_5.setGeometry(QtCore.QRect(50, 12, 36, 36))
        self.pushButton_rewind_5.setText("")
        self.pushButton_rewind_5.setObjectName("pushButton_rewind_5")
        self.pushButton_rewind_30 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_rewind_30.setGeometry(QtCore.QRect(90, 12, 36, 36))
        self.pushButton_rewind_30.setText("")
        self.pushButton_rewind_30.setObjectName("pushButton_rewind_30")
        self.pushButton_forward_30 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_forward_30.setGeometry(QtCore.QRect(130, 12, 36, 36))
        self.pushButton_forward_30.setText("")
        self.pushButton_forward_30.setObjectName("pushButton_forward_30")
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.label_memo = QtWidgets.QLabel(Dialog_view_av)
        self.label_memo.setObjectName("label_memo")
        self.gridLayout.addWidget(self.label_memo, 8, 0, 1, 1)
        self.groupBox_search_text = QtWidgets.QGroupBox(Dialog_view_av)
        self.groupBox_search_text.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_search_text.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox_search_text.setTitle("")
        self.groupBox_search_text.setObjectName("groupBox_search_text")
        self.lineEdit_search = QtWidgets.QLineEdit(self.groupBox_search_text)
        self.lineEdit_search.setGeometry(QtCore.QRect(40, 5, 191, 32))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox_search_text)
        self.pushButton_next.setGeometry(QtCore.QRect(280, 3, 36, 36))
        self.pushButton_next.setText("")
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_search_regex = QtWidgets.QLabel(self.groupBox_search_text)
        self.label_search_regex.setGeometry(QtCore.QRect(0, 5, 34, 34))
        self.label_search_regex.setAutoFillBackground(False)
        self.label_search_regex.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search_regex.setText("")
        self.label_search_regex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_search_regex.setWordWrap(True)
        self.label_search_regex.setObjectName("label_search_regex")
        self.pushButton_previous = QtWidgets.QPushButton(self.groupBox_search_text)
        self.pushButton_previous.setGeometry(QtCore.QRect(240, 3, 36, 36))
        self.pushButton_previous.setText("")
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.label_search_totals = QtWidgets.QLabel(self.groupBox_search_text)
        self.label_search_totals.setGeometry(QtCore.QRect(320, 7, 81, 22))
        self.label_search_totals.setAlignment(QtCore.Qt.AlignCenter)
        self.label_search_totals.setObjectName("label_search_totals")
        self.gridLayout.addWidget(self.groupBox_search_text, 6, 0, 1, 1)

        self.retranslateUi(Dialog_view_av)
        QtCore.QMetaObject.connectSlotsByName(Dialog_view_av)
        Dialog_view_av.setTabOrder(self.pushButton_play, self.horizontalSlider_vol)
        Dialog_view_av.setTabOrder(self.horizontalSlider_vol, self.comboBox_tracks)
        Dialog_view_av.setTabOrder(self.comboBox_tracks, self.checkBox_scroll_transcript)
        Dialog_view_av.setTabOrder(self.checkBox_scroll_transcript, self.textEdit_transcription)
        Dialog_view_av.setTabOrder(self.textEdit_transcription, self.horizontalSlider)
        Dialog_view_av.setTabOrder(self.horizontalSlider, self.textEdit)

    def retranslateUi(self, Dialog_view_av):
        _translate = QtCore.QCoreApplication.translate
        Dialog_view_av.setWindowTitle(_translate("Dialog_view_av", "View Audio Video"))
        self.label_transcription.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p><br/></p></body></html>"))
        self.label_transcription.setText(_translate("Dialog_view_av", "Transcription:"))
        self.horizontalSlider.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Left click on the slider button and drag left or right to change audio/video position.</p></body></html>"))
        self.label_speakers.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Add a speaker name to shortcuts. In the text entry box press ctrl + n</p><p>Insert a speaker into transcription. In the text entry box press ctrl + 1 up to ctrl + 8 for the speakers name.</p></body></html>"))
        self.label_speakers.setText(_translate("Dialog_view_av", "Speakers:"))
        self.textEdit.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Memo</p></body></html>"))
        self.pushButton_play.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Play / Pause</p><p>Ctrl + S start/pause</p><p>Ctrl + P start/pause</p></body></html>"))
        self.label_volume.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Volume</p></body></html>"))
        self.label_audio.setText(_translate("Dialog_view_av", "Audio:"))
        self.checkBox_scroll_transcript.setText(_translate("Dialog_view_av", "Scroll transcript while playing. (Transcript is read only)"))
        self.label_rate.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Ctrl + Shift + &gt; increase play rate, maximum 2.0</p><p>Ctrl + Shift + &lt; decrease play rate, minimum 0.1</p></body></html>"))
        self.label_rate.setText(_translate("Dialog_view_av", "1.0x"))
        self.label_time_3.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Time</p></body></html>"))
        self.pushButton_rate_down.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Decrease play rate</p><p>Ctrl + Shift + &lt; </p></body></html>"))
        self.pushButton_rate_up.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Increase play rate</p><p>Ctrl + Shift + &gt; </p></body></html>"))
        self.pushButton_rewind_5.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Rewind 5 seconds</p><p>Ctrl + R</p></body></html>"))
        self.pushButton_rewind_30.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Rewind 30 seconds</p><p>Alt + R</p></body></html>"))
        self.pushButton_forward_30.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Forward 30 seconds</p><p>Alt + F</p></body></html>"))
        self.label_memo.setText(_translate("Dialog_view_av", "Memo:"))
        self.lineEdit_search.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Search for text.</p></body></html>"))
        self.pushButton_next.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Next</p></body></html>"))
        self.label_search_regex.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Search uses Regex functions. </p><p>A dot ‘.’ is used as a wild card, e.g. ‘.ears’ will match ‘bears’ and ‘years’. </p><p>A ‘?’ after a character will match one or none times that character, e.g. ‘bears?’ will match ‘bear’ and ‘bears’ </p><p><span style=\" background-color:transparent;\">A ‘*’ after a character will match zero or more times. </span></p><p><span style=\" background-color:transparent;\">‘</span>\\. will match the dot symbol, ‘\\?’ will match the question mark. ‘\\n’ will match the line ending symbol. </p><p>Regex cheatsheet: <a href=\"http://www.rexegg.com/regex-quickstart.html\"><span style=\" text-decoration: underline; color:#000080;\">www.rexegg.com/regex-quickstart.html</span></a></p></body></html>"))
        self.pushButton_previous.setToolTip(_translate("Dialog_view_av", "<html><head/><body><p>Previous</p></body></html>"))
        self.label_search_totals.setText(_translate("Dialog_view_av", "0 / 0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_view_av = QtWidgets.QDialog()
    ui = Ui_Dialog_view_av()
    ui.setupUi(Dialog_view_av)
    Dialog_view_av.show()
    sys.exit(app.exec_())
