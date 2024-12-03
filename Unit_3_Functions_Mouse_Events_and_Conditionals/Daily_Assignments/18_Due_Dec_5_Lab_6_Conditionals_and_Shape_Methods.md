Due: Thursday, December 5 2024

Create a new python file in your IDLE titled, `LastNameFirstInitial_U3_Lab6_Conditionals_and_Shape_Methods.py`, and complete the following lab:<br><br>

Your task is to complete this program, which changes the color of the leaves and/or visibility of the ground when the different labels are clicked.<br><br>
<img src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/Lab6.png" width="600px"><br>

Hints: <br>
- You should use the hits(x,y) method
- You need 4 conditionals statements

Challenge: <br>
- Make it so that the Fall and Winter trees have no leaves, only ground.

Starter Code (copy and paste this into your file): <br>

```python
# Import the CMU Graphics package:
from cmu_graphics import *#background
app.background = gradient('deepSkyBlue', 'skyBlue', start='top')

# labels
springLabel = Label('Spring', 10, 320, fill='lightPink', size=30, align='left')
summerLabel = Label('Summer', 10, 360, fill='forestGreen', size=30, align='left')
fallLabel = Label('Fall', 390, 320, fill='darkOrange', size=30, align='right')
winterLabel = Label('Winter', 390, 360, fill='white', size=30, align='right')

#leaves
leaves = Star(200, 150, 150, 16, fill='forestGreen', roundness=90)

# tree trunk and branches
Polygon(200, 100, 150, 400, 250, 400, fill='saddleBrown')
Polygon(200, 300, 200, 250, 300, 175, fill='saddleBrown')
Polygon(200, 300, 200, 250, 100, 150, fill='saddleBrown')
Polygon(200, 200, 200, 175, 125, 100, fill='saddleBrown')
Polygon(200, 250, 200, 200, 275, 100, fill='saddleBrown')

#ground (should only be visible in fall and winter)
ground = Polygon(115, 400, 140, 380, 170, 390, 210, 385, 235, 390, 275, 390,
                 295, 400, visible=False)

def onMousePress(mouseX, mouseY):
    # If a label is clicked, make the color of the leaves match the color of
    # that label. Change the leaves and ground visibility when needed.
    # (HINT: Use the hits(x,y) method to check what label you clicked.)
