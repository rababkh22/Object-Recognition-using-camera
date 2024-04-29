import tensorflow as tf
from tensorflow import keras
import os
import numpy as np

base_dir = 'data_objects'   # Size of the images that will be fed into the CNN
IMAGE_SIZE = 224

# Number of images that will be grouped together and passed through the CNN at once
BATCH_SIZE = 64

class Model:
    def __init__(self, base_dir, image_size, batch_size):
        self.base_dir = base_dir
        self.image_size = image_size
        self.batch_size = batch_size
        self.train_generator = None
        self.val_generator = None
        self.class_indices = None  # Added class_indices attribute

    def create_data_generators(self):
        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            validation_split=0.2
        )
        self.train_generator = datagen.flow_from_directory(
            self.base_dir,
            target_size=(self.image_size, self.image_size),
            batch_size=self.batch_size,
            subset='training'
        )
        self.val_generator = datagen.flow_from_directory(
            self.base_dir,
            target_size=(self.image_size, self.image_size),
            batch_size=self.batch_size,
            subset='validation'
        )
        self.class_indices = self.train_generator.class_indices  # Store the class indices

        # Define the shape of the input images as a tuple with dimensions: (width, height, channels).
        # In this case, it is set to (IMAGE_SIZE, IMAGE_SIZE, 3) for images with width and height of IMAGE_SIZE and 3 color channels (RGB).
        IMG_SHAPE = (IMAGE_SIZE, IMAGE_SIZE, 3)

        # Create a base model using the MobileNetV2 architecture
        base_model = tf.keras.applications.MobileNetV2(
            input_shape=IMG_SHAPE,
            include_top=False,
            weights='imagenet'
        )

        base_model.trainable = False
        model = tf.keras.Sequential([
            base_model,
            tf.keras.layers.Conv2D(32, 3, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(len(self.class_indices), activation='softmax')
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(),
            loss='categorical_crossentropy',
            metrics=['accuracy', tf.keras.metrics.Recall()]
        )

        epochs = 10
        history = model.fit(
            self.train_generator,
            epochs=epochs,
            validation_data=self.val_generator
        )

        keras_file = 'NewModel.h5'
        keras.models.save_model(model, keras_file)
        print("Model saved successfully.")

    def load_model(self):
        model = keras.models.load_model('NewModel.h5')
        return model

    def save_class_indices(self):
        np.save('class_indices.npy', self.class_indices)  # Save the class indices to 'class_indices.npy'
        print("Class indices saved successfully.")

    def load_class_indices(self):
        self.class_indices = np.load('class_indices.npy', allow_pickle=True).item()  # Load the class indices from 'class_indices.npy'
        print("Class indices loaded successfully.")

def main():
    trainer = Model(base_dir, IMAGE_SIZE, BATCH_SIZE)
    trainer.create_data_generators()

    # Save the class indices
    trainer.save_class_indices()

    # Load the saved model
    loaded_model = trainer.load_model()
    print("Model loaded successfully.")

    # Load the class indices
    trainer.load_class_indices()
    print("Class indices loaded successfully.")

if __name__ == "__main__":
    main()