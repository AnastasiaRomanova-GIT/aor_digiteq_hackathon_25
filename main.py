import numpy
import cv2
import os
import pandas as pd
from utils.image_loader import load_emoji_template

# data paths
data_folder = './data/basic/'
labels_file = data_folder + 'labels.csv'
image_folder = data_folder + 'dataset/'

# read label file and store it in a dataframe
df =  pd.read_csv(labels_file, sep = ';')
df.columns = ['id', 'file_name', 'label', 'x', 'y']

# clean up string-y columns
df['label'] = df['label'].apply(eval)
df['x'] = df['x'].apply(lambda x: int(eval(x)[0]))
df['y'] = df['y'].apply(lambda x: int(eval(x)[0]))

#read images in a loop and store them in a list
#images = []
for _, row in df.iterrows():
    try:
        emoji, emoji_w, emoji_h = load_emoji_template(row, image_folder)
        #images.append(image)
    except FileNotFoundError as e:
        print(e)
        continue

print(df.head(5))