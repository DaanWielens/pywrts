# pywrts
pywrts is a GUI-based Python application with which one can learn words or phrases. The application reads a user-provided words list and selects random words from the list which need to be translated by the user. While the user works through the list, correct translated words/phrases will be removed from the 'to-translate' list, while incorrect attempts will not remove the word/phrase. Hence, the user will need to attempt to translate these words/phrases until all translations are correct. 

A screenshot of the GUI can be found below:<br>
![GUI of the program](https://raw.githubusercontent.com/DaanWielens/pywrts/main/pywrts_gui.png)

The dictionary file is a plain-text file (utf-8 encoded). An example is [dutch_english_sample.pywrts](https://github.com/DaanWielens/pywrts/blob/main/dutch_english_sample.pywrts). The file can be edited in any text editor, but the extension must remain .pywrts.

#### Ultra-short manual
- Run the script (i.e. through Spyder)
- Click the __folder__ icon to browse for a dictionary file
- The program will now ask for words to translate. Type the translation in the big text box and hit [Return] to submit the translation. For special characters that might not appear on a standard US-International keyboard, extra buttons have been added. 
