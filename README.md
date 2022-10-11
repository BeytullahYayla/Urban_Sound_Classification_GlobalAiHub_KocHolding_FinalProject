# Urban Sound Classification 
In this project we aim to classify urban sounds using deep learning methods.
## Dataset Definition: Urban Sound 8K
Urban Sound 8k is a dataset that contains 8732 labeled sound excerpts of urban sounds from 10 classes: air_conditioner, car_horn, 
children_playing, dog_bark, drilling, engine_idling, gun_shot, jackhammer, siren, and street_music. The classes are 
drawn from the urban sound taxonomy described in the following article, which also includes a detailed description of 
the dataset and how it was compiled:

J. Salamon, C. Jacoby and J. P. Bello, "A Dataset and Taxonomy for Urban Sound Research", 
22nd ACM International Conference on Multimedia, Orlando USA, Nov. 2014.

You can easily access the complete dataset from following link:[UrbanSound8k](https://urbansounddataset.weebly.com/urbansound8k.html)

## The Goal Of The Project

The main goal of this project classifying sound excerpts by corresponding label. We are going to use spectogram images of every audio file instead of using directly audio files to train deep learning model. Because of the achivement of convolutional neural networks on classifying images we've used CNN model to train our model.

