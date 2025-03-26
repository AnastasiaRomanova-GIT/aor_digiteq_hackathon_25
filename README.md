# Emoji Detection
 To get started, please download the repository and carefully review the assignment details. You'll find 100 pictures and a CSV file with data labels available for use in developing and testing your application. The data is available in the "data" folder within the repository. For more comprehensive assignment information, refer to the Emo Task assignment.docx document.

 # running the program 
 The script has two possible running modes:

basic with no vsualisation:
```
python main.py
```

 and with visualisation:
 ```
 python main.py --show
```

# description
As the task allows some explorations of the methods, this fork cuts the template from
the first image. It is assumed, that the rest of the emojis are very similar to the
original one. No averaging of the template is performed. The main functionality of the 
program is searchingof the template copies throught the whole data-set provided.
This task is performed with standard functionality of cv2 library.
No custom methods are developed.

Visualisation represents the main idea behind the template matching and is not strict.
It only shows a cartoon, based on the previously found coordinates of the emoji.
