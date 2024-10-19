# Unit 1, Assignment 12: Configuration Tasks
Due: Monday, October 21st 2024

## Download and configure Python.

1. Open your preferred web browser and navigate to https://python.org/downloads.
2. Click the yellow button labeled "Download Python 3.12.5".
3. Navigate to your downloads directory and double click the file you just downloaded (`python-3.12.5-amd64`) to install Python.
   * Select "Install Now".
   * After installation is complete, close the window.
4. In the desktop search bar, type "IDLE", **right click** `IDLE (Python 3.12 64-bit)`, and select "Open File Location".  
5. Right click `IDLE (Python 3.12 64-bit)`, select "Send To", and select "Desktop (Create Shortcut)."
6. Close out all windows.  You now have a desktop shortcut to the Python IDLE.
7. Open your file explorer, and from the top navigation bar select "View" > "Show" > "Hidden "Items".
8. Navigate to This PC > C: > Users > YourUserName > AppData > Local > Programs > Python > Python312.
9. Within this directory, create a new folder titled `AP CSP Portfolio`.
10. Right click your new `AP CSP Portfolio` directory, select "Send To", and select "Desktop (Create Shortcut)."
11. Close out all windows.  You now have a desktop shortcut to your AP CSP Portfolio.  This is the directory that will contain your code files.
    
## Download and install Pillow.

1. In the desktop search bar, type "cmd" to open the command prompt.
2. Enter the command `cd AppData\Local\Programs\Python\Python312\Scripts` to navigate to the directory containing pip.
3. Type the command `pip install Pillow` to download and install the Pillow package.
4. After installation has been completed, close all windows.

## Download and install CMU Graphics.

1. In the desktop search bar, type "cmd" to open the command prompt.
2. Enter the command `cd AppData\Local\Programs\Python\Python312\Scripts` to navigate to the directory containing pip.
3. Type the command `pip install cmu-graphics` to download and install the CMU Graphics package.
4. After installation has been completed, close all windows.

## Run, save, and upload your first CMU Graphics Program.

1. Open `IDLE (Python 3.12 64-bit)` using the desktop shortcut you created.
2. Create a new file titled, `LastNameFirstInitial_My_First_CMU_Graphics_Program.py`
3. Copy/Paste the following code into your new file:
```python
#Impor the CMU Graphics Package:
from cmu_graphics import *

# Display a black square in the center of the canvas:
Rect(100,100,200,200)

# Run program:
cmu_graphics.run()
```
4. Save and run your file.  A new window will open containing an image of a black square.
5. Capture a screenshot of this image, title it `LastNameFirstInitial_My_First_CMU_Graphics_Program.tif' and save it to the AP CSP Portfolio on your desktop.
6. Upload both `LastNameFirstInitial_My_First_CMU_Graphics_Program.py' and `LastNameFirstInitial_My_First_CMU_Graphics_Program.tif' to a new folder in your GitHub portfolio titled, `Labs`

## Rubric

|Outcome|Mastery+|Incomplete|
|---|---|---|
|**Employability Skills**|I have completed all configuration tasks.|I have not yet completed all configuration tasks.|
