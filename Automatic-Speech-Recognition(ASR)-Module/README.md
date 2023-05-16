
# Automatic Speech Recognition(ASR) with simple RNN

An Automatic speech Recognition(ASR) with simple RNN applied on real dataset of 4 instruments(scalpel, straight dissection clamp, curved mayo scissor, straight mayo scissor) collected from surgeons doctors from different countries which are:  
-Egypt: Cairo, Assiut, Aswan  
-Scotland  
-Australia

Published a paper with all dataset and project documentation with name 'A Hybrid Speech-Vision Automated System of Robotic Scrub Nurse Using Deep Learning' in 
International Conference on Advanced Technology and Applied Sciences(ICATAS) 2022, Paper ID: 5962.

Features extracted with Mel-Frequency Cepstral Coefficients(MFCCs), passed to a simple RNN and result integrated with the computer vision module in order to apply object detection on 4 instruments using YOLOv5





## Installation

- Install Librosa
```
  !pip install librosa
```
- Install Tensorflow
```
  !pip install tensorflow
```
- Install preprocess
```
  !pip install preprocess
```

## Preprocessing

Data is collected and labeled manually so we don't need to explore it we already knew the structure of the data(all files are .wav format and data is balanced)

- Extracted features using MFCCs
- Mapped the features to the labels
- Encoded the labels
## Simple RNN

- Built and compiled the model
- Passed the data to the model
- Model Evaluation
