# AP Computer Science Principles
Tuesday, October 22nd 2024

### Fills and Borders

**AIM(s):** <br>
How can we customize the colors and borders of rectangles?
What is the difference between parameters and arguments?

**OUTCOME ALIGNMENT**:<br> 
<ins>TYS61XT.4</ins> Code using appropriate syntax.<br> 
<ins>TYS61XT.5</ins> Communicate effectively as a Computer Scientist.<br> 
<ins>TYS61XT.6</ins> Engage in the design thinking process to iteratively develop your work.<br> 

**SUCCESS CRITERIA:**
- [ ] I can describe the difference between parameters and arguments.
- [ ] I can generate an image containing rectangles of different shapes, sizes, and positions on the canvas.

<table>
  <tr>
    <td><b>DO NOW:</b>
    <br> If you DO NOT have your own device, relocate yourself to the center of the room facing the smartboard, and take out your notebook.<br>
    If you DO have your own device, take it out, sign in to your local account, open the Python IDLE, and take out your notebook.<br>
    </td>
    </tr>
</table>

**AGENDA:**

1. Parameters vs. Arguments
2. CMU Graphics Built-in Colors 
3. Revisiting RGB Colors 
4. Fill and Border Code Along
    * Starter Code
      ```python
      # Import the CMU Graphics Package:
      from cmu_graphics import *

      # Run program:
      cmu_graphics.run()
      ```
    * Customizing Fill Color
    * Customizing Border Color
    * Customizing Border Width
5. Practice - CMU Graphics Exercise Set 1.1.5
   
**HOMEWORK:** <br><br>
[Unit 2 Assignment 03](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_2_Intro_to_CMU_Graphics/Daily_Assignments/01_Due_Tue_Oct_22_CMU_Graphics_Exercise_Set_1_1_3.md)<br>
[Unit 2 Assignment 04](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_2_Intro_to_CMU_Graphics/Daily_Assignments/02_Due_Tue_Oct_22_Lab_1_Intro_to_CMU_Graphics.md)

## Resources
|New Code|Description and Details|
|---|---|
|`Rect(left, top, width, height, fill, border, borderWidth)`|The parameters `fill`, `border`, and `borderWidth` can be used to customize rectangles (and other shapes).<br><br>Arguments passed to `fill`, `border`, and `borderWidth` are passed using the **keyword passing technique** meaning they are passed using parameter names.<br><br>The argument passed to `fill` sets the color of the rectangle.<br><br>The argument passed to `border` sets the color of the rectangle's border.<br><br>The argument passed to `borderWidth` sets the width of the rectangle's border.<br><br>Built in colors may be described using their names such as `'midnightBlue'` or `'hotPink'`.  CMU Graphics has a over 100 built-in colors.  **Note:** When using color names, the color names must be surrounded by quotes.<br><br>Other colors may be described using their RGB Triplets such as `rgb(75,15,120)`, a shade of very dark purple, similar, but not identical to, CMU Graphics' `'indigo'` or `rgb(255,180,5)` a shade of bright orange, similar, but not identical to, CMU Graphics' `'orange'`. **Note:** When using RGB triplets, quotes are not required. <br><br>**Example**:<br>`Rect(50, 100, 40, 80, fill = 'navy', border = rgb(185,245,250), borderWidth = 5)` generates a navy rectangle with a light blue border that is 5 pixels wide, as shown below.<br><br><img src = "https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Rectangle_Image.png">|

|Additional Resources|
|---|
|[Parameters vs. Arguments](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/tree/main/Resources)<br><br>[CMU Graphics Built-in Color List (including names and RGB Triplets)](https://academy.cs.cmu.edu/docs/builtInColors)<br><br>[The Google Color Picker](https://www.google.com/search?q=google+color+picker&sca_esv=808cf4c753ad636e&rlz=1C1CHBF_enUS904US904&sxsrf=ADLYWILLYFkuoNVAlQnxJdNxPVMnA-AelA%3A1729365379453&ei=gwUUZ52pG5al5NoPhLWrkAE&ved=0ahUKEwjd9oOJlJuJAxWWElkFHYTaChIQ4dUDCBA&uact=5&oq=google+color+picker&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2dvb2dsZSBjb2xvciBwaWNrZXIyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyDRAAGIAEGLADGEMYigUyDRAAGIAEGLADGEMYigVI6h9QiRBYsR1wAXgBkAEAmAFToAGfAqoBATS4AQPIAQD4AQGYAgWgAtQCwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIFEAAYgATCAgcQIxiwAhgnwgIHEAAYgAQYDZgDAOIDBRIBMSBAiAYBkAYKkgcBNaAHkB0&sclient=gws-wiz-serp)|
