import sys, os
from PyQt5.QtWidgets import *

from resources import r

MENU = {
    'pref': 'Preferences',
    'mainPage': 'Back to main page'
}


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('WaniKani for Chinese')

        self.lv = r.Level()

    def showUI(self):
        menubar = self.menuBar()

        menuSettings = menubar.addMenu('&Settings')
        submenuPref = QAction(MENU['pref'], self)
        menuSettings.addAction(submenuPref)
        menuSettings.triggered[QAction].connect(self.actionGeneral)

        menuFile = menubar.addMenu('&File')
        submenuMainPage = QAction(MENU['mainPage'], self)
        menuFile.addAction(submenuMainPage)
        menuFile.triggered[QAction].connect(self.actionGeneral)

        menuLevels = menubar.addMenu('&Levels')
        self._menuAddLevels(menuLevels, self.actionGenLevel)

        menuRadicals = menubar.addMenu('&Radicals')
        self._menuAddLevels(menuRadicals, self.actionRadicals)
        menuRadicals.addSeparator()
        self._menuAddLattice(menuRadicals, ('Name', 'Progress'), self.actionRadicals)

        menuKanji = menubar.addMenu('&Kanji')
        self._menuAddLevels(menuKanji, self.actionKanji)
        menuKanji.addSeparator()
        self._menuAddLattice(menuKanji, ('Combined', 'Meaning', 'Reading', 'Progress'),
                             self.actionKanji)

        menuVocab = menubar.addMenu('&Vocabularies')
        self._menuAddLevels(menuVocab, self.actionVocab)
        menuVocab.addSeparator()
        self._menuAddLattice(menuVocab, ('Combined', 'Meaning', 'Reading', 'Progress'),
                             self.actionVocab)

        resolution = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, resolution.width(), resolution.height())

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.show()

    def actionGeneral(self, qaction):
        text = qaction.text()
        print('General', text)
        # if text == MENU['pref']:
        #     layout = preferences.Layout()
        # elif text == MENU['doctorWork']:
        #     layout = personnel.doctorWork.Layout()
        # elif text == MENU['nurseWork']:
        #     layout = personnel.nurseWork.Layout()
        # elif text == MENU['logout']:
        #     login.main()
        #     self.close()
        #     return
        # elif text == MENU['doctorLog']:
        #     layout = personnel.doctorLog.Layout()
        # elif text == MENU['wardLog']:
        #     layout = personnel.wardLog.Layout()
        # elif text == MENU['emr']:
        #     layout = patient.emr.Layout()
        #
        # sub = common.SubWindow()
        # sub.setWindowTitle(text)
        # sub.overall = layout
        # sub.param = self.param
        # self.mdi.addSubWindow(sub)
        # sub.showUI()

    def actionGenLevel(self, qaction):
        text = qaction.text()
        print('Total level:', text)

    def actionRadicals(self, qaction):
        text = qaction.text()
        print('Radicals:', text)

    def actionKanji(self, qaction):
        text = qaction.text()
        print('Kanji:', text)

    def actionVocab(self, qaction):
        text = qaction.text()
        print('Vocab:', text)

    def createMenu(self, wordList, menu, action):
        for text in wordList:
            if text == 'sep':
                menu.addSeparator()
            else:
                menu.addAction(QAction(text, self))
        menu.triggered[QAction].connect(action)

    def _menuAddLevels(self, menu, func):
        for level_label in self.lv.getLabels():
            submenuLabel = QMenu(level_label['full name'], self)
            menu.addMenu(submenuLabel)

            for level_number in level_label['levels']:
                action = QAction('Level {}'.format(level_number), self)
                submenuLabel.addAction(action)

            submenuLabel.triggered[QAction].connect(func)

    def _menuAddLattice(self, menu, name_list, func):
        submenuLattice = QMenu('Lattice', self)
        for name in name_list:
            action = QAction(name, self)
            submenuLattice.addAction(action)

        submenuLattice.triggered[QAction].connect(func)
        menu.addMenu(submenuLattice)


if __name__ == '__main__':
    os.chdir('..')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showUI()
    sys.exit(app.exec_())
