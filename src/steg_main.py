'''
Entry point for embedding and extracting images using 
least significant bits.

see readme for usage details. 
'''
import argparse

import cv2 

import steg_utils as utils, steg_img_operations as steg_img

#TODO: add functionality to resize images with unlike dimensions. 
def main(args):
   if args['operation'] == 'EMBED_EXTRACT':
     utils.check_embed_extract_input_args(args)
     num_bits = int(args['numbits'])
     cover_img = cv2.imread(args['cover'])
     secret_img = cv2.imread(args['secret'])
     assert cover_img is not None and secret_img is not None, \
               'There was a problem reading the image, check file path.'

     embedded_img = steg_img.embed_LSB(cover_img, secret_img, num_bits)
     extracted_img = steg_img.extract_LSB(embedded_img, num_bits)

     cv2.imshow(f'Secret Image Embedded in the {num_bits} LSBs of Cover Image',embedded_img)
     cv2.imshow(f'Secret Image Extracted from the {num_bits} LSBs of Cover Image',extracted_img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

   elif args['operation'] == 'EMBED':
     utils.check_embed_input_args(args)
     num_bits = int(args['numbits'])
     cover_img = cv2.imread(args['cover'])
     secret_img = cv2.imread(args['secret'])
     assert cover_img is not None and secret_img is not None, \
               'There was a problem reading the image, check file path.'

     embedded_img = steg_img.embed_LSB(cover_img, secret_img, num_bits)

     cv2.imshow(f'Secret Image Embedded in the {num_bits} LSBs of Cover Image',embedded_img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
   elif args['operation'] == 'EXTRACT':
     utils.check_extract_input_args(args)
     num_bits = int(args['numbits'])
     cover_img = cv2.imread(args['cover'])
     assert cover_img is not None, \
               'There was a problem reading the image, check file path.'

     extracted_img = steg_img.extract_LSB(cover_img, num_bits)

     cv2.imshow(f'Secret Image Extracted from the {num_bits} LSBs of Cover Image',extracted_img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

   else: 
     print("operation argument must be 'EMBED_EXTRACT', 'EMBED' or 'EXTRACT'")
      

if __name__ == "__main__":
   arg_parser = argparse.ArgumentParser(description='LSB image hiding and subsequent extraction')
   arg_parser.add_argument('--cover', nargs='?', default=None, required=True, 
        help='a cover photo of file_type bmp to hide secret in')
   arg_parser.add_argument('--secret', nargs='?', default=None, required=True, 
        help='a secret photo file_type bmp to hide in cover photo')
   arg_parser.add_argument('--numbits', nargs='?', default=None, required=True, 
        help='number of least signifigant bits for image hiding & extraction')
   arg_parser.add_argument('--operation', nargs='?', default='EMBED_EXTRACT', type=str, required=False, 
        help='operation types are "EMBED_EXTRACT", "EMBED" or "EXTRACT"')
   
    
   args = vars(arg_parser.parse_args())
   print(args)
   main(args)

 

 