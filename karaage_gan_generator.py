# -*- coding: utf-8 -*-
import numpy as np
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array, load_img
from PIL import Image

# Loading model
model_gen = model_from_json(open('./model/karaage_gen_model.json').read())
model_gen.load_weights('./model/karaage_gen_weight.hdf5')
model_gen.summary()

img = img_to_array(load_img('test.jpg', target_size=(10,10)))
img_gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
img_array = img_gray.flatten()
img_array = img_array/255*2-1
img_array = img_array.reshape(1,100)

generated_images = model_gen.predict(img_array)
img = generated_images[0] * 127.5 + 127.5
pil_img = Image.fromarray(np.uint8(img))
pil_img.save('karaage_gen.png')
