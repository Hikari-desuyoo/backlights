import pyaudio
import time
import numpy
import math
import struct
import threading

class Audio:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    SHORT_NORMALIZE = (1.0/32768.0)

    @classmethod
    def get_rms(cls, block):
        # RMS amplitude is defined as the square root of the 
        # mean over time of the square of the amplitude.
        # so we need to convert this string of bytes into 
        # a string of 16-bit samples...

        # we will get one short out for each 
        # two chars in the string.
        count = len(block)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, block )

        # iterate over the block.
        sum_squares = 0.0
        for sample in shorts:
            # sample is a signed short in +/- 32768. 
            # normalize it to 1.0
            n = sample * cls.SHORT_NORMALIZE
            sum_squares += n*n

        return math.sqrt( sum_squares / count )


    def __init__(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self.pyaudio.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK,
                        output_device_index=1)

    def finish(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

    def on_read(self, data):
        pass

    def update(self):
        data = self.stream.read(self.CHUNK)
        threading.Thread(target=self.on_read, args=(data,)).start()


