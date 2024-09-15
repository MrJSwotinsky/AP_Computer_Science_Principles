# Unit 0, Project 1: Pixelated Pic Task
Due: Tuesday, September 26th 2024

### In this project you will apply what you have learned about the binary, encoding, and the methods computing devices use for storing and sharing data by generating your own pixelated pic, representing it in binary form, and using a python script to convert the binary version of your pixelated pic to a digital image.

## Part 1 - Generate Your Own Pixelated Pic

1. Sketch an 8 x 8 pixelated pic on the grid provided in class. (To download and print an extra copy of the grid, [click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Pixelated%20Pic%20Sketch.pdf).)
  * For each square, use one color.
  * For your entire pic, use at least 5 different colors.
  * Be creative!
2. Create a new folder in your GitHub repo titled, `Pixelated_Pic_Project` containing a file, titled, `README.md`<br>*Need help creating a new folder or file? [Click Here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/How_To_Create_Folders_and_Files.md)*
3. Scan your pixelated pic sketch into a PDF document titled, `LastNameFirstInitial_Pixelated_Pic_Sketch.pdf`.
4. Upload the PDF of your sketch to your pixelated pic project folder.<br>*Need help uploading a file to GitHub? [Click Here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Resources/How_To_Upload_a_File_to_GitHub.md)*

## Part 2 - Generate a Digitized Version of Your Pixelated Pic

Now that you have created a pixelated pic sketch by hand, your next step is to digitize it!  Follow the steps below to create a digitized version of your pixelated pic sketch:

[Click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Digitized%20Pixelated%20Pic%20Sketch%20Example.pdf) to see an example of what you will be creating.

1. Download [Pixelated Pic Project - Digitized Pixelated Pic Sketch.docx](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Digitized%20Pixelated%20Pic%20Sketch.docx) to your Computer Science portfolio directory on your device.
2. Open `Pixelated Pic Project - Digitized Pixelated Pic Sketch.docx` on your device and type your name and the date in the heading.
3. Digitize the top left pixel of your pixelated pic sketch.  To accomplish this...
   * [Click here](https://www.google.com/search?q=google+color+picker&rlz=1C1CHBF_enUS904US904&oq=google+color+picker&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDI3NzJqMGo5qAIAsAIB&sourceid=chrome&ie=UTF-8) to open the Google Color Picker.
   * Adjust the sliders to best match the color of your top left pixel.
   * Once you are confident that you have matched the color of your top left pixel to the best of your ability, enter the RGB values in the top left box of your `Pixelated Pic Project - Digitized Pixelated Pic Sketch.docx` file.
   * Capture a screenshot of the color from the color picker and copy/paste it in the top left box of your `Pixelated Pic Project - Digitized Pixelated Pic Sketch.docx` file above the RGB values.
   * To adjust the size and position of each pixel, right click the color square, select "Format Picture", select "Crop", and set the following:

     **Picture Position**
     * Width: 0.5"
     * Height: 0.5"
     * Offset X: 0"
     * Offset Y: 0"
     
     **Crop Position**
     * Width: 0.5"
     * Height: 0.5"
    
4. Repeat for all other pixels.
5. Save your file, convert it to a PDF, and upload it to your pixelated pic project folder on GitHub.  Remember to include an appropriate commit message.

## Part 3 - Generate A Bitstring To Represent Each Color

Now that you have digitized your pixelated pic, your next step is to create a grid of pixels in binary form by converting each color to binary!  Follow the steps below to create a grid of pixels in binary form:

[Click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Binary%20Pixels%20Example.pdf) to see an example of what you will be creating.

1. Download [Pixelated Pic Project - Binary Pixels.docx](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Binary%20Pixels.docx) to your Computer Science portfolio directory on your device.
2. Open `Pixelated Pic Project - Binary Pixels.docx` on your device and type your name and the date in the heading.
3. Convert the top left pixel to binary form.  To accomplish this...
    *  Convert the Red value to a byte (i.e. an 8-bit binary bitstring)
    *  Convert the Green value to a byte (i.e. an 8-bit binary bitstring)
    *  Convert the Blue value to a byte (i.e. an 8-bit binary bitstring)
    *  Append the 3 bitstrings together to form a single 24-bit bitstring.
    *  Capture your work using copies of the graphic organizer provided in class. To download and print extra copies of the graphic organizer, [click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Graphic%20Organizer.pdf).  For help using the graphic organizer, [click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20Graphic%20Organizer%20Example.pdf) for an example.
4. Repeat for all other pixels.
5. Save your file, convert it to a PDF, and upload it to your pixelated pic project folder on GitHub.  Remember to include an appropriate commit message.
6. Scan your work into a single document, convert it to an appropriately named PDF, and upload it to your pixelated pic project folder on GitHub.  Remember to include an appropriate commit message.

## Part 4 - Generate A Bitstring To Represent Your Pixelated Pic

Now that you have created a grid of pixels in binary form, your next step is to generate a single bitstring to represent your pixelated pic in binary form!  Follow the steps below to create the binary version of your pixelated pic:

[Click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20BitString%20Example.pdf) to see an example of what you will be creating.

1. Download [Pixelated Pic Project - BitString.docx](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated%20Pic%20Project%20-%20BitString.docx) to your Computer Science portfolio directory on your device.
2. Open `Pixelated Pic Project - BitString.docx` on your device and type your name and the date in the heading.
3. Append all bitstrings together to form one large bitstring.
4. Save your file, convert it to a PDF, and upload it to your pixelated pic project folder on GitHub.  Remember to include an appropriate commit message.


## Part 5 - Generate A Digital Image Of Your Pixelated Pic

Now that you have created a bitstring to represent the binary version of your pixelated pic, your next step is to generate a single bitstring to represent your pixelated pic in binary form!  Follow the steps below to create the binary version of your pixelated pic:

[Click here](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/my_pixelated_pic0_Example.tif) to see an example of what you will be creating.

1. Download [Pixelated_Pic_Project_Image_Builder.py](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles/blob/main/Unit_0_Digital_Information/Projects/Pixelated_Pic_Project/Pixelated_Pic_Project_Image_Builder.py) to the `Python312` directory on your device (As part of device configuration, you created a shortcut to this directory on your desktop.)
2. Run the Pixelated_Pic_Project_Image_Builder python file you just downloaded.
3. When prompted, copy/paste your bitstring and press "Enter".
4. Check your `Python312` directory for a new file titled `my_pixelated_pic0.tif` and open it to see a digital image of the pixelated pic you created!

**What if the image I see is not my pixelated pic?**  If this applies to you, it most likely means you have made an error.  However, there is no need to worry.  First, upload your pixelated pic to your pixelated pic project folder on GitHub.  Then try out the troubleshooting steps below.

* Double check your binary conversions for each color for binary conversion errors.
* Double check your bitstring for copy/paste errors.
* Consult with colleagues to get additional perspective.
* **For each revision attempt**, upload all updates to your pixelated pic project folder on GitHub.  Updated files should include:
    * Your Binary Pixels Grid
    * Your Graphic Organizers
    * Your BitString
    * Your Final Image.
  
