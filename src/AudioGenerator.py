from pydub.generators import Sine
from pydub.playback import play

def generate(frequency, duration, level=0, smooth_start=1, smooth_end=1):
    if smooth_start <= 0:
        smooth_start = 1

    if smooth_end <= 0:
        smooth_end = 1

    # Generate a sine tone with frequency self.freq
    gen = Sine(frequency)
    # AudioSegment with duration self.duration in ms, gain -3
    sine = gen.to_audio_segment(duration).apply_gain(level)
    # Fade in / out
    sine = sine.fade_in(smooth_start).fade_out(smooth_end)
    # Play the result
    play(sine)

if __name__ == "__main__":
    generate(500, 1000, smooth_end=100, smooth_start=10, level=0)