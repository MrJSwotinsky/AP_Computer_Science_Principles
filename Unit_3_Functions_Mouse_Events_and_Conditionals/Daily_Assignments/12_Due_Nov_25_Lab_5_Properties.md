Due: Monday, November 25 2024

Create a new markdown file on GitHub in your AP CSP Portfolio > Labs folder titled, LastNameFirstInitial_U3_Lab5_Properties.md, and complete the following lab:

**For each question, you will run and examine the provided code snippet, before answering questions about them in your markdown file on GitHub**

*[For help formatting your markdown file, click here](https://www.markdownguide.org/cheat-sheet/)*

1.  Copy/paste and run the following starter code into your IDLE.

```python
# Import the CMU Graphics package:
from cmu_graphics import *

Label('Position Properties Tutorial', 200, 20, size=20, bold=True)
Label('Press the mouse to move the rectangles', 200, 45)
Label('Blue rectangle sets the centerX & centerY properties', 200, 65)
Label('Gold rectangle sets the left & top properties', 200, 85)
Label('Red rectangle sets the right & bottom properties', 200, 105)

rect1 = Rect( 50, 150, 150, 100, fill='maroon', opacity=50)
rect2 = Rect(125, 200, 150, 100, fill='navy', opacity=50)
rect3 = Rect(200, 250, 150, 100, fill='gold', opacity=50)

def onMousePress(mouseX, mouseY):
    rect1.right = mouseX
    rect1.bottom = mouseY
    
    rect2.centerX = mouseX
    rect2.centerY = mouseY
    
    rect3.left = mouseX
    rect3.top = mouseY

# Run program:
cmu_graphics.run()
```

**Answer the following questions in your markdown file**<br><br>
a. List all of the `property` names found in the code above <br>
b. In your own words, what do the properties in the `onMousePress()` function body describe?<br>
c. Try out different values for `opacity`. Describe what happens when the opacity of a shape is higher. What happens when the opacity is lower? <br>

2. Copy/paste and run the following starter code into your IDLE.

```python
# Import the CMU Graphics package:
from cmu_graphics import *

Label('Size Properties Tutorial', 200, 20, size=20, bold=True)
Label("Press the mouse to set the rectangle's width and height", 200, 45)

r = Rect(0, 0, 100, 100, fill='blue', opacity=50)

def onMousePress(mouseX, mouseY):
    r.width = mouseX
    r.height = mouseY

# Run program:
cmu_graphics.run()
```

**Answer the following questions in your markdown file**<br><br>
a. Click around the screen. How are the x and y position of the mouse used to affect and size of the rectangle <br>

3. Copy/paste and run the following starter code into your IDLE.

```python
# Import the CMU Graphics package:
from cmu_graphics import *

Label('Border Properties Tutorial', 200, 20, size=20, bold=True)
Label('Press the mouse to change the dashes', 200, 45)

l = Line(50, 50, 350, 350, lineWidth=10)

def onMousePress(x, y):
    l.dashes = True

def onMouseRelease(x, y):
    l.dashes = False

# Run program:
cmu_graphics.run()
```
a. The line becomes dashed, using l.dashes = True. `Dashes` can be either `True`, `False`, or a pair of values `(dashWidth, gapWidth)`, that change how long the dashes are and how far apart they are. Try experimenting with this. What happens when you set l.dashes = (20, 5) in the `onMousePress()` function in the example above? <br>

4. Copy/paste and run the following starter code into your IDLE.

```python
# Import the CMU Graphics package:
from cmu_graphics import *

Label('Changing Properties Demo', 200, 20, size=20, bold=True)
Label('Press the mouse to move the rectangles', 200, 45)

r1 = Rect(150, 200, 50, 50, fill='gold')
r2 = Rect(200, 200, 50, 50, fill='navy')
r3 = Rect(175, 100, 50, 50, fill='green')

def onMousePress(x, y):
   r1.centerX -= 10
   r2.centerX += 10

# Run program:
cmu_graphics.run()
```
a. Click the screen many times. Describe how the line `r1.centerX -= 10` works to affect the position of the gold rectangle. <br>
b. Describe how the line `r2.centerX += 10` works to affect the position of the navy rectangle. <br>
c. Write a line of code that would go inside `onMousePress` to continuously rotate the green rectangle in any direction. Use the += or -= operation. 
d. What direction would += rotate the rectangle in? What direction would -= rotate the rectangle in?


   
