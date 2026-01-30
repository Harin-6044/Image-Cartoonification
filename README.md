# Image-Cartoonification

### Description :

* <p align = "justify">A python program that is developed to cartoonify an image that is fed in as an input to the application. Here, the given input image is converted from its original form of image to its cartoon form of image.</p> 

* <p align = "justify">Python and OpenCV are the two main tools that are used to build this cartoonifying application. This is a menu-driven program that provides a menu to the users with several operations as options to be performed.</p>

### Requirements :

* Python
* Numpy
* CV2
* Imageio
* Matplotlib
* Easygui
* Tkinter
* OS

### Methodology :

* Uploading
* Greyscaling
* Smoothening
* Retrieving Edges
* Masking Image
* Cartooning Effect

<p align = "justify">&emsp;&emsp;First by using easygui, the upload of the image is done and then the image is converted to a greyscale image. The next two steps are the important steps for converting original images into cartoon images. They are smoothening and then retrieving the edges. In this process, color of the image is smoothened to give the cartoon look and then the retrieval of the edges are done and highlighted in the final image.</p>

<p align = "justify">&emsp;&emsp;Next, the preparation of the mask image is done. In this, the bilateral filter is used which removes the noise and smoothen it to some extent. Now the final step is giving the cartooning effect. To the image which is obtained in the previous step, the combination of the two important steps is done and finally gives a mask-edged image that looks like a cartoon image.</p>
