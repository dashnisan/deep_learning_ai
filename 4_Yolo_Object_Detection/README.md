# YOLO Object Detection: You Only Look Once

Here we use transfer learning from a pretrained YOLO model in order to make object detection.

The YOLO algorithm is in term of resources usage much more efficient than algorithms based on the "sliding windows"
method. However it requires also a lot of data to be trained; that is wha we selected to use a pre-trained model as base.

The base model used is the implementation of the C-Yolo version "Darknet" for Keras. We use it to detect objects in 
pictures. The outputs are stored to the folder "out".

Because of the ethical code of this course, the main functions of this exercise have been compiled and invoked from the 
main script.

Please note that the file containing the weights of the pre-trained model is bigger than 100MB. Because of this is not loaded to this repository. It is normally found under model_data/variables/variables.data-00000-of-00001

## REFERENCES

<ol>
<li> Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi - [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) (2015) </li> 
<li> Joseph Redmon, Ali Farhadi - [YOLO9000: Better, Faster, Stronger](https://arxiv.org/abs/1612.08242) (2016) </li> 
<li> Allan Zelener - [YAD2K: Yet Another Darknet 2 Keras](https://github.com/allanzelener/YAD2K) </li> 
<li> The official YOLO website (https://pjreddie.com/darknet/yolo/) </li> 
</ol>


