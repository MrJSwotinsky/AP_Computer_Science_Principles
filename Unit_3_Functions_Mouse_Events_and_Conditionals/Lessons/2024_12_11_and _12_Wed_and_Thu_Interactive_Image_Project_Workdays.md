# AP Computer Science Principles
Wednesday, December 11th 2024

### Interactive Image Project Workdays #2 & #3

**AIM(s):** <br>
How can we finalize a first draft of our Interactive Image Project?

**OUTCOME ALIGNMENT**:<br> 
<ins>TYS61XT.3</ins> Code using appropriate programming logic.<br> 
<ins>TYS61XT.4</ins> Code using appropriate syntax.<br> 
<ins>TYS61XT.5</ins> Communicate effectively as a Computer Scientist.<br> 
<ins>TYS61XT.6</ins> Engage in the design thinking process to iteratively develop your work.<br> 

**SUCCESS CRITERIA:**
- [ ] I have finished the first draft of my interactive image project.

<table>
  <tr>
    <td>
      <b>DO NOW:</b><br>
      1. OPEN YOUR INTERACTIVE IMAGE FOLDER ON GITHUB IN ANOTHER TAB AND LEAVE IT OPEN. <br>
      2. Read this reminder of ALL the things your project should accomplish: <br><br>
      - When you click something/somewhere, something should APPEAR<br>
      - When you release somewhere, something should happen/change<br>
      - When you move OR drag the mouse, something should happen/change<br>
      <br>
      Technically speaking, the way that you accomplish this is with mouse events, a user defined function, a function call, variables, conditionals, etc. 
          
</td>
</tr>
</table>

**AGENDA:**

1. Do Now
2. Your resources: GitHub, CMU Graphics, the people around you, your teachers. 
3. Work time: First draft of <a href='https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_3_Functions_Mouse_Events_and_Conditionals/Projects/Interactive_Image_Project.md'>your project</a>
  - Remember to COMMIT often!
5. Self-evaluation checklist
 
   
**HOMEWORK:** <br><br>
[Interactive Image Project - Due: Friday, December 13th 2024](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_3_Functions_Mouse_Events_and_Conditionals/Projects/Interactive_Image_Project.md)<br><br>
**By the end of tonight, you should have made the following progress:**<br>
* Completed your first draft of your project
* At least 4 commits made to your project code file

