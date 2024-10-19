## Parameters vs. Arguments

Imagine the `Rect()` function as a machine that draws rectangles.  This machine has specific input slots: 

* **`left`:**  The x coordinate of the top left corner of the rectangle.
* **`top`:** The y coordinate of the top left corner of the rectangle.
* **`width`:** How wide the rectangle should be.
* **`height`:** How tall the rectangle should be.
* **`fill`:** What color the rectangle should be.
* **`border`:** What color the border of the rectangle should be.
* **`borderWidth`:** How wide the border of the rectangle should be.
<br>etc.

These input slots are called **parameters**. They are like labels that tell the machine what kind of information it needs to work.

When you actually want to draw a rectangle, you give the machine specific values for each slot. These values are called **arguments**.

**In short:**

* **Parameters** are the names of the input slots (`left`, `top`, `width`, `height`,`fill`, `border`, `borderWidth`). They are defined in the function itself.
* **Arguments** are the actual values you provide to the function when you use it (like `200`, `100`, `50`, `50`, `'red'`, `'blue'`, and `2`).

So, `Rect(200, 100, 50, 50, 'red', 'blue', 2)` has seven arguments: `200`, `100`, `50`, `50`, `'red'`, `'blue'`, and `2`.  These arguments correspond to the `left`, `top`, `width`, `height`,`fill`, `border`, and `borderWidth` parameters of the `Rect()` function.
