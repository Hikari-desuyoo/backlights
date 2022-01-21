import os

def set_brightness(value, key='all'):
    key_dict = {
        'all':'dell::kbd_backlight',
        'caps':'dell::kbd_backlight/subsystem/input3::capslock'
    }

    os.system(f"sudo bash -c \'echo {value} > /sys/devices/platform/dell-laptop/leds/{key_dict[key]}/brightness\'")
