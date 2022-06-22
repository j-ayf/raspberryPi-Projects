# Executes the "imperialButton.py" script upon a button click

from gpiozero import Button
from signal import pause
import imperialLed


def main():
    button = Button(27)

    def button_released():
        print('Now playing "Imperial March" on LED')
        imperialLed.main()
        print('Finished playing.')

    print('Waiting...')
    button.when_released = button_released

    pause()


if __name__ == '__main__':
    main()
