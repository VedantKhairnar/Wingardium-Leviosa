# Wingardium Leviosa

![Stars](https://img.shields.io/github/stars/VedantKhairnar/Wingardium-Leviosa.svg?style=social)
![Forks](https://img.shields.io/github/forks/VedantKhairnar/Wingardium-Leviosa.svg?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/VedantKhairnar/Wingardium-Leviosa.svg)
![Language](https://img.shields.io/github/languages/top/VedantKhairnar/Wingardium-Leviosa.svg)
[![GitHub](https://img.shields.io/github/license/VedantKhairnar/Wingardium-Leviosa.svg)](https://choosealicense.com/licenses/mit)
[![Say Thanks!](https://img.shields.io/badge/Say-Thanks!-yellow.svg)](http://bit.ly/2M0s0Vu)
[![HitCount](http://hits.dwyl.io/VedantKhairnar/Wingardium-Leviosa.svg)](http://hits.dwyl.io/VedantKhairnar/Wingardium-Leviosa)

#### Dedicated to my soulmate...a PotterHead

### Computer System Control using gestures

Ever thought, how awesome it will be if you could control ur computer system just by ur hand gestures?
This project provides you the provision to do so.

Control your system by ur fist. Now you can say, your computer is in your fist...

Using the ability that the whole system can be controlled using Keyboard.

    y coordinate increse : fist up : Tab View 
    y coordinate decrease : fist down : minimize all windows 
    x coordinate decrese : fist left : open task manager
    y coordinate decrease : fist right : change window 
    
#### Libraries Used :
    
    pynput (for keyboard control)
    cv2    (for hand gesture recognition)
 
 #### Logic:
  
    Fist Detection using HaarCascade
    Instruct System as per the gesture detected
    
#### Theory :

[Haar Cascade](https://medium.com/dataseries/face-recognition-with-opencv-haar-cascade-a289b6ff042a) is a machine learning object detection algorithm used to identify objects in an image or video
It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

The algorithm has four stages:

Haar Feature Selection
Creating  Integral Images
Adaboost Training
Cascading Classifiers
It is well known for being able to detect faces and body parts in an image, but can be trained to identify almost any object.


 
 For pynput reference, click [here](https://pypi.org/project/pynput/)
 
 For various Virtual-Key Codes, click [here](https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)
 
 #### Future Prospects :
 
    Addition of multiple gestures (now limited to fist)
    Improve the Efficieny using Deep Learning (specifically trained )
    
 For Any Queries, connect me :
 [Vedant Khairnar](http://vedantkhairnar.ml/)

