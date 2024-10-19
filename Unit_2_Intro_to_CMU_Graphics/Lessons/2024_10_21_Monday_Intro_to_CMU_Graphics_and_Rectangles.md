# AP Computer Science Principles
Monday, October 21st 2024

### Intro to CMU Graphics and Rectangles

**AIM(s):** <br>
In what ways can we leverage CMU Graphics on the web and on our devices to support our learning journies as emerging coders?<br>
What is the CMU Graphics Canvas and how can we display rectangles on it?<br>
What are code comments, and why are they so important?<br>
What does it mean to iteratively develop our work?

**OUTCOME ALIGNMENT**:<br> 
<ins>TYS61XT.4</ins> Code using appropriate syntax.<br> 
<ins>TYS61XT.5</ins> Communicate effectively as a Computer Scientist.<br> 
<ins>TYS61XT.6</ins> Engage in the design thinking process to iteratively develop your work.<br> 

**SUCCESS CRITERIA:**
- [ ] I can access all of the resources I need to code.
    - [ ]   CMU Graphics Lessons
    - [ ]   CMU Graphics Exercises
    - [ ]   Python IDLE with CMU Graphics package installed
- [ ] I can explain what the CMU Graphics Canvas is, as well as how to identify points on the canvas using coordinate pairs.
- [ ] I can describe what `arguments` are and explain what each of the first four arguments of the `Rect()` function represent.
- [ ] I can generate an image containing rectangles of different shapes, sizes, and positions on the canvas.

<table>
  <tr>
    <td><b>DO NOW:</b>
    <br> If you DO NOT have your own device, relocate yourself to the center of the room facing the smartboard, and take out your notebook.<br>
    If you DO have your own device, take it out, sign in to your local account, and take out your notebook.<br>
    </td>
    </tr>
</table>

**AGENDA:**

1. Configuration Task Code Along
2. Introducing the Canvas
3. Code Comments
4. Rectangle Code Along
    * Starter Code
      ```python
      # Import the CMU Graphics Package:
      from cmu_graphics import *

      # Run program:
      cmu_graphics.run()
      ```
    * The firt for arguments of `Rect()`
    * Running our First Program
    * Uploading Our Work
    * The Iterative Development Process
5. Introducing CMU Graphics on the Web
   
**HOMEWORK:** <br><br>
[Unit 2 Assignment 01](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_2_Intro_to_CMU_Graphics/Daily_Assignments/01_Due_Tue_Oct_22_CMU_Graphics_Exercise_Set_1_1_3.md)<br>
[Unit 2 Assignment 02](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_2_Intro_to_CMU_Graphics/Daily_Assignments/02_Due_Tue_Oct_22_Lab_1_Intro_to_CMU_Graphics.md)

## Resources
|New Code|Description and Details|
|---|---|
|`Rect(left, top, width, height)`|This function creates a rectangle on the canvas.<br><br>`Rect()`'s first four parameters are `left`,`top`,`width`, and `height`.<br><br>Arguments passed to `left`,`top`,`width`, and `height` are passed using the positional passing technique meaning they are passed using their position.<br><br>The arguments passed to `left` and `top` set the position of the top left corner of the rectangle.<br><br>The arguments passed to `width` and `height` set the width and height of the rectangle.<br><br>**Example**:<br>`Rect(50, 100, 40, 80)` generates a rectangle that is 40 pixels wide by 80 pixels tall with its top left corner positioned at x = 50, y = 100.<br><br>**Remember:** Coordinate pairs on the canvas are not the same as coordinate pairs on the coordinate plane.<br><br>The point, (0,0) is in the top left corner (not the middle!)<br><br>As x increases you head right.<br><br>As y increases, you head down (not up!).|

|Python IDLE - Getting Started - Quick Reference Guide|
|---|
|**To start coding...** <br>1. Click the `IDLE (Python 3.12 64-bit)` shortcut on the desktop of your device.<br>2. Select File > New File.<br>3. Start Coding!<br><br>**To save files in the correct directory...** <br>1.  Select File > Save As.<br>2. Navigate to AppData > Local > Programs > Python > Python312 > AP CSP Portfolio.<br>3. Create an appropriate name for your file (ending in .py).<br>4. Save!<br><br>**To save images in the correct directory...** <br>1.  Capture a screenshot of the window containing the image.<br>2. Right click and select Save As.<br>2. Navigate to AppData > Local > Programs > Python > Python312 > AP CSP Portfolio.<br>3. Create an appropriate name for your file (ending in .tif).<br>4. Save!<br><br>**To run programs you have previously written...** <br>1.  Click the `AP CSP Portfolio` shortcut on the desktop of your device.<br>2. Open the file you would like to run.<br><br>**A quick note about filenames and version history...** <br>1. As you work, upoad and commit to GitHub frequently.  Every time you commit, GitHub saves a copy of your file at that point in time.  This creates a **version history** of your file.<br>2.  When you commit, write a brief message to describe how your file has been updated.<br>3. **Do not change your filename!** This applies to image files as well.  Changing the file name will interfere with the version history of your file on GitHub.  On your device, the new file will overwrite the old file.  However, as long as you have uploaded and committed the previous version of your file to GitHub, your work will not be lost.|


|Additional Resources|
|---|
|[Python Code Comment Guide](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Python_Code_Comment_Guide.md)<br><br>[CMU Graphics Website](https://academy.cs.cmu.edu/desktop)<br><br>[The CMU Graphics Canvas](https://academy.cs.cmu.edu/docs/canvas)<br><br>[CMU Graphics - Full Documentation](https://academy.cs.cmu.edu/docs)|
