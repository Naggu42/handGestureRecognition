from tensorflow.keras.layers import Flatten, Activation, Dropout, Convolution2D, Dense, BatchNormalization, MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.optimizers import Adam
import pathlib

# Defines the structure of the model, complies and trains it. Then saves it as "my_mdodel.json"
data_dir = "/Training_data"
data_dir = pathlib.Path(data_dir)

model = Sequential()

model.add(Convolution2D(64, (3, 3),padding='valid',input_shape=(256, 256, 1)))
convout1 = Activation('relu')
model.add(convout1)
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(4, 4)))

model.add(Flatten())

model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(6))
model.add(Activation('softmax'))

optimizer = Adam(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy', 'categorical_accuracy'])

model.summary()

train_dataset = image_dataset_from_directory(data_dir, labels="inferred", label_mode='categorical', color_mode='grayscale')

model.fit(train_dataset, epochs=70, batch_size=32)
model.save("my_model.h5")

