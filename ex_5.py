from time import sleep
from librip.ctxmngrs import timer

if __name__ == '__main__':
    with timer():
        sleep(5.5)