|Primary Resources|
|---|
|Truth Table: <br><img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Truth_table.png" width="350px"><br>Conditions:<br><img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Conditions.png" width="300px"><br>[Parameters vs. Arguments](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/tree/main/Resources)<br><br>[CMU Graphics Built-in Color List (including names and RGB Triplets)](https://academy.cs.cmu.edu/docs/builtInColors)<br><br>[The Google Color Picker](https://www.google.com/search?q=google+color+picker&sca_esv=808cf4c753ad636e&rlz=1C1CHBF_enUS904US904&sxsrf=ADLYWILLYFkuoNVAlQnxJdNxPVMnA-AelA%3A1729365379453&ei=gwUUZ52pG5al5NoPhLWrkAE&ved=0ahUKEwjd9oOJlJuJAxWWElkFHYTaChIQ4dUDCBA&uact=5&oq=google+color+picker&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2dvb2dsZSBjb2xvciBwaWNrZXIyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyDRAAGIAEGLADGEMYigUyDRAAGIAEGLADGEMYigVI6h9QiRBYsR1wAXgBkAEAmAFToAGfAqoBATS4AQPIAQD4AQGYAgWgAtQCwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIFEAAYgATCAgcQIxiwAhgnwgIHEAAYgAQYDZgDAOIDBRIBMSBAiAYBkAYKkgcBNaAHkB0&sclient=gws-wiz-serp)|

|New Code|Description and Details|
|---|---|
|Shape functions|To call a function on a shape, you use this format: `variableName.method(parameters)` <br> <br> `.hits(x, y)` Takes in two numbers and returns True if the point (x, y) hits a shape drawn on the canvas. Otherwise, returns False. <br><br> `.hitsShape(shape)` Takes in a shape and returns True if it hits any filled portion of the shape that the method applies to. Otherwise, returns False.|
|Old Code|Description and Details|
|Mouse Events |`onMousePress(x,y)` is a partially user defined function that is triggered when the mouse is pressed. `x` and `y` refer to the x and y position of the mouse when it is clicked. <br><br> `onMouseRelease(x,y)` is a partially user defined function that is triggered when the mouse is released (after being pressed). `x` and `y` refer to the x and y position of the mouse when it is released. <br><br>`onMouseMove(x,y)` is a partially user defined function that is triggered when the mouse is moving on the canvas without being clicked. `x` and `y` refer to the x and y position of the mouse as it moves along the screen. <br><br> `onMouseDrag(x,y)` is a partially user defined function that is triggered when the mouse is pressed down AND moving across the canvas (meaning, being dragged). `x` and `y` refer to the x and y position of the mouse as it is being dragged. <br>|
|`def functionName(parameter1, parameter2, ...):`|A function groups together a sequence of statements that we can run when we want. <br><br> The `def` at the start of the line tells Python that we want to define a function and call it `functionName`. This function takes values known as `parameters` that can be used in the function's code.<br> <img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Functions_Notes.png" width="600px"> <img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Functions_Examples.png" width="600px">|
|`Line(x1, y1, x2, y2)`|`Line` is defined by the coordinates of its start and end points <br><br> `lineWidth` determines how thick the line is (MUST BE GREATER THAN 0)<br><br> `dashes` can be set to True to draw a dashed line. <br><br> `arrowStart` and `arrowEnd` can be set to True to draw an arrow head on either end of a line.|
|`Polygon(x1, y1, x2, y2, x3, y3, …)`|Polygons are drawn by providing a list of coordinate pairs, between which lines will be drawn to form a shape. You need a minimum of 3 coordinate pairs to draw a Polygon. |
|`Label(text, centerX, centerY)`|`text` refers to the text you want to display in the label. <br><br>  `size` changes the size of the text to the given number (the default is 12). <br><br>  `font` changes the font of the text; can be any of the following: 'arial', 'monospace', 'cursive', 'caveat', 'cinzel', 'montserrat', 'grenze', 'sacramento', 'orbitron', or 'symbols'.<br><br>  `bold` or `italic` can either be set to True or False. <br><br> Other familiar properties that can be used to customize Labels are `fill`, `border`, `borderWidth` and `rotateAngle` <br><br> For example, the following code produces the following label: <br> `Label('AP CSP', 200,200, size=100, font='monospace',fill=gradient('lightSkyBlue','navy', start='top'), border='blue', bold=True)` <br> <img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Label.png" width="300px">|
|`Oval(centerX, centerY, width, height)`|Unlike rectangles, the first two parameters give us the center coordinates for the oval. <br><br> The `rotateAngle` property can be used to rotate the oval, or any shape (MUST BE BETWEEN 0 AND 360). For example : `Oval(50,50,30,30, rotateAngle=45`)|
|`Circle(centerX, centerY, radius)`|The first two parameters give us the center coordinates for the circle. <br><br>`radius` defines the length of half the circle (MUST BE GREATER THAN 0)|
|`Star(centerX, centerY, radius, points, roundness=none)`| The first two parameters give us the center coordinates for the star. <br><br>`radius` determines how large the star is (MUST BE GREATER THAN 0)<br><br> `points` determines how many points are in the star (MUST BE GREATER THAN 2) <br><br> `roundness` changes how round the star is (MUST BE BETWEEN0 to 100)|
|`gradient(color1, color2, color3, ..., start='center')`|`Gradient` can be used in place of a color for the `fill` parameter. <br><br>For example, in the following code: `Rect(50,50,100,100,fill='blue')`,`'blue'` can be replaced by `gradient('yellow','blue',start='top')` as such: <br><br>`Rect(50,50,100,100,fill=gradient('yellow','blue',start='top'))`<br><br>Gradients need at least 2 colors and can have up to as many colors as you want it to.<br><br>The parameter `start` can be used to customize the gradient.<br><br>The argument passed to `start` can be used to define where the first color begins and then the gradient will proceed linearly or radially across the shape. `start` is set to 'center' by default and can be set to the following values: <br><br> <img src = "https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Gradient_Start_Values.png">|
|`Rect(left, top, width, height, fill, border, borderWidth)`|The parameters `fill`, `border`, and `borderWidth` can be used to customize rectangles (and other shapes).<br><br>Arguments passed to `fill`, `border`, and `borderWidth` are passed using the **keyword passing technique** meaning they are passed using parameter names.<br><br>The argument passed to `fill` sets the color of the rectangle.<br><br>The argument passed to `border` sets the color of the rectangle's border.<br><br>The argument passed to `borderWidth` sets the width of the rectangle's border.<br><br>Built in colors may be described using their names such as `'midnightBlue'` or `'hotPink'`.  CMU Graphics has a over 100 built-in colors.  **Note:** When using color names, the color names must be surrounded by quotes.<br><br>Other colors may be described using their RGB Triplets such as `rgb(75,15,120)`, a shade of very dark purple, similar, but not identical to, CMU Graphics' `'indigo'` or `rgb(255,180,5)` a shade of bright orange, similar, but not identical to, CMU Graphics' `'orange'`. **Note:** When using RGB triplets, quotes are not required. <br><br>**Example**:<br>`Rect(50, 100, 40, 80, fill = 'navy', border = rgb(185,245,250), borderWidth = 5)` generates a navy rectangle with a light blue border that is 5 pixels wide, as shown below.<br><br><img src = "https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Rectangle_Image.png" width=50%>
