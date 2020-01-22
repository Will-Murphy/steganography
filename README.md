# Hidden Image Embdedding: #
Embeds a secret photo in the least signifigant bits (LSB) of a cover photo, it then extracts that image. 
The point being to to examine changes in hidden image quality upon extraction and the extent to 
an image is hidden as a factor of the number of LSB bits used, or simply to just to hide sensitive
images in a cover image.

Program returns display window with Secret Image embedded in the {num_bits} LSBs 
of Cover Image as well as a display window Secret Image extracted from the {num_bits} 
LSBs of Cover Image.

**Note:** Photos must be of same dimensions (subject to change) and have .bmp file extension

### Setup: 

   ```pip install opencv-python```

### Usage: 
first cd into  **steganography/src/**

usage: steg_main.py [-h] --cover [COVER] --secret [SECRET] --numbits [NUMBITS]
steg_main.py: error: the following arguments are required: --cover, --secret, --numbits


#### Example Call - will work as is after set up step completed :

   ```python3 steg_main.py --cover images/train_img.bmp --secret images/water_img.bmp --numbits 4```

#### parameters explanation:
- ```--cover  a cover photo of file_type bmp```
- ```--secret  a secret photo file_type bmp```
- ```--numbits  a number 0-8 for # of LSB bits used in embedding```

### Examples 

See **steganography/images_out/** to see examples of the embedded and extracted images. 
