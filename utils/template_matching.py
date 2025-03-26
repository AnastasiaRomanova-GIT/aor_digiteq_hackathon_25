import cv2
import os
import time

def create_template_from_labeled_image(row, image_folder):
    """
    Create a template by cropping a labeled emoji from the
    first file in the dataset.
    """
    image_path = os.path.join(image_folder, row['file_name'])
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # get the coordinates of the upper left corner of the emoji
    # from the df
    # add height and width to get the lower right corner
    x, y = row['x'], row['y']
    h, w = 50, 50  #emoji size

    template = image[y:y+h, x:x+w]

    return template, h, w

def template_matching(row, image_folder, image, emoji, emoji_w, emoji_h, show):
    """
    Perform template matching on each image in the dataset.
    """
    threshold = 0.95
    # Perform template matching
    result = cv2.matchTemplate(image, emoji, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    x, y = max_loc
    gt_x, gt_y = row['x'], row['y']
    if max_val >= 0.95:
        print(f"{row['file_name']}:\n✅ Found emoji at (x={x}, y={y}), score={max_val:.1f}")
        if abs(x - gt_x) <= 5 and abs(y - gt_y) <= 5:
            print(f"Deviation X: {x - gt_x}, deviation Y: {y - gt_y}\n")
        else:
            print(f"Match found but differs from label ({gt_x}, {gt_y})\n")
        if show:
            visualize_fake_search(row, image_folder, emoji_w, emoji_h, delay=2)
    
    else:
        print(f"{row['file_name']}: ❌ No strong match found. Max score = {max_val:.1f}")


def visualize_fake_search(row, image_folder, emoji_w, emoji_h, delay=1):
    """
    Emulates searchinh. A sliding red rectangle searches for the
    emoji position. When found, the rectangles turns green
    """
    image_path = os.path.join(image_folder, row["file_name"])
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"❌ Failed to load image: {row['file_name']}")
        return

    gt_x, gt_y = row['x'], row['y']
    win_name = f"Searching: {row['file_name']}"

    for y in range(0, image.shape[0] - emoji_h + 1, 50):
        for x in range(0, image.shape[1] - emoji_w + 1, 50):
            vis = cv2.cvtColor(image.copy(), cv2.COLOR_GRAY2BGR)

            # Use red rectangle while searching
            color = (0, 0, 255)
            if y >= gt_y:
                y = gt_y
                if x >= gt_x:
                    # Switch to green rectangle at match
                    color = (0, 255, 0)
                    x = gt_x

            cv2.rectangle(vis, (x, y), (x + emoji_w, y + emoji_h), color, 2)
            cv2.imshow(win_name, vis)
            key = cv2.waitKey(10)

            if color == (0, 255, 0):
                # Match reached: pause for delay then exit
                cv2.waitKey(delay * 500)
                cv2.destroyAllWindows()
                return
