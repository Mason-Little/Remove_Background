## all things cars interior and exterior

In this repo there are many tool for cars interior and exterior,

**How to install**
```
git clone 'https://github.com/Mason-Little/Remove_Background.git'

cd Remove_Background

conda env create -f environment.yml
```
note: if you want to run remove_background.py you need to pip install rembg in a new environment without tensorflow install, they do not play nice together.

 - dominant.py is used for find the 2 most dominant colour in a given folder ..\\data\\Input\\Interior and ..\\data\\Input\\Exterior or in ..\\data\\Output\\Interior and ..\\data\\Output\\Exterior which is changed within the code.

 - remove_background.py is used for removing the background and cropping for size it will then output the data in the ..\\Output founder
 - binary image classification.ipynb is a fine-tuned model using the EfficientNetB0 model to classify images as interior or exterior of a car
 - notebook vechile detection.ipynb uses a small custom build model that yeild 96% accuracy on the test set when using my data set found at [here](https://drive.google.com/file/d/1XGXDr-L7VyGX-LRtDYUQIZzeGqYIQlL9/view) this data set has 1,278 interior images and 2,126 exterior images

 

