import base64
from django.shortcuts import render
from django.http import HttpResponse 
import tensorflow as tf 
import numpy as np
from keras.preprocessing import image
import io

model = tf.keras.models.load_model(r'C:\Users\HP\Desktop\model_chein_chat')

# chien_chat/views.py


def home(request): 
    imagefile = request.FILES.get('imagefile')
    if imagefile is not None: 
        image_data = imagefile.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        test_image = image.load_img(io.BytesIO(image_data), target_size=(128, 128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        
        if result[0][0] == 0:
            predictions = "chat"
        else:
            predictions = "chien"
        
        return render(request, 'result.html', {'predictions': predictions, 'image_data': encoded_image})
    else: 
        return render(request, 'index.html')
