from PyQt5.QtWidgets import *
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
        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_volumeUp.clicked.connect(lambda: self.volume_up())
        self.button_volumeDown.clicked.connect(lambda: self.volume_down())
        self.button_channelDown.clicked.connect(lambda: self.channel_down())
        self.button_channelUp.clicked.connect(lambda: self.channel_up())
        self.tv_output_label.setText(
            f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')

    def power(self):
        """
        Method to turn TV on and off
        :return: True or False to self.__status
        """
        if self.__status:
            self.__status = False
            self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
        else:
            self.__status = True
            self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')

    def mute(self):
        """
        Method to mute and unmute volume
        :return: True or False to self.__muted and return self.__volume changes
        """
        if self.__muted and self.__status == True:
            # DEBUG: fix mute logic
            self.__volume = Controller.MAX_VOLUME
            self.__muted = False
            self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
        elif self.__muted == False and self.__status == True:
            self.__volume = Controller.MIN_VOLUME
            self.__muted = True
            self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')

    def channel_up(self):
        """
        Method to increase channel number by 1
        :return: increase to self.__channel
        """
        if self.__status:
            if self.__channel >= Controller.MIN_CHANNEL and self.__channel < Controller.MAX_CHANNEL:
                self.__channel += 1
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
            elif self.__channel == Controller.MAX_CHANNEL:
                self.__channel = Controller.MIN_CHANNEL
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')

    def channel_down(self):
        """
        Method to decrease channel number by 1
        :return: decrease to self.__channel
        """
        if self.__status:
            if self.__channel > Controller.MIN_CHANNEL and self.__channel <= Controller.MAX_CHANNEL:
                self.__channel -= 1
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
            elif self.__channel == Controller.MIN_CHANNEL:
                self.__channel = Controller.MAX_CHANNEL
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')

    def volume_up(self):
        """
        Method to increase volume by 1
        :return: increase to self.__volume
        """
        if self.__status:
            if self.__volume < Controller.MAX_VOLUME:
                self.__volume += 1
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
            elif self.__volume == Controller.MAX_VOLUME:
                self.__volume = Controller.MAX_VOLUME
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')

    def volume_down(self):
        """
        Method to decrease volume by 1
        :return: decrease to self.__volume
        """
        if self.__status:
            if self.__volume > Controller.MIN_VOLUME:
                self.__volume -= 1
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
            elif self.__volume == Controller.MIN_VOLUME:
                self.__volume = Controller.MIN_VOLUME
                self.tv_output_label.setText(f'Power: {self.__status}\nMuted: {self.__muted}\nVolume: {self.__volume}\nChannel: {self.__channel}')
