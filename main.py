import os
import time
import functools

import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_hub as hub


def tensor_to_image(tensor):
  
    tensor = np.array(tensor * 255, dtype=np.uint8)
    
    if np.ndim(tensor) > 3:
        # A batch of images. Just take the first one.
        tensor = tensor[0]
        
    return PIL.Image.fromarray(tensor)


def load_image(image_path):
    max_dim = 512
    
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)

    image = tf.image.convert_image_dtype(image, tf.float32)
    

    shape = tf.cast(tf.shape(image)[:-1], tf.float32)
    long_dim = max(shape)
    scale = max_dim / long_dim
    
    new_shape = tf.cast(shape * scale, tf.int32)
    
    image = tf.image.resize(image, new_shape)
    # Add a 'batch' dimension to the start
    image = image[tf.newaxis, :]
    
    return image

# --- Main Program Logic ---

# 1. Define the file paths for your images
content_path = r"C:\Users\alvin\OneDrive\Documents\py scripts\tensorflow\orginal.jpg"
style_path = r"C:\Users\alvin\OneDrive\Documents\py scripts\tensorflow\style_refrence1.jpg"

# 2. Load the content and style images into tensors
content_image = load_image(content_path)
style_image = load_image(style_path)

# 3. Load the pre-trained model from TensorFlow Hub
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# 4. Apply the style transfer model
#    The model expects (content_image, style_image)
stylized_result_tensor = hub_model(tf.constant(content_image), tf.constant(style_image))[0]

# 5. Convert the output tensor back to an image
final_image = tensor_to_image(stylized_result_tensor)

# 6. Display the final image
plt.imshow(final_image)
plt.axis('off') # Hide the axes
plt.show()