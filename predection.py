import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing import image

IMAGE_SIZE = 224  # Set the desired image size

def load_and_display_image(img_path, image_size):
    # Load the image
    img = image.load_img(img_path, target_size=(image_size, image_size))

    # Convert the image to a numpy array and preprocess it
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values to be between 0 and 1

    return img_array

def predict_image_class(img_path):
    # Load the saved model
    loaded_model = keras.models.load_model('NewModel.h5')
    print("Model loaded successfully.")

    # Load and display the test image
    img_array = load_and_display_image(img_path, IMAGE_SIZE)

    # Make predictions on the image
    predictions = loaded_model.predict(img_array)
    predicted_class_index = np.argmax(predictions)

    # Load the class indices mapping
    class_indices = np.load('class_indices.npy', allow_pickle=True).item()
    predicted_class_name = list(class_indices.keys())[list(class_indices.values()).index(predicted_class_index)]
    print(f"The object is: {predicted_class_name}")

    return predicted_class_name
  

if __name__ == "__main__":
    img_path = 'IMAGE/lap.jpg'  # Replace with the path to your image file
    predicted_class_name = predict_image_class(img_path)

