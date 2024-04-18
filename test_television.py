import pytest
from television import *

class Test:
    def setup_method(self):
        self.test1 = Television()
        self.test2 = Television()
        self.test3 = Television()

    def teardown_method(self):
        del self.test1
        del self.test2
        del self.test3

    def test_init(self):
        assert self.test1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    # FIXME: Ask for help on this
    def test_power(self):
        self.test1.power()
        assert self.test1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass