import os
import cv2

def load_emoji_template(row, image_folder):
    """
    Given a row from the DataFrame, load and return the grayscale image.
    """
    image_path = os.path.join(image_folder, row["file_name"])
    emoji = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if emoji is None:
        raise FileNotFoundError(f"Emoji template not found: {path}")

    height, width = emoji.shape 
    return emoji, height, width
