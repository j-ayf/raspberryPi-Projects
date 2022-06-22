# Script that makes an LED blink to the rhythm of the "Imperial March" by John Williams

from gpiozero import LED
from time import sleep

led = LED(17)
SONG_BPM = 100
SPEED_MODIFIER = 60 / SONG_BPM
OFF_TIME = 0.05  # amount of seconds the LED will turn off between 'notes'


def main():
    for i in range(2):
        play_note(1)
        play_note(1)
        play_note(1)
        play_main_bam_ba_dam()
        play_main_bam_ba()
        play_note(2)
    play_note(1)
    play_main_bam_ba_dam()
    play_main_bam_ba()
    play_note(0.25)
    play_note(0.25)
    play_note(0.5)
    play_pause(0.5)
    play_note(0.5)
    play_note(1)
    play_main_bam_ba()
    play_note(0.25)
    play_note(0.25)
    play_note(0.5)
    play_pause(0.5)
    play_note(0.5)
    play_note(1)
    play_main_bam_ba_dam()
    play_main_bam_ba()
    play_note(2)
    play_note(1)
    play_main_bam_ba_dam()
    play_main_bam_ba()
    play_note(0.25)
    play_note(0.25)
    play_note(0.5)
    play_pause(0.5)
    play_note(0.5)
    play_note(1)
    play_main_bam_ba()
    play_note(0.25)
    play_note(0.25)
    play_note(0.5)
    play_pause(0.5)
    play_note(0.5)
    play_note(1)
    play_main_bam_ba_dam()
    play_main_bam_ba()
    play_note(2)


def play_note(length):
    """Turns on LED for required amount of time. Takes note length as absolute number in seconds, which then gets
    modified to be the correct speed for the song by the speed_modifier variable."""

    # length of one note depends on the bpm of the song. Off-time is subtracted from total to prevent build up of
    # offset, especially in fast sections
    length *= SPEED_MODIFIER - OFF_TIME

    led.on()
    sleep(length)
    led.off()
    sleep(OFF_TIME)


def play_pause(length):
    """Keeps the LED off for required amounf of time. Takes pause length as absolute number in seconds, which then gets
    modified to be the correct speed for the song by the speed_modifier variable."""
    length *= SPEED_MODIFIER

    sleep(length)


def play_main_bam_ba():
    """Recurring dotted eighth note with following sixteenth note"""
    play_note(0.75)
    play_note(0.25)


def play_main_bam_ba_dam():
    """Recurring dotted eighth note with following sixteenth and quarter note."""
    play_main_bam_ba()
    play_note(1)


if __name__ == '__main__':
    main()
