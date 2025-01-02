# AP Computer Science Principles
Thursday, January 2nd 2025

### Introduction to Groups

**AIM(s):** <br>
How can we leverage groups to manage the complexity of our programs?

**OUTCOME ALIGNMENT**:<br> 
<ins>TYS61XT.2</ins>Apply computational thinking skills to a variety of tasks.<br>
<ins>TYS61XT.3</ins>Code using appropriate programming logic<br>
<ins>TYS61XT.4</ins> Code using appropriate syntax.<br> 


**SUCCESS CRITERIA:**
- [ ] I can construct images using groups.
- [ ] I can modify image properties by modifying group properties (e.g. centerX, centerY, left, top, right, bottom, width, height, rotateAngle, fill, opacity, and visible)

|**DO NOW**|
|---|
|1.  Start a new file in your Python IDLE and save it as `LastNameFirstInitial_Unit5_Lab1_Intro_to_Groups.py`<br><br>2.  Sketch a simple image in your notes containing at least 3 shapes.|

**AGENDA:**
1. Image Quick Share
2. Code Along
    * Construct an image using a group.
    * Modify image properties using group properties.  For example, by clicking / releasing the mouse...
      * Change the position of an image.
      * Move an image (left / right / up / down).
      * Rotate an image.
      * Change the color of an image.
      * Change the opacity of an image.
      * Make an image appear / disappear.
  * Incorporate conditionals.
  * Incorporate buttons.
3. Summary/Close (Think-Pair-Share):
     * In the simplest terms possible, what is a group?
     * Give some examples of group properties we can modify and explain how each will affect each shape in the group.
     * How can we leverage groups to manage the complexity of our programs?

   
**HOMEWORK:** <br>

## Resources

**Definition:** <br><br>
A **group** is a collection of shapes which are treated as a single shape.<br><br>

**CMU Graphics Documentation:** <br>
* [Groups](https://academy.cs.cmu.edu/docs/group)
* [Group Properties and Methods](https://academy.cs.cmu.edu/docs/groupPropertiesAndMethods)
* [Common Group Questions Explained](https://academy.cs.cmu.edu/docs/commonGroupQuestionsExplained)<br><br>

**Code Reference:** <br>
<table>
   <tr>
      <td>
         <b>Code</b>
      </td>
      <td>
         <b>Description</b>
      </td>
   </tr>
   <tr>
      <td>
         <pre>group_name = Group(<br>    shape_1,<br>    shape_2,<br>    shape_3,<br>    etc...<br>)</pre>
      </td>
      <td>
         Creates a group named <code>group_name</code> containing <code>shape_1</code>, <code>shape_3</code>, <code>shape_3</code>, etc.<br><br><b>Example 1/</b>The following code creates the group of shapes that make up the smiley face below.<br><pre>smiley_face = Group(<br>    Circle(200, 200, 100, fill = 'yellow'),<br>    Circle(165, 165, 10, fill = 'black'),<br>    Circle(235, 165, 10, fill = 'black'),<br>    Circle(200, 225, 50, fill = 'black'),<br>    Rect(150, 175, 100, 50, fill = 'yellow')<br>)</pre><p align="center"><img align=center, src="https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/smiley_face.png"> 
      </td>
   </tr>
   <tr>
      <td>
         <pre>group_name.group_property = property_value</pre>
      </td>
      <td>
         Changes <code>group_property</code> of <code>group_name</code> to <code>property_value</code>.<br><br><b>Example 2/</b>The following code changes the 
      </td>
   </tr>
</table>
