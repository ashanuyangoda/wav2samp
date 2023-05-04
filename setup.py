import setuptools
setuptools.setup(
name='wav2samp',
version='0.1',
author="Ashan Uyangoda",
author_email="ashan7git@gmail.com",
description="Convert wav file in to text file with audio samples and vice versa",
long_description="This package is mainly use for DSP purposes. This package contains different functions to convert wav files in to text files with audio samples and convert text files with audio samples in to wav files. This package supports both Stereo and Mono.",
packages=setuptools.find_packages(),
install_requires=['numpy', 'scipy'],
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)