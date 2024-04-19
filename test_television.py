import pytest
from television import *

class Test:
    '''Tests functions from television.py'''
    def setup_method(self):
        '''Creates an object called "test" from the Television class'''
        self.test = Television()

    def teardown_method(self):
        '''Deletes the "test" object from the Television class'''
        del self.test

    def test_init(self):
        '''Tests the __init__ function from the Television class'''
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        '''Tests the power function from the Television class'''
        # TV on
        self.test.power()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # TV off
        self.test.power()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        '''Tests the mute function from the Television class'''
        # TV on, volume increased once, TV muted
        self.test.power()
        self.test.volume_up()
        self.test.mute()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # TV on, TV unmuted
        self.test.mute()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # TV off, TV muted
        self.test.power()
        self.test.mute()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 1'

        # TV off, TV unmuted
        self.test.mute()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        '''Tests the channel_up function from the Television class'''
        # TV off, channel increased once
        self.test.channel_up()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # TV on, channel increased once
        self.test.power()
        self.test.channel_up()
        assert self.test.__str__() == 'Power = True, Channel = 1, Volume = 0'

        # TV on, channel increased past maximum value
        self.test.channel_up()
        assert self.test.__str__() == 'Power = True, Channel = 2, Volume = 0'
        self.test.channel_up()
        assert self.test.__str__() == 'Power = True, Channel = 3, Volume = 0'
        self.test.channel_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        '''Tests the channel_down function from the Television class'''
        # TV off, channel decreased once
        self.test.channel_down()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # TV on, channel decreased past minimum value
        self.test.power()
        self.test.channel_down()
        assert self.test.__str__() == 'Power = True, Channel = 3, Volume = 0'
        self.test.channel_down()
        assert self.test.__str__() == 'Power = True, Channel = 2, Volume = 0'
        self.test.channel_down()
        assert self.test.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.test.channel_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.channel_down()
        assert self.test.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        '''Tests the volume_up function from the Television class'''
        # TV off, volume increased once
        self.test.volume_up()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # TV on, volume increased once
        self.test.power()
        self.test.volume_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # TV on, muted, then volume increased once
        self.test.mute()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.volume_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 2'

        # TV on, volume increased past maximum value
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.test.volume_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.test.volume_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        '''Tests the volume_down function from the Television class'''
        # TV off, volume decreased once
        self.test.volume_down()
        assert self.test.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # TV on, volume decreased from max volume
        self.test.power()
        self.test.volume_up()
        self.test.volume_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.test.volume_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.test.volume_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.volume_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # TV on, muted, then volume decreased past minimum value
        self.test.volume_up()
        self.test.volume_up()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.test.mute()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.volume_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.test.mute()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.volume_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.mute()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.test.volume_down()
        assert self.test.__str__() == 'Power = True, Channel = 0, Volume = 0'