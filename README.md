# Keyboard_Play
Software enable user to play music(sound) with computer keyboard which is based on my idea just come up with.

# Requirements
use pip command or conda command(if you are using Anaconda)
```
pip install pandas
```

# Description
## scale2freq.py
Main function is to provide map of scale(音階) to frequency(周波数). **A#0 = As0** in the code.  
reference: https://tomari.org/main/java/oto.html  

## keyboardPlay.py
Enable user to play the music with keyboard(is**Computer Keyboard** not Piano Keyboard!!). Function(play_score) provide which beep the sound according to passed frequency and duration of time.    
By running comannd below, and you will be able to play the music like Piano.
```
python keyboard_play.py "asdfghjkl;'#" "wrtuio[]"
```
First argument correspond to normal scale(not sharpe one like A3), and second argument correspond to sharpe scale(like A#3). 
Above example is using UK keybord.

![piano_keys](https://user-images.githubusercontent.com/44910734/128111831-d44a3869-959d-4d6b-8d45-31987bc01e86.jpg)
retrieved from http://www.piano-keyboard-guide.com/piano-notes.html  
![uk_keyboard](https://user-images.githubusercontent.com/44910734/128111926-76fab6ea-eeec-4e5f-b589-b256b067d5fc.png)
retrieved from https://keyshorts.com/blogs/blog/44712961-how-to-identify-laptop-keyboard-localization#uk-british-english

The mapping of the key to scale is defined in the code.
To finish the program, please enter ESC key.  

*Unfortinately the refrection speed of the sound beeped when key is pressed is much slower than piano. Using multiprocessing could be one of the biggest factor. However, without multiprocessing, the sound will not be canceled if new key is pressed immediately after the previous one.*  

## Note
Since this code purpose was just trying to realize what I come up with in one night, probably I will not come back to this code to modify it unless it interest me again.

**Of course feel free to modify code if you come up with good idea.**
