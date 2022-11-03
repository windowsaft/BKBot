from pages import BKBotPages
from helpers import PrintHelp
import sys


class BKBot ():
    def __init__(self) -> None:
        """
            Options: \n
                        --help          / -h \n
                        --time          / -t \n
                        --store_number  / -s
        """
        
        _arguments = sys.argv
        s = 0
        d = 0


        if "-h" in _arguments:
            _index = _arguments.index("-h")
            s = -1

        elif "--help" in _arguments:
            _index = _arguments.index("--help")
            s = -1

        
        else:
            if "-d" in _arguments:
                _index = _arguments.index("-d")
                self.day = _arguments[_index + 1]
                
                try:
                    self.day = int(self.day)
                    d = 1

                except Exception as _e:
                    print(_e)
                    d = 0


            elif "--day" in _arguments:
                _index = _arguments.index("--day")
                self.day = _arguments[_index + 1]
                
                try:
                    self.day = int(self.day)
                    d = 1

                except Exception:
                    print(f'ValueError: "{self.day}" is not an integer. Only integers are vaild!')
                    d = 0



            try:
                _index = _arguments.index("--time")
                self.time = _arguments[_index + 1]

            except Exception:
                try:
                    _index = _arguments.index("-t")
                    self.time = _arguments[_index + 1]

                except Exception:
                    print("Missing Argument: time")
                    s = 1


            try:
                _index = _arguments.index("--store_number")
                self.store_number = _arguments[_index + 1]

            except Exception:
                try:
                    _index = _arguments.index("-s")
                    self.store_number = _arguments[_index + 1]

                except Exception:
                    print("Missing Argument: store_number")
                    s = 1

        if s == 0:
            if d == 1:
                self.BKBotP = BKBotPages(self.store_number, self.time, self.day)

            else:
                self.BKBotP = BKBotPages(self.store_number, self.time)

        elif s == -1:
            PrintHelp()
            exit()

        else:
            print("Error: Not all requierd arguments were given!")
            print("\n")
            print("This may help you:")
            print()
            PrintHelp()
            exit()


    def FillIn (self):
        for i in range(1, 65, 1):
            self.BKBotP.page(i)


if __name__ == '__main__':
    _BKBot = BKBot()
    _BKBot.FillIn()

        



