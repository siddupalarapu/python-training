from PIL import Image
import os
#import sys
def imageResizing (filename,compressedfilename):
    input_image_path = filename 
    output_image_path = compressedfilename 
    target_filesize = 1.2 * 1024 * 1024  # Target file size in bytes (1.2 MB)

    # Load the original image
    original_image = Image.open(input_image_path)

    while True:
        # Save the image with the current compression quality
        original_image.save(output_image_path, quality=95)  # Set a high initial quality

        # Check the file size
        filesize = os.path.getsize(output_image_path)
        print (filesize)
        # Break the loop if the file size is less than or equal to the target size
        if filesize <= target_filesize:
            break

        # Reduce image size by 10%
        width, height = original_image.size
        new_width = int(width * 0.9)
        new_height = int(height * 0.9)

        # Resize the image
        original_image = original_image.resize((new_width, new_height))


    print(f"Final image size: {filesize / (1024 * 1024.0):.2f} MB")

imageResizing('testimage.jpg' , 'compressedtestimage.jpg')
