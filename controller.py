from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    class that rus the tv controller
    """
    # class variables - constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

        self.setupUi(self)
        self.button_0Disney.setIcon(QtGui.QIcon('disney.jpg'))
        self.button_0Disney.setIconSize(QtCore.QSize(50, 150))
        self.button_1Hulu.setIcon(QtGui.QIcon('hulu.jpg'))
        self.button_1Hulu.setIconSize(QtCore.QSize(50, 150))
        self.button_3Netflix.setIcon(QtGui.QIcon('netflix.png'))
        self.button_3Netflix.setIconSize(QtCore.QSize(50, 150))
        self.button_4Crunchy.setIcon(QtGui.QIcon('Crunchyroll.jpg'))
        self.button_4Crunchy.setIconSize(QtCore.QSize(50, 150))

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_volumeUp.clicked.connect(lambda: self.volume_up())
        self.button_volumeDown.clicked.connect(lambda: self.volume_down())
        self.button_channelDown.clicked.connect(lambda: self.channel_down())

        self.button_channelUp.clicked.connect(lambda: self.channel_up())
        self.button_0Disney.clicked.connect(lambda: self.button_0())
        self.button_1Hulu.clicked.connect(lambda: self.button_1())
        self.button_3Netflix.clicked.connect(lambda: self.button_2())
        self.button_4Crunchy.clicked.connect(lambda: self.button_3())

    def power(self):
        """
        Method to turn TV on and off
        :return: True or False to self.__status
        """
        if self.__status:
            self.__status = False
            self.button_volumeUp.setDisabled(False)
            self.button_volumeDown.setDisabled(False)
            self.label_screen.setPixmap(QtGui.QPixmap("black.png"))
            self.label_mute.clear()
            self.label_channel.setText(f'Channel: 0')
            self.label_volume.setText(f'Volume: 0')
        else:
            self.__status = True
            self.show_channel()


    def mute(self):
        """
        Method to mute and unmute volume
        :return: True or False to self.__muted and return self.__volume changes
        """
        if self.__muted and self.__status == True:
            self.__muted = False
            self.button_volumeUp.setDisabled(False)
            self.button_volumeDown.setDisabled(False)
            self.label_volume.setText(f'Volume: {self.__volume}')
            self.label_mute.clear()
        elif self.__muted == False and self.__status == True:
            self.__muted = True
            self.button_volumeUp.setDisabled(True)
            self.button_volumeDown.setDisabled(True)
            self.label_volume.setText(f'Volume: {Controller.MIN_VOLUME}')
            self.label_mute.setPixmap(QtGui.QPixmap("mute.jpg"))

    def channel_up(self):
        """
        Method to increase channel number by 1
        :return: increase to self.__channel
        """
        if self.__status:
            if self.__channel >= Controller.MIN_CHANNEL and self.__channel < Controller.MAX_CHANNEL:
                self.__channel += 1
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')

            elif self.__channel == Controller.MAX_CHANNEL:
                self.__channel = Controller.MIN_CHANNEL
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')

    def channel_down(self):
        """
        Method to decrease channel number by 1
        :return: decrease to self.__channel
        """
        if self.__status:
            if self.__channel > Controller.MIN_CHANNEL and self.__channel <= Controller.MAX_CHANNEL:
                self.__channel -= 1
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')
            elif self.__channel == Controller.MIN_CHANNEL:
                self.__channel = Controller.MAX_CHANNEL
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')

    def volume_up(self):
        """
        Method to increase volume by 1
        :return: increase to self.__volume
        """
        if self.__status:
            if self.__volume < Controller.MAX_VOLUME:
                self.__volume += 1
                self.label_volume.setText(f'Volume: {self.__volume}')
            elif self.__volume == Controller.MAX_VOLUME:
                self.__volume = Controller.MAX_VOLUME

    def volume_down(self):
        """
        Method to decrease volume by 1
        :return: decrease to self.__volume
        """
        if self.__status:
            if self.__volume > Controller.MIN_VOLUME:
                self.__volume -= 1
                self.label_volume.setText(f'Volume: {self.__volume}')
            elif self.__volume == Controller.MIN_VOLUME:
                self.__volume = Controller.MIN_VOLUME
                self.label_volume.setText(f'Volume: {self.__volume}')

    def show_channel(self):
        """
        Method to update screen corresponding to the channel
        :return: updates image on screen
        """
        if self.__channel == 0:
            self.label_screen.setPixmap(QtGui.QPixmap("disney.jpg"))
        elif self.__channel == 1:
            self.label_screen.setPixmap(QtGui.QPixmap("hulu.jpg"))
        elif self.__channel == 2:
            self.label_screen.setPixmap(QtGui.QPixmap("netflix.png"))
        elif self.__channel == 3:
            self.label_screen.setPixmap(QtGui.QPixmap("Crunchyroll.jpg"))

    def button_0(self):
        """
        Method to control Disney Button
        :return: updates image on screen
        """
        if self.__status:
            if self.__status == True:
                self.__channel = 0
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')

    def button_1(self):
        """
        Method to control Hulu Button
        :return: updates image on screen
        """
        if self.__status:
            if self.__status == True:
                self.__channel = 1
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')

    def button_2(self):
        """
        Method to control Netflix Button
        :return: updates image on screen
        """
        if self.__status:
            if self.__status == True:
                self.__channel = 2
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')

    def button_3(self):
        """
        Method to control Crunchyroll Button
        :return: updates image on screen
        """
        if self.__status:
            if self.__status == True:
                self.__channel = 3
                self.show_channel()
                self.label_channel.setText(f'Channel: {self.__channel}')
