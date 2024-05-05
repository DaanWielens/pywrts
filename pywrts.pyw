# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:41:04 2024

@author: Daan Wielens
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import os
import numpy as np

# Change working directory to this file's path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Main window
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle('pyWRTS v0.1 (2024-05-05)')
        self.setFixedWidth(600)
    
    # --- Define layout --- 
        # Main layout: vertical structure
        layMain = QVBoxLayout()
        
        # File selection / toolbar
        layToolsGroup = QGroupBox()
        layTools = QHBoxLayout()
        
        self.select_file_btn = QPushButton('', self)
        self.select_file_btn.setIcon(QIcon('open_file.png'))
        self.select_file_btn.setIconSize(QSize(16, 16))
        self.select_file_btn.clicked.connect(self.load_file)
        self.select_file_btn.setToolTip('Refresh plot according to the Data selector.')
        layTools.addWidget(self.select_file_btn)
        
        self.file_path_box = QLineEdit('', self)
        self.file_path_box.setToolTip('File path of the dictionary file.')
        self.file_path_box.returnPressed.connect(self.load_data_box)
        layTools.addWidget(self.file_path_box)
        
        layToolsGroup.setLayout(layTools)
        layMain.addWidget(layToolsGroup)

        # Game window        
        self.layGameGroup = QGroupBox('Translate the given word or phrase')
        layGame = QVBoxLayout()
        self.layGameGroup.setLayout(layGame)
        
        self.word_in_lbl = QLabel()
        self.word_in_lbl.setText('Input word')
        self.word_in_lbl.setFixedWidth(560)
        self.word_in_lbl.setAlignment(Qt.AlignCenter)
        self.word_in_lbl.setFont(QFont('Arial', 20))
        layGame.addWidget(self.word_in_lbl)
        
        self.word_out_box = QLineEdit('', self)
        self.word_out_box.setToolTip('Enter your translation here.')
        self.word_out_box.setFont(QFont('Arial', 20))
        self.word_out_box.returnPressed.connect(self.check_answer)
        layGame.addWidget(self.word_out_box)
        
        self.answer_lbl = QLabel()
        self.answer_lbl.setText(' ')
        self.answer_lbl.setFixedWidth(560)
        self.answer_lbl.setAlignment(Qt.AlignCenter)
        self.answer_lbl.setFont(QFont('Arial', 16))
        layGame.addWidget(self.answer_lbl)
        
        layMain.addWidget(self.layGameGroup)
        
        # Special characters
        layCharGroup = QGroupBox('Special characters')
        layChar = QHBoxLayout()
        layChar.setAlignment(Qt.AlignLeft)
        layCharGroup.setLayout(layChar)
        
        hard_c_btn = QPushButton('č', self)
        hard_c_btn.clicked.connect(self.add_hard_c)
        hard_c_btn.setToolTip('Hard c')
        hard_c_btn.setFont(QFont('Arial', 14))
        hard_c_btn.setFixedWidth(24)
        layChar.addWidget(hard_c_btn)
        
        soft_c_btn = QPushButton('ć', self)
        soft_c_btn.clicked.connect(self.add_soft_c)
        soft_c_btn.setToolTip('Soft c')
        soft_c_btn.setFont(QFont('Arial', 14))
        soft_c_btn.setFixedWidth(24)
        layChar.addWidget(soft_c_btn)
        
        hard_z_btn = QPushButton('ž', self)
        hard_z_btn.clicked.connect(self.add_hard_z)
        hard_z_btn.setToolTip('Hard z')
        hard_z_btn.setFont(QFont('Arial', 14))
        hard_z_btn.setFixedWidth(24)
        layChar.addWidget(hard_z_btn)
        
        meko_d_btn = QPushButton('đ', self)
        meko_d_btn.clicked.connect(self.add_meko_d)
        meko_d_btn.setToolTip('Meko d')
        meko_d_btn.setFont(QFont('Arial', 14))
        meko_d_btn.setFixedWidth(24)
        layChar.addWidget(meko_d_btn)
        
        hard_s_btn = QPushButton('š', self)
        hard_s_btn.clicked.connect(self.add_hard_s)
        hard_s_btn.setToolTip('Hard s')
        hard_s_btn.setFont(QFont('Arial', 14))
        hard_s_btn.setFixedWidth(24)
        layChar.addWidget(hard_s_btn)

        ringel_s_btn = QPushButton('ß', self)
        ringel_s_btn.clicked.connect(self.add_ringel_s)
        ringel_s_btn.setToolTip('Scharfes s')
        ringel_s_btn.setFont(QFont('Arial', 14))
        ringel_s_btn.setFixedWidth(24)
        layChar.addWidget(ringel_s_btn)    
        
        enye_btn = QPushButton('ñ', self)
        enye_btn.clicked.connect(self.add_enye)
        enye_btn.setToolTip('Enye')
        enye_btn.setFont(QFont('Arial', 14))
        enye_btn.setFixedWidth(24)
        layChar.addWidget(enye_btn) 
        
        layMain.addWidget(layCharGroup)
        
        # Progress
        layProgressGroup = QGroupBox('Progress')
        layProgress = QHBoxLayout()
        layProgressGroup.setLayout(layProgress)
        
        self.count_lbl = QLabel('', self)
        layProgress.addWidget(self.count_lbl)
        
        layMain.addWidget(layProgressGroup)
        
        # Final layout
        widget = QWidget()
        widget.setLayout(layMain)
        self.setCentralWidget(widget)
    
    # --- Add signals and slots
    def dummy(self):
        print('Triggered.')
        
    def add_hard_c(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'č')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))

    def add_soft_c(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'ć')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))

    def add_hard_z(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'ž')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))

    def add_meko_d(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'đ')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))
        
    def add_hard_s(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'š')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))

    def add_ringel_s(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'ß')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))

    def add_enye(self):
        txt = self.word_out_box.text()
        self.word_out_box.setText(txt + 'ñ')
        self.word_out_box.setFocus(Qt.MouseFocusReason)
        self.word_out_box.setCursorPosition(len(self.word_out_box.text()))        
        
    def check_answer(self):
        txt_user = self.word_out_box.text()
        if txt_user != self.word_list[self.word_list_not_answered_correctly[self.word_index]][1]:
            self.answer_lbl.setText('Wrong! Correct answer: ' + self.word_list[self.word_list_not_answered_correctly[self.word_index]][1])
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.red)
            self.answer_lbl.setGraphicsEffect(color_effect)
            self.n_mistakes += 1
        else:
            self.answer_lbl.setText('Correct!')
            color_effect = QGraphicsColorizeEffect()
            color_effect.setColor(Qt.darkGreen)
            self.answer_lbl.setGraphicsEffect(color_effect)
            # Remove the correct answer's index from the list of wrong answers
            elements_to_remove = self.word_list_not_answered_correctly[self.word_index]  
            self.word_list_not_answered_correctly = self.word_list_not_answered_correctly[~np.isin(self.word_list_not_answered_correctly, elements_to_remove)]
            # Add to the list of correct answers
            self.word_list_answered_correctly.append(self.word_index)
        self.new_word()
            
    def load_file(self):
        options = QFileDialog.Options()
        fileName = QFileDialog.getOpenFileName(self, 'Open a pywrts file', filter='pyWRTS files (*.pywrts)')
        if fileName:
            self.load_data(file=fileName[0])
            
    def load_data_box(self):
        file = self.file_path_box.text()
        self.load_data(file)
            
    def load_data(self, file):
        self.file_path_box.setText(file)
        self.word_list = []
        self.word_list_answered_correctly = []
        self.n_mistakes = 0
        with open(file, 'r', encoding='utf-8') as file:
            for line in file:
                if '% language' in line:
                    self.lang1 = line.split(':')[1].split(' - ')[0]
                    self.lang2 = line.split(':')[1].split(' - ')[1]
                if '|' in line:
                    word1 = line.split(' | ')[0]
                    word2 = line.split(' | ')[1].strip('\r').strip('\n')
                    self.word_list.append([word1, word2])
                    
        self.count_lbl.setText('Translated correctly: ' + str(len(self.word_list_answered_correctly)) + '/' + str(len(self.word_list)) + '      | Number of mistakes: ' + str(self.n_mistakes))
        self.word_list_not_answered_correctly = np.arange(len(self.word_list))
        
        self.layGameGroup.setTitle('Translate the given word or phrase: ' + self.lang1 + ' → ' + self.lang2)
        # Start with first word
        self.new_word()
        
    def new_word(self):
        self.word_out_box.setText('')
        if len(self.word_list_not_answered_correctly) > 0:
            self.word_index = int(np.round(np.random.rand() * len(self.word_list_not_answered_correctly)) - 1)
            if self.word_index < 0:
                self.word_index = 0
            self.word_in_lbl.setText(self.word_list[self.word_list_not_answered_correctly[self.word_index]][0])
            self.count_lbl.setText('Translated correctly: ' + str(len(self.word_list_answered_correctly)) + '/' + str(len(self.word_list)) + '      | Number of mistakes: ' + str(self.n_mistakes))
        else:
            self.word_in_lbl.setText('The game is finished. Well done!')
            self.count_lbl.setText('Translated correctly: ' + str(len(self.word_list_answered_correctly)) + '/' + str(len(self.word_list)) + '      | Number of mistakes: ' + str(self.n_mistakes))
        
   
    # Fix to make PyQt5 close correctly in Spyder    
    def closeEvent(self,event):
        QApplication.quit()       

# Run main code
app = QApplication.instance()
window = MainWindow()
window.show()
app.exec_()