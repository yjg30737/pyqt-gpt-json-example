from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QPushButton, QGroupBox, QWidget, QSplitter, QVBoxLayout, QLabel, QTableWidget, \
    QTableWidgetItem, QComboBox, QHeaderView


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        try:
            pass
        except Exception as e:
            raise Exception(e)


class FormTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        # QTableWidget 설정
        self.setRowCount(5)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['Name', 'Type'])

        # 각 행에 텍스트와 QComboBox 추가
        for i in range(5):
            item = QTableWidgetItem()
            self.setItem(i, 0, item)

            comboBox = QComboBox()
            comboBox.addItems(["Integer", "String"])
            self.setCellWidget(i, 1, comboBox)

        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)

    def getData(self):
        data = [{"Name": self.item(i, 0).text(), "Type": self.cellWidget(i, 1).currentText() } for i in range(self.rowCount())]
        return data


class FormWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.__initUi()

    def __initUi(self):
        self.__formTableWidget = FormTableWidget()
        lay = QVBoxLayout()
        lay.addWidget(QLabel('Form Attributes'))
        lay.addWidget(self.__formTableWidget)

        settingsGrpBox = QGroupBox()
        settingsGrpBox.setTitle('Settings')
        settingsGrpBox.setLayout(lay)

        runBtn = QPushButton('Run')
        runBtn.clicked.connect(self.__run)

        lay = QVBoxLayout()
        lay.addWidget(settingsGrpBox)
        lay.addWidget(runBtn)

        leftWidget = QWidget()
        leftWidget.setLayout(lay)

        rightWidget = QWidget()

        saveBtn = QPushButton('Save')

        splitter = QSplitter()
        splitter.addWidget(leftWidget)
        splitter.addWidget(rightWidget)
        splitter.setHandleWidth(1)
        splitter.setChildrenCollapsible(False)
        splitter.setSizes([500, 500])
        splitter.setStyleSheet(
            "QSplitterHandle {background-color: lightgray;}")

        lay = QVBoxLayout()
        lay.addWidget(splitter)
        lay.addWidget(saveBtn)
        self.setLayout(lay)

    def __run(self):
        data = self.__formTableWidget.getData()
        self.__t = Thread()
        self.__t.started.connect(self.__started)
        self.__t.finished.connect(self.__finished)
        self.__t.start()

    def __started(self):
        print('started')

    def __finished(self):
        print('finished')