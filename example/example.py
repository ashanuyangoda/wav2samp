import wav2samp as w2s

# Creating a mono .wav file with sampling rate of 22050Hz from the audio samples of .txt file
w2s.txt2mono_wav('audio_content.txt', 22050, 'example1.wav')
print("  ")  # Extra space to separate different processes

# Creating a mono .wav file with sampling rate of 44000Hz from the audio samples of .txt file
w2s.txt2mono_wav('audio_content.txt', 44000, 'example2.wav')
print("  ")  # Extra space to separate different processes

# Creating a .txt file with audio samples by using mono .wav file
w2s.mono_wav2txt('mono_22050.wav', 'test1.txt')
print("  ")  # Extra space to separate different processes

# Creating two .txt files (left side and right side) by using a stereo .wav file
w2s.stereo_wav2txt('stereo_44100.wav', 'left.txt', 'right.txt')
print("  ")  # Extra space to separate different processes

# Creating a stereo .wav file using two .txt files (left side and right side)
w2s.txt2stereo_wav('left.txt', 'right.txt', 44100, 'stereo_test1.wav')


