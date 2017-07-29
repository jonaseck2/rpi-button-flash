#!/usr/bin/env python
try:
    import RPi.GPIO as GPIO
    from time import sleep
    from os import getenv

    GPIO.setmode(GPIO.BCM)

    channel_switch = int(getenv('CHANNEL_SWITCH', 17))
    channel_led = int(getenv('CHANNEL_LED', 18))
    pwm_cycle = float(getenv('PWM_CYCLE', 0.005))
    num_flashes = int(getenv('NUM_FLASHES', 3))

    GPIO.setup(channel_led, GPIO.OUT)
    pwm_led = GPIO.PWM(channel_led, 100)
    pwm_led.start(0)

    def callback_flash(channel):
        for flashes in range(1, num_flashes):
            for i in range(0,101):      # 101 because it stops when it finishes 100
                pwm_led.ChangeDutyCycle(i)
                sleep(pwm_cycle)
            for i in range(100,-1,-1):      # from 100 to zero in steps of -1
                pwm_led.ChangeDutyCycle(i)
                sleep(pwm_cycle)

    GPIO.setup(channel_switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(channel_switch, GPIO.RISING, callback=callback_flash, bouncetime=1000)

    print ("Ready")
    while True:
        sleep(1000)

    pwm_led.stop()
    GPIO.cleanup()
except KeyboardInterrupt:
    pwm_led.stop()
    GPIO.cleanup()
