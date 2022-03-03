import simpleaudio as sa
import time
def play_sound():
    wave_obj = sa.WaveObject.from_wave_file("./wav/buzzer.wav")
    # wave_obj = sa.WaveObject.from_wave_file("./wav/alam-sutera.wav")
    for i in range(5):
        play_obj = wave_obj.play()
        play_obj.wait_done()
        time.sleep(1)
    print("PLAYSOUND - Finish")

