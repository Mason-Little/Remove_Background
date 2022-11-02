import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import keras
from keras_preprocessing.image import ImageDataGenerator

# base model
model = tf.keras.applications.EfficientNetB0(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3))

model.trainable = False

inputs = keras.Input(shape=(224, 224, 3))
x = model(inputs, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dropout(0.2)(x)
outputs = keras.layers.Dense(2)(x)
model = keras.Model(inputs, outputs)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# loading the data
train_data_gen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    rotation_range=20.,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=[0.9, 1.25],
    brightness_range=[0.5, 1.5],
    horizontal_flip=True,
    validation_split=0.2)

valid_data_gen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)

train_generator = train_data_gen.flow_from_directory(
    r'D:\Data\Binary_Classifaction_using_rembg',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=True,
    subset='training')

validation_generator = valid_data_gen.flow_from_directory(
    r'D:\Data\Binary_Classifaction_using_rembg',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False,
    subset='validation')
# ---------------------------------------------------------------------------

# training the model
history = model.fit(train_generator, epochs=10, validation_data=validation_generator)
