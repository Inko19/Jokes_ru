import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
from parsing import Parsing as pars

class Logic(QMainWindow):
	def __init__(self):
		super(Logic, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton_10.clicked.connect(lambda: self.parse_Putin())
		self.ui.pushButton_8.clicked.connect(lambda: self.parse_Obama())
		self.ui.pushButton_7.clicked.connect(lambda: self.parse_Ukrain())
		self.ui.pushButton_5.clicked.connect(lambda: self.parse_Pensioners())
		self.ui.pushButton_6.clicked.connect(lambda: self.parse_Fishing())
		self.ui.pushButton_2.clicked.connect(lambda: self.parse_Politics())
		self.ui.pushButton_4.clicked.connect(lambda: self.parse_Stirlitz())
		self.ui.pushButton_3.clicked.connect(lambda: self.parse_Chukchi())
		self.ui.pushButton_9.clicked.connect(lambda: self.parse_Junkies())

	def parse_Putin(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Putin_jokes_parsing()))
	def parse_Obama(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Obama_jokes_parsing()))
	def parse_Ukrain(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Ukrain_jokes_parsing()))
	def parse_Pensioners(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Pensioners_jokes_parsing()))
	def parse_Fishing(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Fishing_jokes_parsing()))
	def parse_Politics(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Politics_jokes_parsing()))
	def parse_Stirlitz(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Stirlitz_jokes_parsing()))
	def parse_Chukchi(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Chukchi_jokes_parsing()))
	def parse_Junkies(self):
		self.ui.plainTextEdit.setPlainText(str(pars.Junkies_jokes_parsing()))	






if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Logic()
	window.show()
	sys.exit(app.exec())

