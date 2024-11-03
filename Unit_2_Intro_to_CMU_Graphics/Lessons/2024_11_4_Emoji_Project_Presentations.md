# AP Computer Science Principles
Monday, November 4th 2024

### Emoji Project Presentations/Gallery Walk

**AIM(s):** <br>
How can I show off my emoji project? In what ways can I learn from my peers' projects? <br><br>

**OUTCOME ALIGNMENT**:<br> 
<ins>TYS61XT.5</ins> Communicate effectively as a Computer Scientist.<br> 
<ins>TYS61XT.8</ins> Model employability skills such as personal mindset, planning for success, and collaboration.<br> 

**SUCCESS CRITERIA:**
- [ ] I have presented my project to one of my peers.
- [ ] I engaged in the feedback process during the gallery walk.

<table>
  <tr>
    <td>
      <b>DO NOW:</b><br>
      1. Open your project file, and run it. Set up your screen so that both your code and emoji are visible, as follows: <br>
      2. On the handout slip, complete the following sentence: "My emoji represents me because..."<br><br>
      <img src = "https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Gallery_Walk_Setup.png" width="400">
</td>
</tr>
</table>

**AGENDA:**
1. Prepare for the gallery walk (Do Now)
2. Gallery walk
  - You have three post-its. During the gallery walk, leave one post-it on three different projects. They should be:
    - A positive comment (something you liked)
    - A piece of constructive feedback (something to add or change)
    - A question
3. Reflection
  - Discuss the following questions with a peer. Each person should complete their own reflection handout as an exit ticket:
    - What surprised you about a peer’s project?
    - How did feedback help you see your work differently?
    - Did you discover new coding techniques or ideas you want to try? <br><br>
    
**HOMEWORK:**
Put any final touches on your project and complete the reflection section of your project. <br><br>

|Primary Resources|
|---|
|[Parameters vs. Arguments](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/tree/main/Resources)<br><br>[CMU Graphics Built-in Color List (including names and RGB Triplets)](https://academy.cs.cmu.edu/docs/builtInColors)<br><br>[The Google Color Picker](https://www.google.com/search?q=google+color+picker&sca_esv=808cf4c753ad636e&rlz=1C1CHBF_enUS904US904&sxsrf=ADLYWILLYFkuoNVAlQnxJdNxPVMnA-AelA%3A1729365379453&ei=gwUUZ52pG5al5NoPhLWrkAE&ved=0ahUKEwjd9oOJlJuJAxWWElkFHYTaChIQ4dUDCBA&uact=5&oq=google+color+picker&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2dvb2dsZSBjb2xvciBwaWNrZXIyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyDRAAGIAEGLADGEMYigUyDRAAGIAEGLADGEMYigVI6h9QiRBYsR1wAXgBkAEAmAFToAGfAqoBATS4AQPIAQD4AQGYAgWgAtQCwgIKECMYgAQYJxiKBcICCxAAGIAEGJECGIoFwgIFEAAYgATCAgcQIxiwAhgnwgIHEAAYgAQYDZgDAOIDBRIBMSBAiAYBkAYKkgcBNaAHkB0&sclient=gws-wiz-serp)|

|Old Code|Description and Details|
|---|---|
|`Line(x1, y1, x2, y2)`|`Line` is defined by the coordinates of its start and end points <br><br> `lineWidth` determines how thick the line is (MUST BE GREATER THAN 0)<br><br> `dashes` can be set to True to draw a dashed line. <br><br> `arrowStart` and `arrowEnd` can be set to True to draw an arrow head on either end of a line.|
|`Polygon(x1, y1, x2, y2, x3, y3, …)`|Polygons are drawn by providing a list of coordinate pairs, between which lines will be drawn to form a shape. You need a minimum of 3 coordinate pairs to draw a Polygon. |
|`Label(text, centerX, centerY)`|`text` refers to the text you want to display in the label. <br><br>  `size` changes the size of the text to the given number (the default is 12). <br><br>  `font` changes the font of the text; can be any of the following: 'arial', 'monospace', 'cursive', 'caveat', 'cinzel', 'montserrat', 'grenze', 'sacramento', 'orbitron', or 'symbols'.<br><br>  `bold` or `italic` can either be set to True or False. <br><br> Other familiar properties that can be used to customize Labels are `fill`, `border`, `borderWidth` and `rotateAngle` <br><br> For example, the following code produces the following label: <br> `Label('AP CSP', 200,200, size=100, font='monospace',fill=gradient('lightSkyBlue','navy', start='top'), border='blue', bold=True)` <br> <img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Label.png" width="300px">|
|`Oval(centerX, centerY, width, height)`|Unlike rectangles, the first two parameters give us the center coordinates for the oval. <br><br> The `rotateAngle` property can be used to rotate the oval, or any shape (MUST BE BETWEEN 0 AND 360). For example : `Oval(50,50,30,30, rotateAngle=45`)|
|`Circle(centerX, centerY, radius)`|The first two parameters give us the center coordinates for the circle. <br><br>`radius` defines the length of half the circle (MUST BE GREATER THAN 0)|
|`Star(centerX, centerY, radius, points, roundness=none)`| The first two parameters give us the center coordinates for the star. <br><br>`radius` determines how large the star is (MUST BE GREATER THAN 0)<br><br> `points` determines how many points are in the star (MUST BE GREATER THAN 2) <br><br> `roundness` changes how round the star is (MUST BE BETWEEN0 to 100)|
|`gradient(color1, color2, color3, ..., start='center')`|`Gradient` can be used in place of a color for the `fill` parameter. <br><br>For example, in the following code: `Rect(50,50,100,100,fill='blue')`,`'blue'` can be replaced by `gradient('yellow','blue',start='top')` as such: <br><br>`Rect(50,50,100,100,fill=gradient('yellow','blue',start='top'))`<br><br>Gradients need at least 2 colors and can have up to as many colors as you want it to.<br><br>The parameter `start` can be used to customize the gradient.<br><br>The argument passed to `start` can be used to define where the first color begins and then the gradient will proceed linearly or radially across the shape. `start` is set to 'center' by default and can be set to the following values: <br><br> <img src = "https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Gradient_Start_Values.png">|
|`Rect(left, top, width, height, fill, border, borderWidth)`|The parameters `fill`, `border`, and `borderWidth` can be used to customize rectangles (and other shapes).<br><br>Arguments passed to `fill`, `border`, and `borderWidth` are passed using the **keyword passing technique** meaning they are passed using parameter names.<br><br>The argument passed to `fill` sets the color of the rectangle.<br><br>The argument passed to `border` sets the color of the rectangle's border.<br><br>The argument passed to `borderWidth` sets the width of the rectangle's border.<br><br>Built in colors may be described using their names such as `'midnightBlue'` or `'hotPink'`.  CMU Graphics has a over 100 built-in colors.  **Note:** When using color names, the color names must be surrounded by quotes.<br><br>Other colors may be described using their RGB Triplets such as `rgb(75,15,120)`, a shade of very dark purple, similar, but not identical to, CMU Graphics' `'indigo'` or `rgb(255,180,5)` a shade of bright orange, similar, but not identical to, CMU Graphics' `'orange'`. **Note:** When using RGB triplets, quotes are not required. <br><br>**Example**:<br>`Rect(50, 100, 40, 80, fill = 'navy', border = rgb(185,245,250), borderWidth = 5)` generates a navy rectangle with a light blue border that is 5 pixels wide, as shown below.<br><br><img src = "https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Rectangle_Image.png" width=50%>
