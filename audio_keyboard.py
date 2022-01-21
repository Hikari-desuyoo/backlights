from audio import Audio
from keyboard import set_brightness

class AudioKeyboard(Audio):
    light_value = {
        0:0.03,
        1:0.06,
        2:10
    }

    def on_read(self, data):
        amplitude = self.get_rms(data)
        self.set_brightness_by_amplitude(amplitude)

    def set_brightness_by_amplitude(self, amplitude):
        for light_value, amplitude_value in self.light_value.items():
            if amplitude < amplitude_value:
                value_to_set = light_value
                break

        
        set_brightness(value_to_set)