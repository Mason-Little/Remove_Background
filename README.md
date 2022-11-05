## all things cars interior and exterior

this repo containes many tools for cars interior and exterior classification,

**How to install**
```
git clone 'https://github.com/Mason-Little/Remove_Background.git'

cd Remove_Background

conda env create -f RemoveBackground.yml
```

 - dominant.py is used to find the 2 most dominant colours in a given folder ..\\data\\Input\\Interior and ..\\data\\Input\\Exterior or in ..\\data\\Output\\Interior and ..\\data\\Output\\Exterior which is changed within the code.

 - remove_background.py is used to remove the background and crop it to size, it will then output the data in the ..\\Output founder
 - binary image classification.ipynb is a fine-tuned model using the EfficientNetB0 model to classify images as interior or exterior of a car
 - notebook vehicle detection.ipynb uses a small custom build model that yields 96% accuracy on the test set when using my data set found at [here](https://drive.google.com/file/d/1XGXDr-L7VyGX-LRtDYUQIZzeGqYIQlL9/view) this data set has 1,278 interior images and 2,126 exterior images

 

