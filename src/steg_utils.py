"""
Utility functions for preforming LSB Steganography 
"""
import cv2

def check_embed_extract_input_args(args):
   """Check user embed extract input w helpers."""
   check_embed_input_args(args)


def check_embed_input_args(args):
   """Check user embed input w helpers."""
   __check_img_type(args['cover']) 
   __check_img_type(args['secret'])
   __check_num_bits(int(args['numbits']))


def check_extract_input_args(args):
   """Check user extract input w helpers."""
   __check_img_type(args['cover']) 
   __check_num_bits(int(args['numbits']))


def __check_img_type(img_file_path):
    """Check that img is of type .bmp or bit map """ 
    assert img_file_path.endswith('.bmp'), 'img must be of type .bmp'

def __check_num_bits(bits):
   """Check that number of bits is in range RGB pixel."""
   assert (bits >= 0) and (bits <= 8), 'numbits must be between 0 and 8'

def display_embedded_extracted_imgs(embedded_img,extracted_img, num_bits):
   cv2.imshow(f'Secret Image Extracted from the {num_bits} LSBs of Cover Image',extracted_img)
   cv2.imshow(f'Secret Image Embedded in the {num_bits} LSBs of Cover Image',embedded_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()


def display_extracted_img(extracted_img, num_bits):
   cv2.imshow(f'Secret Image Extracted from the {num_bits} LSBs of Cover Image',extracted_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()


def display_embedded_img(embedded_img, num_bits):
   cv2.imshow(f'Secret Image Embedded in the {num_bits} LSBs of Cover Image',embedded_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

def get_and_check_dimensions( cover_img_shape, secret_img_shape = None):
   """Get img dimensions and ensure they are the same."""
   cheight, cwidth = cover_img_shape
   if(secret_img_shape is None):
      pass
   else:
      sheight, swidth = secret_img_shape
      assert cheight == sheight and  cwidth == swidth, \
             'imgs must have same dimensions'
   return cheight, cwidth


#TODO: rework this method
def get_bit_mask(bits):
   """
   Return integer representing bit mask for n zeroed bits 
   of cover img.
   """
   mask = ''
   for i in range(8):
      if(i< 8-bits):
         mask = mask + '1'
      else:
         mask = mask + '0'
   return int(mask,2)
