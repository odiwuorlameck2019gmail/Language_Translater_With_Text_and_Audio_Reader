from PyQt5.QtWidgets  import *
from  textblob import  TextBlob
import os
import sys
import pyttsx3

reader = pyttsx3.init()




class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.the_language_chosen=""
        self.final_text_file=""
        self.setWindowTitle("Translate from one Language to another :")
        grid_layout=QGridLayout()
        self.path_to_file=QLineEdit()
        self.path_to_file.setPlaceholderText("file_name.txt ")
        label=QLabel("Choose the Language that you want to translate to :")
        grid_layout.addWidget(self.path_to_file,10,13)
        grid_layout.addWidget(label,10,10)
        self.languages=QComboBox()
        self.languages.addItems(["English","French","Germany","Spanish","Chinese","Italian","Greek","Latin","Arabic"])
        self.languages.currentIndexChanged.connect(self.choose_language)
        button=QPushButton("Translate To a new Language")
        button.setStyleSheet("color:yellow")
        button.setStyleSheet("background-color:blue;color:yellow;border-radius:30px;")
        button.clicked.connect(self.translate)
        self.textarea=QPlainTextEdit()
        self.textarea.setReadOnly(False)
        self.textarea.setMinimumWidth(560)
        self.textarea.setMinimumHeight(300)
        self.textarea.setWordWrapMode(True)
        grid_layout.addWidget(self.textarea,12,10)
        grid_layout.addWidget(button,12,12)
        grid_layout.addWidget(self.languages,10,12)
        self.setStyleSheet("Background-color:yellow;font-size:30px;")
        self.setLayout(grid_layout)
    def translate(self):
                 try:
                    file_dir=str(self.path_to_file.text())
                    text_file_to_be_translated=open(file_dir,"r")
                    text_file=text_file_to_be_translated.read()
                    final_text_file=TextBlob(text_file)
                    text_file_to_be_translated.close()
                    final_text_translation=final_text_file.translate(to=self.the_language_chosen)
                    self.textarea.insertPlainText(str(final_text_translation))
                    #you are about to read the translation.
                    reader.say(final_text_translation)
                    reader.runAndWait()
                 except OSError as e:
                     alert=QMessageBox()
                     alert.setWindowTitle("Kindly enter the path to the text to be translated and ensure you connect to the internet")
                     alert.setText(" Error: ,"+str(e))
                     alert.exec_()
                
                 

    def choose_language(self):
            language_chosen=self.languages.currentText()
            if(language_chosen=="English"):
                self.the_language_chosen="en"
            elif(language_chosen=="French"):
                self.the_language_chosen="fr"
            elif(language_chosen=="Spanish"):
                self.the_language_chosen="es"
            elif(language_chosen=="Germany"):
                self.the_language_chosen="de"
            elif(language_chosen=="Chinese"):
                self.the_language_chosen="zh"
            elif(language_chosen=="Italian"):
                self.the_language_chosen="it"
            elif(language_chosen=="Greek"):
                self.the_language_chosen="el"
            elif(language_chosen=="Latin"):
                self.the_language_chosen="la"
            elif(language_chosen=="Arabic"):
                self.the_language_chosen="ar"
            
            



        

app=QApplication(sys.argv)
mainwindow=MainWindow()
mainwindow.show()
app.exec_()











