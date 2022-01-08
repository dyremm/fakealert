from gtts import gTTS
import time
import os
import sys
import random

if __name__ == "__main__":
    delay = None
    randelayrange = None
    dirname = os.path.dirname(__file__)
    if len(sys.argv) < 2:
        print("devi inserire giusto il testo che vuoi far sentire, non metterci altro coglione")
        exit()
    if len(sys.argv) == 3:
        delay = int(sys.argv[2])
    elif len(sys.argv) == 4:
        randelayrange = [int(sys.argv[2]), int(sys.argv[3])]

    with open(os.path.join(dirname, 'nomi.txt'),  'r') as f:
        names = f.readlines()
    name = names[random.randint(0, len(names))]
    s = f"{name} ha donato {random.randint(1, 10)}.{random.randint(0,100)} euro. {sys.argv[1]}"
    gTTS(s, lang="it").save(os.path.join(dirname, "temp.mp3"))
    if delay is not None:
        time.sleep(delay)
    if randelayrange is not None:
        time.sleep(random.randrange(randelayrange[0], randelayrange[1]))
    os.system("mpg123 " + os.path.join(dirname, "alert.mp3"))
    os.system("mpg123 " + os.path.join(dirname, "temp.mp3"))

