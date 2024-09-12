# AP Computer Science Principles
Thursday, September 12th 2024

### Overflow and Roundoff Errors

**AIM:** What are overflow and roundoff errors and in what ways do they impact programs?

**OUTCOME ALIGNMENT:**
<br><ins>IEC.TYS61XT.2</ins>: Apply computational thinking skills to a variety of tasks.

**SUCCESS CRITERIA:**
- [ ] I can describe the different types of data that can be represented by a single binary digit.
- [ ] I can determine the number of data points that can be represented given a particular number of bits.
- [ ] I can determine the number of bits required to represent a given number of data points.
- [ ] I can describe what overflow and roundoff errors are, as well as the impact they have on programs.

<table>
  <tr>
    <td><b>DO NOW:</b><br><br>
      <ul>
        <li>Write down the greatest <b>single-digit</b> number you can think of.
        <li>Write down the greatest <b>double-digit</b> number you can think of.
        <li>Write down the greatest <b>triple-digit</b> number you can think of.
        <li>Write a rule that describes how to determine the greatest ___-digit number anyone can think of. 
      </ul>
    </tr>
</table>

**AGENDA:**

1. Greatest ___-Digit Number Rule Share Out
2. What Type of Data Can We Represent with a Single Bit?
3. How Many Data Points Can We Represent with ___ Bits ?
4. How Many Bits Do We Need to Represent ___ Data Points?
5. Overflow Errors
6. Roundoff Errors
7. Check for Understanding

**WHAT TYPE OF DATA CAN WE REPRESENT WITH A SINGLE BIT?** 

Turn-talk-share activity

**HOW MANY DATA POINTS CAN WE REPRESENT WITH ___ BITS?** 

Example 1a/ A school uses bitstrings containing 4-bit sequences to generate student ID's.  How many unique student ID's can be generated?

Example 1b/ To accomodate more student IDs, the school begins using 5-bit sequences to generate student ID's.  Now, how many unique student ID's can be generated?

Example 1c/ How many unique student ID's will can be generated using 6-bit sequences?

Example 1d/ How many uniqe student ID's will be generated using 7-bit sequences?

Example 1e/ How many unique ID's will be generated using 16-bit sequences?

**HOW MANY BITS DO WE NEED TO REPRESENT ___ DATA POINTS?** 

Example 2a/ The IT department for a small business implements a new tech support ticket system.  The new system uses a unique binary sequence to identify each tech support ticket that has been submitted.  The system resets ticket numbers after it reaches 1000 tickets.  What is the minimum number of bits required to support 1000 unique ticket numbers?

Example 2b/ How many more bits would be needed if the system were expected to support 2000 unique ticket numbers?

**OVERFLOW AND ROUNDOFF ERRORS** 

Example 3a/ 3-bit sequences are used to represent data.  For example, 101 represents the number 5.  Will any error occur if the numbers 3 and 4 are added? Why or why not?

Example 3b/ Will any error occur if the numbers 5 and 6 are added? Why or why not?

**HOMEWORK:** <br>
[Unit 0 Assignment 05](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Daily_Assignments/Unit_0_Assignment_05_Due_Thu_Sept_12_AP_Classroom_Practice_02_Overflow_And_Roundoff_Errors.md)
