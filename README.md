## Hand Gesture Recognition Project
### A simple CNN to detect five different hand gestures.

This project consists of a simple convolution neural network using Keras API.

It has been trained to recognise five hand gestures-
1. Open Hand / Full hand 
>![img_0](https://user-images.githubusercontent.com/64610850/120102929-e9509a80-c16a-11eb-8441-823ea9de03ad.jpg)
2. Closed Fist  
>![img_13](https://user-images.githubusercontent.com/64610850/120102946-fa011080-c16a-11eb-97d3-45740e181037.jpg)
3. OK gesture 
>![img_25](https://user-images.githubusercontent.com/64610850/120102950-fec5c480-c16a-11eb-8530-f84550a8b6ca.jpg)
4. Palm 
>![img_0](https://user-images.githubusercontent.com/64610850/120102962-09805980-c16b-11eb-9f5d-541a266062a2.jpg)
5. Thumbs up 
>![img_0](https://user-images.githubusercontent.com/64610850/120102993-2157dd80-c16b-11eb-9ffa-5bd71b801b6c.jpg)


Some photos of the project being tested - 

>![image](https://user-images.githubusercontent.com/64610850/120103120-b5c24000-c16b-11eb-9a14-ee686d9735c8.png)
>![image](https://user-images.githubusercontent.com/64610850/120103136-c5da1f80-c16b-11eb-9f74-6efbe37a7dd8.png)
>![image](https://user-images.githubusercontent.com/64610850/120103145-d68a9580-c16b-11eb-9735-c70687278df2.png)


The Neural Network Structure is as follows-
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 254, 254, 64)      640       
_________________________________________________________________
activation (Activation)      (None, 254, 254, 64)      0         
_________________________________________________________________
dropout (Dropout)            (None, 254, 254, 64)      0         
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 63, 63, 64)        0         
_________________________________________________________________
flatten (Flatten)            (None, 254016)            0         
_________________________________________________________________
dense (Dense)                (None, 128)               32514176  
_________________________________________________________________
activation_1 (Activation)    (None, 128)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 6)                 774       
_________________________________________________________________
activation_2 (Activation)    (None, 6)                 0         
=================================================================
Total params: 32,515,590
Trainable params: 32,515,590
Non-trainable params: 0
_________________________________________________________________
```


