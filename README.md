# Hidden Image Embdedding: #

Program embeds a secret image in specified number of least significant bits (LSB) of a cover image or, conversely, extracts a secret image from a specified number LSBs of a cover image with an embedded secret.

By defualt, provided a cover and secret photo, program will return a display window with a Secret Image embedded in the {num_bits} LSBs of Cover Image, as well as a display window with Secret Image subsequently extracted from the {num_bits} 
LSBs of Cover Image. There are also options which will soley return an embedded image from a cover and secret, or an extracted image from a single cover image(see example calls).

### Notes:
- Image type should be of file type .bmp
- For image embedding, cover image and secret image must be of same dimensions  
-  For image extraction, it is best if the number of LSB bits used to extract is the same as the number of LSB bits used to originally embed the secret image. If it is not know try with bits 1-8 and see which produces clearest image. 

### Setup: 

   ```pip install opencv-python```

### Usage: 
first cd into  **steganography/src/**

default operation is embed and extract (see example calls)
   ```
   usage: steg_main.py [-h] --cover [COVER] --secret [SECRET] --numbits [NUMBITS]
                     [--operation [OPERATION]]

   LSB image hiding and subsequent extraction

   optional arguments:
   -h, --help            show this help message and exit
   --cover [COVER]       a cover photo of file_type bmp to hide secret in
   --secret [SECRET]     a secret photo file_type bmp to hide in cover photo
   --numbits [NUMBITS]   number of least signifigant bits for image hiding &
                           extraction
   --operation [OPERATION]
                           operation types are "EMBED_EXTRACT", "EMBED" or
                           "EXTRACT"
   ```
   #### parameters explanation:
- ```--cover  a cover photo of file_type bmp```
- ```--secret  a secret photo file_type bmp```
- ```--numbits  a number 0-8 for # of LSB bits used in embedding```
- ```--operation type of operation to preform on input```
### Example Calls - will work with provided example images as is after set up step completed :

##### Produce Embedded and Subsequently Extract Image with four bits
   ```python3 steg_main.py --cover ../images/train_img.bmp --secret ../images/water_img.bmp --numbits 4```
##### Produce Embedded Image with four bits
   ```python3 steg_main.py --cover ../images/train_img.bmp --secret ../images/water_img.bmp --numbits 4 --operation EMBED```
##### Produce Extracted Image from one LSB bits of Cover Image
   ```python3 steg_main.py --cover ../images_out/embedded_1.bmp  --numbits 1 --operation EXTRACT```

### Input/Output Examples

See **steganography/images_out/** to see examples of outputted embedded and extracted images with 1 and 7 LSB bits 
See **steganography/Images/** to see the example cover and secret images used as input
