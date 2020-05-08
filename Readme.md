Hello Developers, I have explained briefly my approach in making a GUI and I have named it as “MitBild” which deals with computer vision applications.  

How can I create a GUI?

We can create a GUI of our own by making use of Tkinter or by using PyQt library. Here, I have used PyQt library as I felt it was much more easier than Tkinter. You will need to download Qt Designer first, once the download is completed you can start designing how you want your GUI to look like. Check https://doc.qt.io/qt-5/qtdesigner-manual.html and https://dev.to/amigosmaker/python-gui-pyqt-vs-tkinter-5hdd for detailed information.

Just a GUI? 

We all know GUI is a tool which varies from a simple Calculator to Google Chrome and much more. Now it’s left to us how we want our GUI to function. Shall we make a GUI which deals with Images? Seems fine, let’s get started.
This GUI will deal with image and basic operations on the image such as rotate right, left and flip with the help of buttons. Detailed information about this tool can be understood in the MitBild functionality section below. Whenever a button is clicked, some operation should be performed on the image and it should be displayed.

How to operate with Image?

Just to make our lives simpler, Intel has developed OpenCV library of programming functions mainly aimed at real-time computer vision applications. We will be using a lot of OpenCV functions in the development of this tool. To get detailed information check  https://opencv.org/.

Functionality of MitBild:
![Flow chart](https://user-images.githubusercontent.com/63425115/81398766-7f241c80-9147-11ea-9c7c-17880ebef0d3.JPG)

How does the tool look like? Follow the steps below.

**Important: From the repository download MitBild.py and Help.py, make sure that both are in the same folder**

Step1: 
Run MitBild.py and a new window opens which looks like this

![1 GUI MainWindow](https://user-images.githubusercontent.com/63425115/81399594-dc6c9d80-9148-11ea-9086-f2d3f65377d2.JPG)

Now the tool is ready to be used! Get Started 

Step2: Let’s select an image by clicking “Add Image” Button. 

![2 GUI AddImage](https://user-images.githubusercontent.com/63425115/81399623-eee6d700-9148-11ea-824a-2d813473af78.JPG)
Now the Image and it’s Histogram are displayed. The other Buttons are now active and waiting to be clicked. For more details about Histogram check https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html

Step3: HSV Image, Harris Detection and Canny Detection

Harris detection and Canny detection are feature detections which determines the Corner and Edge respectively in an Image. The HSV .i.e. Hue, Saturation and Value is an easier way to represent a color than RBG model. For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

![Feature Det](https://user-images.githubusercontent.com/63425115/81399270-5cdece80-9148-11ea-949c-4df329e95f5e.JPG)

In order to know more, check
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html and https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html#harris-corners

Step4: Image Effects

We all have used filters while editing an Image, uploading on instagram or any social media platforms. Now let us also add few filters on an Image in this tool. Just by clicking buttons under Image Effects section the filter will be applied to the Image as shown below. You can find more filters here https://pypi.org/project/pilgram/

![Image Filters](https://user-images.githubusercontent.com/63425115/81399318-7122cb80-9148-11ea-8d41-89670aee9842.JPG)

Now, let us also see how the histogram changes with respect to the applied filter. 

![All In one](https://user-images.githubusercontent.com/63425115/81399218-49cbfe80-9148-11ea-8fd6-f537dabf5ac7.JPG)

Step5: Salient features

When we look at an Image, our brain will automatically focus on the important region in an Image. Let us implement this in our tool. 
The Saliency Map determines roughly the important region present in the Image. Each pixel will be allotted a value between 0 and 1. If the pixel consists any important portion then it will assigned a value closer to 1 and vice versa. The Saliency Detection multiplies each pixel with 255 and calculates the Salient region. The Threshold Image  would be a useful to extract the ROI of the likely object. For detailed explanation check https://www.pyimagesearch.com/2018/07/16/opencv-saliency-detection/

![Saliency Detection](https://user-images.githubusercontent.com/63425115/81399416-96173e80-9148-11ea-81d8-1e5a2411217e.jpg)

What is Object Detection?

 Object Detection is an application related to computer vision and image processing that deals with detecting and locating instances of semantic objects of a certain class (such as humans, buildings, or cars) in digital images. In order to detect objects in an Image we need to train the model with few classes (Eg: Car, Person, Dog etc). RCNN and YOLO are deep learning approaches for object detection. Here, we will be using YOLO (You only look once) approach. In order to know more about YOLO check https://heartbeat.fritz.ai/introduction-to-basic-object-detection-algorithms-b77295a95a63 .
 
 Step6: Object Detection 
 
In this tool we are using OpenCV framework with YOLO algorithm to detect objects. Just make sure that you have OpenCV 3.4.2 at least installed in your system. In order to detect objects we need to have some important files such as Weight file, cfg file and Name files which can be downloaded from https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/. 

Important: Make sure that MitBild.py, Help.py, coco.names, yolov3 and yolov3.weights are in the same folder in order to detect objects successfully. 

![Object Detection](https://user-images.githubusercontent.com/63425115/81399374-84ce3200-9148-11ea-8f01-8189bb0cbc24.jpg)

Step7: You can Save the displayed image as JPEG format. The Exit button closes the tool.

I hope this tool brought some fun while using it.
Thank you

















