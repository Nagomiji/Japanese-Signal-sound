import RPi.GPIO as GPIO
import argparse
import time

SPEAKER_PIN = 26
RED = 16
GREEN = 20

def main():
    parser = argparse.ArgumentParser(
                prog='signal', # プログラム名
                description='Process some integers.', # 引数のヘルプの前に表示
                epilog='end', # 引数のヘルプの後で表示
                add_help=False, # -h/–help オプション
                )
    parser.add_argument('type', nargs='?', default=1, type=int)
    args = parser.parse_args()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # メロディーのノートとその持続時間を定義
    ra1 = 116.541
    si1 = 130.813
    do2 = 138.591
    re2 = 155.563
    mi2 = 174.614
    fa2 = 184.997
    so2 = 207.652
    ra2 = 233.082
    si2 = 261.626
    do3 = 277.183
    re3 = 311.127
    fa3 = 369.994

    try:
        if args.type == 1:
            melody = [
                (0, 1.5),
                (850, 0.2),
                (0, 0.5),
                (640, 0.7),
            ]

        elif args.type == 2:
            melody = [
                (0, 2.0),
                (mi2, 1.0),
                (mi2, 1.0),
                (re2, 1.0),
                (mi2, 1.0),
                (mi2, 0.5),
                (re2, 0.5),
                (si1, 2.0),
                (fa2, 1.0),
                (fa2, 0.5),
                (fa2, 0.5),
                (ra2, 1.0),
                (fa2, 0.5),
                (mi2, 0.5),
                (fa2, 0.5),
                (mi2, 0.5),
                (re2, 0.5),
                (re2, 0.5),
                (mi2, 1.0),
                (0, 1.0),
                (fa2, 1.0),
                (fa2, 2.0),
                (ra2, 0.5),
                (fa2, 0.5),
                (mi2, 0.5),
                (fa2, 0.5),
                (mi2, 0.5),
                (re2, 0.5),
                (re2, 0.5),
                (mi2, 1.0),
                (0, 1.0),
                (do2, 1.5),
                (do2, 0.5),
                (mi2, 1.0),
                (do2, 0.5),
                (si1, 0.5),
                (do2, 0.5),
                (si1, 0.5),
                (ra1, 0.5),
                (ra1, 0.5),
                (si1, 1.0),
                (0, 1.0),
                (do2, 0.5),
                (do2, 1.0),
                (do2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (do2, 0.5),
                (si1, 0.5),
                (do2, 0.5),
                (si1, 0.5),
                (ra1, 0.5),
                (ra1, 0.5),
                (si1, 1.0),
                (0, 1.0),
                (fa2, 0.5),
                (fa2, 0.5),
                (fa2, 0.5),
                (fa2, 0.5),
                (ra2, 0.5),
                (ra2, 0.5),
                (fa2, 0.5),
                (mi2, 0.5),
                (fa2, 0.5),
                (mi2, 0.5),
                (re2, 0.5),
                (re2, 0.5),
                (mi2, 2.0),
                (do2, 0.5),
                (do2, 0.5),
                (do2, 0.5),
                (do2, 0.5),
                (do2, 0.5),
                (mi2, 0.5),
                (do2, 0.5),
                (si1, 0.5),
                (do2, 0.5),
                (si1, 0.5),
                (ra1, 0.5),
                (ra1, 0.5),
                (si1, 1.0),
                (0, 1.0),
                (mi2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (re2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (mi2, 0.5),
                (re2, 0.5),
                (ra1, 0.5),
                (ra1, 0.5),
                (si1, 1.0),
                (0, 0.5),
                (ra1, 0.5),
                (si1, 0.5),
                (do2, 0.5),
                (re2, 0.5),
                (mi2, 0.5),
                (fa2, 0.5),
                (mi2, 0.5),
                (fa2, 1.0),
                (ra2, 1.0),
                (si2, 0.5),
                (ra2, 0.5),
                (fa2, 1.0),
                (mi2, 1.0),
                (mi2, 0.5),
                (re2, 0.5),
                (si1, 2.0)
            ]

        elif args.type == 3:
            melody = [
                (0, 2.0),
                (re2, 1.0),
                (re2, 0.5),
                (re2, 1.0),
                (si2, 0.5),
                (ra2, 1.0),
                (so2, 0.5),
                (ra2, 1.0),
                (si2, 0.5),
                (re2, 1.0),
                (re2, 0.5),
                (mi2, 1.0),
                (re2, 0.5),
                (so2, 2.0),
                (0, 1.0),
                (re2, 1.0),
                (re2, 0.5),
                (re3, 1.0),
                (si2, 0.5),
                (ra2, 1.0),
                (so2, 0.5),
                (ra2, 1.0),
                (si2, 0.5),
                (re2, 1.0),
                (re2, 0.5),
                (mi2, 1.0),
                (re2, 0.5),
                (so2, 2.0),
                (0, 1.0),
                (re3, 1.0),
                (si2, 0.5),
                (so2, 1.0),
                (si2, 0.5),
                (ra2, 1.0),
                (so2, 0.5),
                (ra2, 1.0),
                (si2, 0.5),
                (re3, 1.0),
                (si2, 0.5),
                (so2, 1.0),
                (re3, 0.5),
                (fa3, 3.0),
                (re3, 1.0),
                (si2, 0.5),
                (do3, 1.0),
                (ra2, 0.5),
                (si2, 1.0),
                (so2, 0.5),
                (ra2, 1.0),
                (so2, 0.5),
                (re2, 1.0),
                (re2, 0.5),
                (mi2, 1.0),
                (re2, 0.5),
                (so2, 2.0),
            ]

        else:
            exit()

        GPIO.setup(SPEAKER_PIN, GPIO.OUT)
        GPIO.setup(RED, GPIO.OUT)
        GPIO.setup(GREEN, GPIO.OUT)
        if GPIO.input(GREEN) == 1:
            GPIO.output(GREEN, False)
        GPIO.output(RED, True)
        time.sleep(5)
        GPIO.output(RED, False)
        GPIO.output(GREEN, True)

        while True:
            for freq, dur in melody:
                play_note(freq, dur)

    except KeyboardInterrupt:
        if GPIO.input(RED) == 1:
            GPIO.output(RED, False)
            exit()
        for i in range(15):
            GPIO.output(GREEN, False)
            time.sleep(0.2)
            GPIO.output(GREEN, True)
            time.sleep(0.2)
        GPIO.output(GREEN, False)
        GPIO.output(RED, True)
        time.sleep(5)
        GPIO.cleanup()

def play_note(frequency, duration):
    if frequency == 0:
        time.sleep(duration / 2)
        return
    period = 1.0 / frequency
    half_period = period / 2
    cycles = int(duration * frequency)
    
    for _ in range(cycles):
        GPIO.output(SPEAKER_PIN, GPIO.HIGH)
        time.sleep(half_period / 2)
        GPIO.output(SPEAKER_PIN, GPIO.LOW)
        time.sleep(half_period / 2)

if __name__ == "__main__":
    main()