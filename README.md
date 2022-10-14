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



## Creating List That Contains Paths of Audio Files

        audio_path="./audio/fold"
        audio_files=[]
        converted_list=[]
        converted_outputs=[]
        for i in range(10):
            audio_clips = os.listdir(audio_path+str(i+1))
            audio_files.append(audio_clips)
            
We have 10 folder in our dataset. Each one contains about 873 audio file. We would like to keep our audio files paths in audio_files list. To do that we've used listdir method imported from os library in python. This method basically takes 1 argument. It is the path of files that will be listed. In for loop actually we are passing to the folders. In every step we append training data's path to the audio_files list.

## Saving spectogram images to our working environment

As mentioned in the project document our primary aim was to convert our audio files into sectogram images and using that data to train our CNN model. In this section we 've saved spectogram images to our local computer.


                                i=1
                                for item in audio_files:
                                    x=1
                                    for audio in item:
                                        audio_file, sr= librosa.load(audio_path+str(i)+"/"+audio)
                                        converted_outputs.append([audio.split("-")[1]])
                                        converted_audio=create_spectrogram(audio_file)
                                        fig = plt.Figure()
                                        canvas = FigureCanvas(fig)
                                        plt.margins(0,0)
                                        ax = fig.add_subplot(111)
                                        p = librosa.display.specshow(converted_audio, ax=ax, sr=sr)
                                        fig.savefig("./converted_audio/"+audio+".png", bbox_inches='tight', pad_inches=0.0)
                                        x=x+1
                                    print(f"Part {i} completed")
                                    i=i+1

audio_files list contains paths of every audio file. We decided to

 

 
 
