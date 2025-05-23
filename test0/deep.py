import keras
import numpy as np
import pandas as pd
import os
from keras.models import load_model
import cv2 as cv2
from PIL import Image
import shutil
import matplotlib.pyplot as plt
import sys
################################################################################################################################
# Load the pre-trained model
model = keras.models.load_model(r'C:/final_models/model1/EfficientNetB0-skin disease-92.10.h5')

# Define the target image size for the model
img_size = (300, 300)

# Define the skin disease classes
classes = ['Acne', 'Eczema', 'psoriasis', 'rosacea', 'vitiligo']

# Preprocess the user-selected image
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize(img_size)
    img = np.array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Validate the user-selected image

def validate_image(path):
    image_path =path
    try:
        img = preprocess_image(image_path)
        preds = model.predict(img)
        pred_class = np.argmax(preds)
        m1= 'Invalid image selected.'
        m2= 'valid image.'
        if pred_class >= len(classes):
            # Image is not a skin disease image
            return m1
        else:
            # Image is a valid skin disease image
            return m2
    except:
        # Handle any errors that occur during image validation
        return 'Invalid image selected.'
def predictor(sdir, csv_path,  model_path, crop_image = False):    
    # read in the csv file
    class_df=pd.read_csv(csv_path)    
    img_height=int(class_df['height'].iloc[0])
    img_width =int(class_df['width'].iloc[0])
    img_size=(img_width, img_height)
    scale=class_df['scale by'].iloc[0] 
    try: 
        s=int(scale)
        s2=1
        s1=0
    except:
        split=scale.split('-')
        s1=float(split[1])
        s2=float(split[0].split('*')[1]) 
        print (s1,s2)
    path_list=[]
    paths=os.listdir(sdir)
    for f in paths:
        path_list.append(os.path.join(sdir,f))
    print ('Model is being loaded')
    model=load_model(model_path)
    image_count=len(path_list)    
    index_list=[] 
    prob_list=[]
    cropped_image_list=[]
    good_image_count=0
    for i in range (image_count):       
        img=cv2.imread(path_list[i])
        if crop_image == True:
            status, img=crop(img)
        else:
            status=True
        if status== True:
            good_image_count +=1
            img=cv2.resize(img, img_size)            
            cropped_image_list.append(img)
            img=img*s2 - s1
            img=np.expand_dims(img, axis=0)
            p= np.squeeze (model.predict(img))           
            index=np.argmax(p)            
            prob=p[index]
            index_list.append(index)
            prob_list.append(prob)
    if good_image_count==1:
        class_name= class_df['class'].iloc[index_list[0]]
        probability= prob_list[0]
        img=cropped_image_list [0] 
        plt.title(class_name, color='blue', fontsize=16)
        plt.axis('off')
        plt.imshow(img)
        return class_name, probability
    elif good_image_count == 0:
        return None, None
    most=0
    for i in range (len(index_list)-1):
        key= index_list[i]
        keycount=0
        for j in range (i+1, len(index_list)):
            nkey= index_list[j]            
            if nkey == key:
                keycount +=1                
        if keycount> most:
            most=keycount
            isave=i             
    best_index=index_list[isave]    
    psum=0
    bestsum=0
    for i in range (len(index_list)):
        psum += prob_list[i]
        if index_list[i]==best_index:
            bestsum += prob_list[i]  
    img= cropped_image_list[isave]/255    
    class_name=class_df['class'].iloc[best_index]
    plt.title(class_name, color='blue', fontsize=16)
    plt.axis('off')
    plt.imshow(img)
    return class_name, bestsum/image_count


def classify1(path):
    store_path=os.path.join('C:/working_dir', 'storage')
    if os.path.isdir(store_path):
        shutil.rmtree(store_path)
        os.mkdir(store_path)
    img_path= path
    img=cv2.imread(img_path,  cv2.IMREAD_REDUCED_COLOR_2)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    file_name=os.path.split(img_path)[1]
    dst_path=os.path.join(store_path, file_name)
    cv2.imwrite(dst_path, img)
    print (os.listdir(store_path))
    csv_path=r'C:/final_models/model1/class_dict (2).csv' # path to class_dict.csv
    model_path=r'C:/final_models/model1/EfficientNetB0-skin disease-92.10.h5' # path to the trained model
    class_name, probability=predictor(store_path, csv_path,  model_path, crop_image = False) # run the classifier
    return {"class_name":class_name,"probability":int(probability * 100)}

