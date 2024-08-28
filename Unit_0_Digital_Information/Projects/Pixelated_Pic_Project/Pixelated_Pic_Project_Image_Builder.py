# ****************************************************************
# *                                                              *
# * AP CSP 2024-2025                                             *
# * MR. SWOTINSKY                                                *
# * PIXELATED PIC PROJECT - IMAGE BUILDER                        *
# * VERSION 1.0 (January 8, 2024)                                * 
# *                                                              *
# * Instructions:                                                *
# *                                                              *
# *(1) Download this file to your 'AP CSP 2023 2024 Directory.   *
# *(2) Use the Python IDLE to open this file.                    *
# *(3) Select Run > Run Module.                                  *
# *(4) Enter the binary representation of your pixelated pic     *
# *(5) Check your 'AP CSP 2023 2024 Directory for a digial       *
# *    image of your pixelated pic.                              *
# *                                                              *
# * NOTE: Each time you run this program a new image with a      *
# *       new name will be generated. (e.g. 'my_pixelated_pic0', *
# *       'my_pixelated_pic1', 'my_pixelated_pic2', etc.)        *
# *                                                              *
# ****************************************************************

# Imports
from PIL import Image 
import os

# Display a banner.  Then, prompt the user to enter the binary representation of a pixelated pic and assign it to the variable, binary_image:
print('****************************************')
print('*                                      *')
print('* PIXELATED PIC PROJECT - FILE BUILDER *')
print('*                                      *')
print('****************************************\n')    

binary_image = input("Enter the binary code for your pixelated pic: ") 

# Generate an empty list to store the binary representations of each pixel:
rgb_vals_in_bin = []

# Truncate off and append the first 24 characters of binary_image to rgb_vals_in_bin: 
def append_pixel():
    global binary_image
    rgb_vals_in_bin.append(binary_image[:24])
    binary_image = binary_image[24:]

# Iterate over binary_image, 24 characters at a time, truncating and appending the first 24 characters of binary_image to rgb_vals_in_bin:
for i in range(len(binary_image)//24):
    append_pixel()

# Create a new 'RGB' image, 8 pixels x 8 pixels, and assign it to the variable, im:
im = Image.new('RGB',(8,8))

# Generate the pixel map for im and assign it to the variable, px:
px = im.load()

# Iterate over all rows and columns of px setting each pixel to its intended RGB value:
for i in range(8):
    for j in range(8):
        rgb_val_in_bin = rgb_vals_in_bin[i + 8 * j]
        red = int(rgb_val_in_bin[:8], base = 2)
        green = int(rgb_val_in_bin[8:16], base = 2)
        blue = int(rgb_val_in_bin[16:], base = 2)
        px[i,j]=(red,green,blue)

# Scale im and its corresponding pixel map by a factor of 50 and assign it to scale_im:
scale_im = Image.new('RGB',(400,400))
scale_px = scale_im.load()
for i in range(400):
    for j in range(400):
        reference_pixel_i_value = (i - i % 50)/50
        reference_pixel_j_value = (j - j % 50)/50
        scale_px[i,j] = px[reference_pixel_i_value, reference_pixel_j_value]        

# Save image as 'my_pixelated_picn.tif".  If the file name already exists, increment n by 1 before saving.  Then, inform the user that a digital image of their pixelated pic has been generated and saved to their AP CSP directory, and thank them for using the pixelated pic project file builder:
pic_index = 0
saved = False
while saved == False:
    file_name = 'my_pixelated_pic' + str(pic_index) + '.tif'
    path = os.getcwd() + '\\' + file_name
    if os.path.isfile(path):
        pic_index += 1
    else:
        scale_im.save(file_name)
        print('\nA digital version of your pixelated pic has been generated and saved to your AP CSP 2023-2024 directory.\n\nThank you for using the pixelated pic project file builder!')
        saved = True
