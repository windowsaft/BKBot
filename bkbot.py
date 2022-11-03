from sys import path
path.append('BKBot') # avoid import error

from BKBot.main import BKBot

if __name__ == '__main__':
    _BKBot = BKBot()
    _BKBot.FillIn()