'''
* This MusicBoxExecutable program, by usage of a Musicbox class,
* is able to play music notes corresponding to integer values.
*  
*
* @author  Nathaniel Ventura
* @version 1.0
* @since   2019-11-30
'''
from musicbox import MusicBox

'''
Notes start from C as the number 60, and for
every whole note, the number connected to each note
goes up by 2.

Chords can also be played, in addition to individual notes.
'''
NOTES = [('C', 60), ('D', 62), ('E', 64), ('F', 65), ('G', 67), ('A', 69), ('B', 71)]
mymusic = MusicBox(0)

'''
Converts from letter note to integer.  Checks for sharps(#) and flats (b)
by going through each line of text.  Checks for notes marked with '^'
as octaves, and adjusts accordingly.
'''
def note_to_int(note):
    octave = note.rfind('^') + 1
    flat_or_sharp = note[octave + 1:]
    full_note = note[octave] 
    

    for i in NOTES: 
        (letter, num) = i
        if letter in full_note:
            letter_value = num
            if flat_or_sharp == '#':
                letter_value += 1
            elif flat_or_sharp == 'b':
                letter_value -= 1
            letter_value += (octave * 12)
    return letter_value

'''
Function that takes in file. Reads converted notes as integers, and has
special accomodations for stopping music and changing instrument sound.
Also has functionality for more than 1 note played (as chords).
'''
def play_song(song_file_name):
    for line in open(song_file_name):
        every_list = line.strip().split(' ')   
        time_sec = every_list[-1] 
        note_prelim = every_list[0]
        if note_prelim != '//': 
            if len(every_list) <= 2: 
                if note_prelim == 'P': 
                    mymusic.pause(int(time_sec))
                elif note_prelim == 'I': 
                    if int(time_sec) <= 127:
                        instrument_change = int(time_sec)
                    mymusic.set_instrument(instrument_change)
                else:
                    note_final = note_to_int(note_prelim)
                    mymusic.play_note(note_final, int(time_sec))
            elif len(every_list) > 2: 
                chord_notes = every_list[0:-1] 
                empty_list = []
                for n in chord_notes:
                    a = note_to_int(n)
                    empty_list.append(a)
                mymusic.play_chord(empty_list, int(time_sec))
        else:
            continue
            
if __name__ == "__main__":
    file_name = input("Please enter a file name: \n")
    play_song(file_name)
            
                
