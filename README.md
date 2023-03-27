# achira_image_classify

## Question 1 : Write a Python program to generate images
following:

## Step 1 - Generating Images

The programming solutions for generating images, using Parse command line arguments and several modules including os, argparse, random, and PIL (Python Imaging Library) which is a library that provides tools to process and manipulate images.

```
python achira.py input_folder output_folder/folder_name(class name) --out-dims 1024 1024 --num-images 250
```
## Breakdown of above line command

* input_folder": This is the path where the input folder containing the images that need to be processed.
* output_folder/folder_name": This is the path to the output folder where the processed images will be saved.
* "--out-dims": This is an optional argument that specifies the output dimensions of the processed images. In this case, the dimensions are set to 1024x1024 pixels(as mentioned).
* "--num-images": This is another optional argument that specifies the maximum number of images that should be processed by the Python script. In this case, the maximum number of images is set to 250(instead of 1000 for each images I made 250 for each classes)

# After generating the images, next step is to train the model where I need to classify/detect the classes based on the image we inference at the end of the prosess

## Step 2 - Model creation using generated images

## Final Words

The architecture uses three convolutional layers and three max pooling layers in the CNN part of the network, followed by two fully connected layers in the Dense part of the network. The total number of layers in this architecture is nine, including the input and output layers.

Breaking down the accuracy 

* Train/Valid - 98% 
* Test - 96% 
* Train/valid Loss - 0.0281 
* Test Loss: 0.08388208597898483

```
python achira_image_detection_classification.ipynb
```
Below is the code in the image to inference the image

![image](https://user-images.githubusercontent.com/50097581/227996609-da3752d3-a006-4df0-90d6-8707503bd198.png)

#Thanks

