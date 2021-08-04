# music_tools
Various music related tools which is based on my idea which are just come up with.

# Requirements
use pip command or conda command(if you are using Anaconda)
```
pip install pandas
```

# Description
## scale2freq.py
Main function is to provide map of scale(音階) to frequency(周波数). **A#0 = As0** in the code. Also provide function which beep the sound according to passed frequency and duration of time.  
reference: https://tomari.org/main/java/oto.html 

## keyboard_play.py
Enable user to play the music with keyboard(is**Computer Keyboard** not Piano Keyboard!!). By running comannd below, and you will be able to play the music like Piano.
```
python keyboard_play.py "asdfghjkl;'#" "wrtuio[]"
```
First argument correspond to normal scale(not sharpe one like A3), and second argument correspond to sharpe scale(like A#3). 
Above example is using UK keybord.

![piano_keys](https://user-images.githubusercontent.com/44910734/128111831-d44a3869-959d-4d6b-8d45-31987bc01e86.jpg)
retrieved from http://www.piano-keyboard-guide.com/piano-notes.html  

retrieved from https://keyshorts.com/blogs/blog/44712961-how-to-identify-laptop-keyboard-localization#uk-british-english

The mapping of the key to scale is defined in the code.
To finish the program, please enter ESC key.
