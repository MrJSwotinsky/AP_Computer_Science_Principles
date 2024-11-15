Due: Friday, November 8 2024

Create a new python file in your Physical Device > AP CSP Portfolio folder titled, LastNameFirstInitial_U3_Lab2_Parameters.py, and complete the following lab:

1.  Copy/paste the following starter code into your file.

```python
# Import the CMU Graphics package:
from cmu_graphics import *

Rect(0, 0, 400, 400, fill='honeydew')

def drawDonut(centerX, centerY, donutColor, frostingColor):
    Circle(centerX, centerY, 40, fill=donutColor)
    Star(centerX, centerY, 35, 15, border='white', fill=frostingColor, roundness=90)
    Circle(centerX, centerY, 10, fill='honeydew')

# Run program:
cmu_graphics.run()
```

**Use the open space between `from cmu_graphics import *` and `# Run program:` to complete the rest of this lab**

2. Write a function call for the function provided in the starter code. Run it to make sure it works.

3. Comment out your function call by adding a `#` at the front (do not erase it).
   
4. Write a function, called `drawThreeDonuts(centerX, centerY, donutColor, frostingColor)`, that draws three donuts: one centered at `(centerX , centerY)`, and the other two directly above and below. Hint: use mathematical operations on one of the parameters to position the top and bottom donuts.

5. Write a function call to test your code. Run it to make sure it works. Your code should produce something similar to this:<br>
   <img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Donuts.png" width="200px">
  
6. Use comments code comments to respond to the following prompts.  Remember, code comments start with the `#` symbol and end at the end of the line.

* In your own words describe your approach to question #4.
    * What mathematical operation did you use to position the top donut. Why?
    * What mathematical operation did you use to position the bottom donut. Why?
    * Did your function call work on the first try? If not, what mistake did you make? How did you fix it?
   
