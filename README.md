# wav2samp
This package can be used to convert wav file in to a text file with audio samples and vice versa.

## Installation
Before use the package please install by using the following command in the terminal.

  ```bash
  pip install wav2samp
  ```
## Usage
There are four functions in this python package.

* The following function can be used to convert .txt file which contains audio samples in to mono .wav file.

` txt2mono_wav(txt_file, sample_rate, wav_file)`


* The following function can be used to convert mono .wav file in to a .txt file with audio samples.

` mono_wav2txt(file_name, txt_file) `


* The following function can be used to convert stereo .wav file in to two .txt files with audio samples of left and right audio contents.

` stereo_wav2txt(file_name, txt_left, txt_right)`


* The following function can be used to convert two .txt file which contains audio samples of left and right audio content in to stereo .wav file.

` txt2stereo_wav(txt_left, txt_right, sample_rate, wav_file)`

The following is the usage in a python file.

```python
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
```