def classify2(path):
    store_path=os.path.join('C:/working_dir', 'storage')
    if os.path.isdir(store_path):
        shutil.rmtree(store_path)
        os.mkdir(store_path)
    img_path=path
    img=cv2.imread(img_path,  cv2.IMREAD_REDUCED_COLOR_2)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    file_name=os.path.split(img_path)[1]
    dst_path=os.path.join(store_path, file_name)
    cv2.imwrite(dst_path, img)
    print (os.listdir(store_path))
    csv_path=r'C:/final_models/model2/class_dict (1).csv' # path to class_dict.csv
    model_path=r'C:/final_models/model2/EfficientNetB0-skin disease-94.70.h5' # path to the trained model
    class_name, probability=predictor(store_path, csv_path,  model_path, crop_image = False) # run the classifier
    return {"class_name":class_name,"probability":int(probability * 100)}

def classify3(path):
    store_path=os.path.join('C:/working_dir', 'storage')
    if os.path.isdir(store_path):
        shutil.rmtree(store_path)
        os.mkdir(store_path)
    img_path=path
    img=cv2.imread(img_path,  cv2.IMREAD_REDUCED_COLOR_2)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    file_name=os.path.split(img_path)[1]
    dst_path=os.path.join(store_path, file_name)
    cv2.imwrite(dst_path, img)
    print (os.listdir(store_path))
    csv_path=r'C:/final_models/model3/class_dict (3).csv' # path to class_dict.csv
    model_path=r'C:/final_models/model3/EfficientNetB2-skin disease-95.55.h5' # path to the trained model
    class_name, probability=predictor(store_path, csv_path,  model_path, crop_image = False) # run the classifier
    return {"class_name":class_name,"probability":int(probability * 100)}

def classify4(path):
    store_path=os.path.join('C:/working_dir', 'storage')
    if os.path.isdir(store_path):
        shutil.rmtree(store_path)
        os.mkdir(store_path)
    img_path=path
    img=cv2.imread(img_path,  cv2.IMREAD_REDUCED_COLOR_2)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    file_name=os.path.split(img_path)[1]
    dst_path=os.path.join(store_path, file_name)
    cv2.imwrite(dst_path, img)
    print (os.listdir(store_path))
    csv_path=r'C:/final_models/model4/class_dict (4).csv' # path to class_dict.csv
    model_path=r'C:/final_models/model4/EfficientNetB2-skin disease-92.06.h5' # path to the trained model
    class_name, probability=predictor(store_path, csv_path,  model_path, crop_image = False) # run the classifier
    return {"class_name":class_name,"probability":int(probability * 100)}
def total_output(path):
    if(validate_image(path)=='valid image.'):
        cls1=classify1(path)
        cls2=classify2(path)
        cls3=classify3(path)
        cls4=classify4(path)
        return {"data":[cls1,cls2,cls3,cls4]}
    else:
        return {"data":'invalid image'}




DISEASE_DIC={
'Acne':'Acne',
'Atopic Dermatitis':'Atopic Dermatitis',
'Basal Cell Carcinoma':'Basal Cell Carcinoma',
'Benign Keratosis-like Lesions':'Benign Keratosis',
'Eczema':'Eczema',
'Hair Loss Alopecia and other Hair Diseases':'Hair Loss',
'Herpes':'Herpes',
'Insecets Bite and Sting':'Insecets Bite',
'Nail Fungus and other Nail Disease':'Nail Fungus',
'Pigment Disorder':'Pigment Disorder',
'Systemic Disease':'Systemic Disease',
'Melanocytic Nevi':'Melanocytic Nevi',
'Melanoma':'Melanoma',
'Psoriasis- Lichen Planus':'Psoriasis',
'Vascular Tumors':'Vascular Tumors',
'Warts Molluscum and other Viral Infections':'Warts Molluscum ',
'Seborrheic Dermatitis':'Seborrheic Dermatitis',
'Tinea Ringworm Candidiasis and other Fungal Infections':'Tinea Ringworm ',
'Urticaria Hives':'Urticaria Hives',
'Vasculitis':'Vasculitis',
'Versicolor':'Versicolor',

}