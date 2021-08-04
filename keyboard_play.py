import sys
import time
import multiprocessing
from msvcrt import getch
from winsound import Beep
from scale2freq import set_scale, scale2freq

key2scale = {}
scale_normal = ["A3","B3","C4","D4","E4","F4","G4","A4","B4","C5","D5","E5"]
scale_sharpe = ["As3","Cs4","Ds4","Fs4","Gs4","As4","Cs5","Ds5"]

def setkey(keys,keys_sharpe):
    if (len(keys) != len(scale_normal)) or (len(keys_sharpe) != len(scale_sharpe)):
        raise ValueError("Invalid arguments: length of the input is not valid.")
    for i,key in enumerate(keys):
        key2scale[key] = scale_normal[i]
    for i,key in enumerate(keys_sharpe):
        key2scale[key] = scale_sharpe[i]
    print("Key mapping:")
    for key,scale in key2scale.items():
        print("{} -> {}".format(key,scale))
    
def play_scale(scale2freq,scale,duration=200):
    freq = int(scale2freq[scale])
    Beep(freq,duration)

if __name__ == "__main__":
    keys_normal = sys.argv[1]
    keys_sharpe = sys.argv[2]
    setkey(keys_normal, keys_sharpe)
    set_scale()
    playing = multiprocessing.Process(target=play_scale, args=(scale2freq,"A3",1))
    playing.start()
    print("\n Let's Start!!")
    print("---------------------------------------------------------")
    while True:
        pre_key = None
        key = getch()
        if key == b'\x1b': break        # if ESC is pressed, finish
        key = key.decode('utf-8')
        if key in key2scale:
            scale = key2scale[key]
            print("Pressed {} -> {}".format(key,scale))
            if key != pre_key:
                time.sleep(0.3)
                playing.terminate()
                playing = multiprocessing.Process(target=play_scale, args=(scale2freq,scale,500))
                playing.start()
            pre_key = key
        else:
            print("Key does not mapped to scale.")
    # finish
    print("Thank you for playing!!")





