import pygame
import time
import pygame.midi


class MusicBox:
    def __init__(self, instrument=0):
        """Creates a new MusicBox variable. An optional parameter from 0 to 127 inclusive sets the instrument ID.
        Experiment with different IDs to play different instruments."""
        try:
            pygame.init()
            pygame.midi.init()
            id = pygame.midi.get_default_output_id()
        except e:
            id = 0
            
        if id >= 0:
            self.__player = pygame.midi.Output(id, 1)
            self.__instrument = instrument
            self.__enabled = True
        else:
            self.__enabled = False

    def close(self):
        if self.__enabled:
            self.__player.close()

    def play_note(self, note, duration):
        """Plays a single note for a given duration. The note is in integer notation."""
        print(f"<MusicBox: play_note({note}, {duration})>")
        if self.__enabled:
            self.__player.set_instrument(self.__instrument, 0)
            self.__player.note_on(note, 127, 0)
            time.sleep(duration / 1000)
            self.__player.note_off(note, 127, 0)

    def pause(self, duration):
        print(f"<MusicBox: pause({duration})")
        time.sleep(duration / 1000)

    def set_instrument(self, instrument):
        print(f"<MusicBox: set_instrument({instrument})")
        if self.__enabled:
            self.__instrument = instrument

    def play_chord(self, chord, duration):
        """Plays a list of notes at the same time, for the given duration."""
        print(f"<MusicBox: play_chord({chord}, {duration})>")
        if self.__enabled:
            channel = 0
            for note in chord:
                self.__player.set_instrument(self.__instrument, channel)
                self.__player.note_on(note, 127, channel)
                channel += 1
            time.sleep(duration / 1000)
            channel = 0
            for note in chord:
                self.__player.note_off(note, 127, channel)
                channel += 1


if __name__ == "__main__":
    # Example of how to use the MusicBox
    m = MusicBox()
    m.play_note(60, 400)
    m.play_note(64, 400)
    m.play_chord([60, 64, 67], 600)
    m.play_chord([60, 64, 67], 200)
    m.play_chord([60, 64, 67], 600)
    m.play_note(69, 400)
    m.play_note(69, 400)
    m.play_note(67, 800)
    m.close()
