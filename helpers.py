import time
import random
import hashlib

def renderEnds():
    a1 = str(random.randint(1, 1000)).encode()

    time.sleep(random.randint(100, 500) / 1000)

    a2 = str(random.randint(1, 1000)).encode()

    return hashlib.sha1(a1).hexdigest() == hashlib.sha1(a2).hexdigest()

def threadHelper(line):
    time.sleep(random.randint(1, 10))
    while True:
        if renderEnds():
            print(f"Линия \"{line}\" успешно обработана")
            break
