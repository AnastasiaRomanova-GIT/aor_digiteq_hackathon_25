import os
import cv2
import numpy as np
import pandas as pd
import argparse
from utils.template_matching import template_matching, create_template_from_labeled_image

def main(show=False):
    # === Path Setup ===
    data_folder = 'data'
    char_data_folder = 'basic'
    labels_file = os.path.join('.', data_folder, char_data_folder, 'labels.csv')
    image_folder = os.path.join('.', data_folder, char_data_folder, 'dataset')
    # save_template_path = './data/template.png'

    # === Load Labels ===
    df = pd.read_csv(labels_file, sep=';')
    df.columns = ['id', 'file_name', 'label', 'x', 'y']

    # === Convert strings to usable Python types ===
    df['label'] = df['label'].apply(eval)
    df['x'] = df['x'].apply(lambda x: int(eval(x)[0]))
    df['y'] = df['y'].apply(lambda x: int(eval(x)[0]))

    # === Generate Template from First Labeled Image ===
    template_row = df.iloc[0]
    emoji, emoji_h, emoji_w = create_template_from_labeled_image(
        template_row,
        image_folder
    )

    # === Process Each Image ===
    for _, row in df.iterrows():
        image_path = os.path.join(image_folder, row["file_name"])
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print(f"Failed to load image: {row['file_name']}")
            continue
        template_matching(row, image_folder, image, emoji, emoji_w, emoji_h, show)


"""
Tne structure is not strictly nessesary, however, it makes passing arguments easier.
It also prevents the code from running when imported as a module.
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Emoji template matching with optional visualization.")
    parser.add_argument('--show', action='store_true', help="Show matched image with rectangle.")
    args = parser.parse_args()

    main(show=args.show)
