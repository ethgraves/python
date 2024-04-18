class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    volume_tracking = ['-']

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    # def get_status(self):
    #     return self.__status

    def power(self):
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = Television.volume_tracking[0]
                Television.volume_tracking[0] = '-'
            else:
                self.__muted = True
                Television.volume_tracking[0] = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = Television.volume_tracking[0]
                Television.volume_tracking[0] = '-'
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = Television.volume_tracking[0]
                Television.volume_tracking[0] = '-'
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
       return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


def main():
    pass

if __name__ ==  '__main__':
    main()
# Filler