"""
Provides main functionality for LSB extracting and embedding .bmp images
"""
import steg_utils


def embed_LSB (cover_img, secret_img, bits):
   """
   Hide 'secret_img' in 'bits' number of least signifigant bits of 
   'cover_img'. Return this 'embedded_img'. 
   """
   height, width = steg_utils.get_and_check_dimensions(cover_img.shape[:2], 
                                                       secret_img.shape[:2])
   bit_mask = steg_utils.get_bit_mask(bits)
   embedded_img = cover_img.copy()
   secret_copy = secret_img.copy() 
   for i in range(height): 
      for j in range(width):
         cover_pixel = embedded_img[i,j]
         secret_pixel = secret_copy[i,j]
         embedded_pixel = [] 
         for k in range(0,3):
               cover_pixel[k] = cover_pixel[k] & bit_mask 
               secret_pixel[k] = secret_pixel[k]>>(8-bits)
               embedded_pixel.append(cover_pixel[k]|secret_pixel[k])
         embedded_img[i,j] = embedded_pixel
   return embedded_img


def extract_LSB (embedded_img, bits ): 
   """
   Extract 'secret_img' from 'bits' number of least signifigant bits of 
   'cover_img'. Return this 'extracted_img'.
   """
   height, width = steg_utils.get_and_check_dimensions( embedded_img.shape[:2])
   extracted_img = embedded_img.copy()
   for i in range(height): 
      for j in range(width):
         extracted_pixel = []
         embedded_pixel = embedded_img[i,j]
         for k in range(0,3):
               extracted_pixel.append(embedded_pixel[k]<<(8-bits))
         extracted_img[i,j] = extracted_pixel
   return extracted_img

