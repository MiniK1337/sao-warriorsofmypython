import time
import random
import hashlib

def renderEnds():
    a1 = str(random.randint(1, 100)).encode()

    time.sleep(random.randint(100, 500) / 1000)

    a2 = str(random.randint(1, 100)).encode()

    return hashlib.sha1(a1).hexdigest() == hashlib.sha1(a2).hexdigest()

def calculateLine(line):
    while True:
        if renderEnds():
            print(f"Линия \"{line}\" успешно обработана")
            break
        yield hashlib.sha1(str(random.random()).encode()).hexdigest()

def threadHelper(line):
    time.sleep(random.randint(1, 10))
    hashes = []
    for i in calculateLine(line):
        hashes.append(i)
        for s in range(100000):
            hashes.append(hashlib.sha1(str(i + str(s) * s).encode()).hexdigest())
