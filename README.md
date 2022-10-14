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
![Screenshot_2](https://user-images.githubusercontent.com/78471151/195842471-cee21f99-0088-4135-9d5a-29297f4fd57b.png)


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

audio_files list contains paths of  audio files in every folder. At every step in outer for loop actually we obtained a list that contains corresponding foldername's audiofiles. In the inner loop we've done neccesseary converting operations and saved figures to our computer.

## Preprocessing 
The aim of pre-processing is to improve the quality of the image so that we can analyse it in a better way. By preprocessing we can suppress undesired distortions and enhance some features which are necessary for the particular application we are working for. In this project we have preprocessed our images before training our deep learning model. Preprocessing operations we used as follows<br>
<ul>
        <li>Reshaping(128,128)</li>
        <li>Converting colorspace to grayscale from BGR</li>
        <li>Normalization</li>
</ul>
        
        inputs=os.listdir("./converted_audio")
        i=1
        print("Converting process of the images is started")
        for input in inputs:
            image=cv2.imread("./converted_audio/"+input)
            gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("./converted_audio/"+input, cv2.resize(gray_image, (128, 128)))
            i=i+1
        print("Converting process of the images is finished")

## Creating inputs and outputs list
In this section we created 2 list called outputs and inputs. First we've read all data using Image.open method and normalized all of them. Then we saved them into outputs and inputs lists again.

        inputs=os.listdir("./converted_audio")
        outputs=[]
        np.save("outputs.npy", outputs)
        new_inputs=[]
        for i in range(len(inputs)):
            outputs.append([int(inputs[i].split("-")[1])])
            image=Image.open("./converted_audio/"+inputs[i])
            arr=np.asarray(image)
            new_inputs.append(arr/255)
        outputs=np.array(outputs).astype(int)
        inputs=np.array(new_inputs)
      
        
## Train,Validation and Test Splitting
We've splitted 0.8 rate of all data as training data. Remained data was splitted into 2 parts equally. After that we created our pickle files for using them at the training section.

        X_train, X_test, y_train, y_test=train_test_split(inputs, outputs, random_state=42, test_size=0.2)
        X_val, X_test, y_val, y_test=train_test_split(X_test, y_test, test_size=0.5)
        print("Check if count of all train, validation and test set datas equal to total data")
        print(f"Total of all splitted data: {len(X_train)+len(X_val)+len(X_test)}")
        print(f"Total of datas do exist: {len(inputs)}")
        my_dataset=(X_train, y_train, X_val, y_val, X_test, y_test)
        f=open('dataset.pickle', "wb")
        pickle.dump(my_dataset, f)
        print("Process completed")
    
## Training Deep Learning Model


 
