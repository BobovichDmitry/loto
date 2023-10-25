import pytest
import unittest
from lotoclass import *


def test_strike():
    assert strike('2') == '2' + '\u0336'


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card_people = Lotocard()

    def test_init(self):
        #card_people = Lotocard()
        # print(len(card_people.card))
        assert len(self.card_people.card) == 27
        assert 100 not in self.card_people.card
    # def test_printcard(self):
    #    card_people = Lotocard()
    #    assert ' ' in card_people.printcard()
    def test_remove_card(self):
        assert self.card_people.winpoint == 15

    def test_remove_number(self):
        for i in range(90):
            if i in self.card_people.card:
                self.card_people.removenumberincard(i)
                assert self.card_people.winpoint == 14
                break