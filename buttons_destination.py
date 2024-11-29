from Main_Window import Ui_MainWindow
from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import *



class MyLocationBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Forgotten Islands")

        self.current_songs = []
        self.current_volume = 50

        self.current_sounds = []
        self.current_volume_sounds = 35

        global stopped
        stopped = False

        self.player = QtMultimedia.QMediaPlayer()
        self.player.setVolume(self.current_volume)

        self.player_sounds = QtMultimedia.QMediaPlayer()
        self.player_sounds.setVolume(self.current_volume_sounds)


        self.widget.setHidden(True)
        self.Btn_Music_play.setHidden(True)
        self.btn_Sound_play.setHidden(True)
        self.Btn_Music_play_clothed.setHidden(True)
        self.btn_Sound_play_clothed.setHidden(True)


        self.Btn_Full_Map.clicked.connect(self.swich_to_Full_Map_Page)

        self.Btn_City.clicked.connect(self.swich_to_City_Page)
        self.Btn_Suburb.clicked.connect(self.swich_to_Suburb_Page)
        self.Btn_Forest.clicked.connect(self.swich_to_Forest_Page)
        self.Btn_Mountains.clicked.connect(self.swich_to_Mountains_Page)
        self.Btn_Village.clicked.connect(self.swich_to_Village_Page)

        self.Btn_City_Tavern.clicked.connect(self.swich_to_City_Tavern_Page)
        self.Btn_Castle.clicked.connect(self.swich_to_Castle_Coridor_Page)
        self.Btn_Port.clicked.connect(self.swich_to_Human_Port_Page)
        self.Btn_Fishman_Port.clicked.connect(self.swich_to_Human_Port_Page)
        self.Btn_Slums.clicked.connect(self.swich_to_Boss_House_Page)

        self.Btn_Suburb_Tavern.clicked.connect(self.swich_to_Suburb_Tavern_Road_Page)

        self.Btn_Back_City.clicked.connect(self.swich_to_City_Page)

        self.Btn_Go_to_City.clicked.connect(self.swich_to_City_Page)
        self.Btn_Go_to_Throne.clicked.connect(self.swich_to_Castle_Throne_room_Page)
        self.Btn_Go_to_Corridor.clicked.connect(self.swich_to_Castle_Coridor_Page)

        self.Btn_Back_City_from_Port.clicked.connect(self.swich_to_City_Page)
        self.Btn_Go_to_Storage.clicked.connect(self.swich_to_Human_Port_Storage_Page)

        self.Btn_Go_to_Port.clicked.connect(self.swich_to_Human_Port_Page)
        self.Btn_from_Storage_to_City.clicked.connect(self.swich_to_City_Page)
        self.Btn_Go_inside_Storage.clicked.connect(self.swich_to_Human_Port_inside_Storage_Page)

        self.Btn_Go_out_Storage.clicked.connect(self.swich_to_Human_Port_Storage_Page)

        self.Btn_Go_City_from_Boss.clicked.connect(self.swich_to_City_Page)
        self.Btn_Go_to_Boss.clicked.connect(self.swich_to_Boss_inside_House_Page)

        self.Btn_Go_from_Boss_to_City.clicked.connect(self.swich_to_Boss_House_Page)

        self.Btn_Back_suburb.clicked.connect(self.swich_to_Suburb_Page)

        self.Btn_Music_play.clicked.connect(self.play_music)
        self.btn_Music_Pause.clicked.connect(self.pause_music)
        self.Btn_Music_play_clothed.clicked.connect(self.play_music)
        self.btn_Music_Pause_clothed.clicked.connect(self.pause_music)
        self.horizontalSlider_2.sliderMoved[int].connect(lambda: self.volume_music_changed())

        self.btn_Sound_play.clicked.connect(self.play_music)
        self.btn_Sound_Pause.clicked.connect(self.pause_music)
        self.btn_Sound_play_clothed.clicked.connect(self.play_music)
        self.btn_Sound_Pause_clothed.clicked.connect(self.pause_music)
        self.horizontalSlider.sliderMoved[int].connect(lambda: self.volume_sounds_changed())

        self.url = QtCore.QUrl.fromLocalFile('Port.flac')
        self.content = QtMultimedia.QMediaContent(self.url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)




    def swich_to_Full_Map_Page(self):
        self.stackedWidget_3.setCurrentIndex(0)

        try:
            self.text_Description.setText('')
            with open('Full_Map_Description.txt', "r") as File:
                self.text_Description.setText(File.read())
                # text = ui.textEdit.toPlainText()
                # File.write(text)

        except FileNotFoundError:
            print('No such Description file')

        try:
            self.text_Encounters.setText('')
            with open('Full_Map_Encounters.txt', "r") as File:
                self.text_Encounters.setText(File.read())
                # text = ui.textEdit.toPlainText()
                # File.write(text)

        except FileNotFoundError:
            print('No such Encounters file')

        self.url = QtCore.QUrl('file:///C:/Users/kelar/OneDrive/Рабочий стол/D&D/DnD Game/full_project'
                               '/music/Full_map.flac')
        self.content = QtMultimedia.QMediaContent(self.url)

        content = QMediaContent(QUrl.fromLocalFile('Port.flac'))
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setVolume(self.current_volume)
        self.player.setMedia(content)
        self.player.play()



    def swich_to_City_Page(self):
        self.stackedWidget_3.setCurrentIndex(1)

        try:
            self.text_Description.setText('')
            with open('City_Description.txt', "r") as File:
                self.text_Description.setText(File.read())
                # text = ui.textEdit.toPlainText()
                # File.write(text)

        except FileNotFoundError:
            print('No such Description file')

        try:
            self.text_Encounters.setText('')
            with open('City_Encounters.txt', "r") as File:
                self.text_Encounters.setText(File.read())
                # text = ui.textEdit.toPlainText()
                # File.write(text)

        except FileNotFoundError:
            print('No such Encounters file')

        try:
            global stopped
            stopped = False

            content = QMediaContent(QUrl('file:///C:/Users/kelar/OneDrive/Рабочий стол/D&D/DnD Game/full_project'
                                         '/music/City.flac'))
            self.player.setMedia(content)
            self.player.play()
        except Exception as e:
            print(f"Play song error: {e}")


    def swich_to_Suburb_Page(self):
        self.stackedWidget_3.setCurrentIndex(2)

        self.text_Encounters.setText('')
        self.text_Description.setText('')

    def swich_to_Forest_Page(self):
        self.stackedWidget_3.setCurrentIndex(3)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Mountains_Page(self):
        self.stackedWidget_3.setCurrentIndex(4)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Village_Page(self):
        self.stackedWidget_3.setCurrentIndex(5)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_City_Tavern_Page(self):
        self.stackedWidget_3.setCurrentIndex(6)

        try:
            self.text_Description.setText('')
            with open('City_Tavern_Description.txt', "r") as File:
                self.text_Description.setText(File.read())
                # text = ui.textEdit.toPlainText()
                # File.write(text)

        except FileNotFoundError:
            print('No such Description file')

        try:
            self.text_Encounters.setText('')
            with open('City_Tavern_Encounters.txt', "r") as File:
                self.text_Encounters.setText(File.read())
                # text = ui.textEdit.toPlainText()
                # File.write(text)

        except FileNotFoundError:
            print('No such Encounters file')



    def swich_to_Castle_Coridor_Page(self):
        self.stackedWidget_3.setCurrentIndex(7)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Castle_Throne_room_Page(self):
        self.stackedWidget_3.setCurrentIndex(8)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Human_Port_Page(self):
        self.stackedWidget_3.setCurrentIndex(9)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Human_Port_Storage_Page(self):
        self.stackedWidget_3.setCurrentIndex(10)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Human_Port_inside_Storage_Page(self):
        self.stackedWidget_3.setCurrentIndex(11)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Boss_House_Page(self):
        self.stackedWidget_3.setCurrentIndex(12)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Boss_inside_House_Page(self):
        self.stackedWidget_3.setCurrentIndex(13)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Suburb_Tavern_Road_Page(self):
        self.stackedWidget_3.setCurrentIndex(14)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def swich_to_Suburb_Tavern_inside_Page(self):
        self.stackedWidget_3.setCurrentIndex(15)

        self.text_Encounters.setText('')
        self.text_Description.setText('')


    def volume_music_changed(self):
        try:
            self.current_volume = self.horizontalSlider_2.value()
            self.player.setVolume(self.current_volume)
        except Exception as e:
            print(f"Changing volume error: {e}")

    def volume_sounds_changed(self):
        try:
            self.current_volume_sounds = self.horizontalSlider.value()
            self.player_sounds.setVolume(self.current_volume_sounds)
        except Exception as e:
            print(f"Changing volume error: {e}")

    def play_music(self):
        self.player.play()

    def pause_music(self):
        self.player.pause()


