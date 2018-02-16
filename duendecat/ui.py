from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from shared.ui import MySpinBox, clickable
from shared import r
from duendecat import config

class Layout(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mOptions = QComboBox()
        self.mLevelChooser = MySpinBox()
        self.mSubmit = QPushButton('Generate')

        top = QHBoxLayout()
        top.addWidget(self.mOptions, stretch=2)
        top.addWidget(self.mLevelChooser, stretch=1)
        top.addWidget(self.mSubmit, stretch=1)

        self.mQuiz = QLabel()
        font = QFont()
        font.setPointSize(24)
        self.mQuiz.setFont(font)
        self.mAnswer = QLabel()

        self.addLayout(top)
        self.addWidget(self.mQuiz)
        self.addWidget(self.mAnswer)

        self._init()

    def _init(self):
        conf = config.read()
        lv = r.Level()
        sentences = r.Sentences()

        self.mOptions.addItems(lv.level_labels)
        self.mOptions.setCurrentText(lv.level2label(conf['level'])['full name'])

        self.mLevelChooser.setPrefix("Level ")
        self.mLevelChooser.setRange(1, 100)
        self.mLevelChooser.setValue(conf['level'])
        self.mLevelChooser.lineEdit().setReadOnly(True)

        randSentence = sentences.getRandRow(conf['level'])
        self.mQuiz.setText(randSentence[2])

        answer = randSentence[1] + '<br />' + randSentence[0]
        self.mAnswer.setText(answer)

        self._setControl()

    def _setControl(self):
        self.mOptions.currentIndexChanged[str].connect(self.labelChanged)
        self.mLevelChooser.valueChanged.connect(self.levelChanged)
        self.mLevelChooser.keyPressed.connect(self.keyPress)
        self.mSubmit.clicked.connect(self.onSubmit)
        clickable(self.mAnswer).connect(self.showAnswer)

    def labelChanged(self, option):
        lv = r.Level()
        for label in lv.getLabels():
            if label['full name'] == option:
                self.mLevelChooser.setValue(label['levels'][0])

    def levelChanged(self, level):
        sentences = r.Sentences()
        randSentence = sentences.getRandRow(level)
        self.mQuiz.setText(randSentence[2])

        answer = randSentence[1] + '<br />' + randSentence[0]
        self.mAnswer.setText(answer)

    def keyPress(self):
        pass

    def onSubmit(self):
        self.updateUI()

    def showAnswer(self):
        pass

    def updateUI(self):
        pass
