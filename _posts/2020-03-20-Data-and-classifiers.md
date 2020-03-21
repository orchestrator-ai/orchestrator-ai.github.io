---
title: Music Classifiers and how UMTN processes data
layout: post
author: Alicia and James
---
making our own music classifier + brief overview of how UMTN collects data

## Music Classifiers



### Helpful Resources for inspiration:

[Pytorch Audio Classifier Tutorial](https://pytorch.org/tutorials/beginner/audio_classifier_tutorial.html?highlight=audio)
- Uses the UrbanSound8K dataset (contains 10 audio classes with over 8000 audio samples, classes such as air_conditioner, car_horn, children_playing, dog_bark, drilling, enginge_idling, gun_shot, jackhammer, siren, and street_music)
- Data is formatted using `torchaudio`.
- CNN, modeled after the [M5 network architecture](https://arxiv.org/pdf/1610.00087.pdf)

[Music Genre Classification with Python](https://towardsdatascience.com/music-genre-classification-with-python-c714d032f0d8)
- Basic guide on processing music with `librosa`
- Has basic Jupyter notebook on classifying music
- Uses the GTZAN music dataset (consists of 1000 audio tracks each 30 seconds long. It contains 10 genres namely, blues, classical, country, disco, hiphop, jazz, reggae, rock, metal and pop. Each genre consists of 100 sound clips)

[Musical Genre Classification, Github Project by Dohppak](https://github.com/Dohppak/Music_Genre_Classification_Pytorch)
- Uses the GTZAN music dataset
- Processes music with `librosa`
- 4 layer CNN, validation accuracy is 77%, test accuracy of this model is 83.39%

[Music genre classification with LSTMs in Keras & PyTorch, Github Project by Ruohoruotsi](https://github.com/ruohoruotsi/LSTM-Music-Genre-Classification)
- Uses the GTZAN music dataset
- Processes music with `librosa`
- Multiple layers of LSTM Recurrent Neural Nets

## UMTN Data
- Use librosa for reading in audio files
- Also uses [h5py](http://docs.h5py.org/en/stable/quick.html), which is a Python package that lets you store huge amounts of numerical data and manipulate it from Numpy

```python
self.data = [DatasetSet(d, args.seq_len, args) for d in args.data]
```
This line of code is pulled from `train.py` and is basically how they pass in most data (`args.data` is passed in through the data parameters in the shell script `train.sh`)
- `DatasetSet` is located in `data.py`. Its subclasses such as `H5Dataset` help take the program take in .wav and .h5 files, process/sample them depending on specific parameters, and then return a dataset. More about manipulating/pulling data from datasets can be found [here](http://docs.h5py.org/en/stable/quick.html).
