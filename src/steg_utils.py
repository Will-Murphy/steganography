"""
Utility functions for preforming LSB Steganography 
"""

def check_embed_extract_input_args(args):
   """Check user embed extract input w helpers."""
   check_embed_input_args(args)


def check_embed_input_args(args):
   """Check user embed input w helpers."""
   __check_image_type(args['cover']) 
   __check_image_type(args['secret'])
   __check_num_bits(int(args['numbits']))


def check_extract_input_args(args):
   """Check user extract input w helpers."""
   __check_image_type(args['cover']) 
   __check_num_bits(int(args['numbits']))


def __check_image_type(image_file_path):
    """Check that image is of type .bmp or bit map """ 
    assert image_file_path.endswith('.bmp'), 'image must be of type .bmp'

def __check_num_bits(bits):
   """Check that number of bits is in range RGB pixel."""
   assert (bits >= 0) and (bits <= 8), 'numbits must be between 0 and 8'


def get_and_check_dimensions( cover_img_shape, secret_img_shape = None):
   """Get image dimensions and ensure they are the same."""
   cheight, cwidth = cover_img_shape
   if(secret_img_shape is None):
      pass
   else:
      sheight, swidth = secret_img_shape
      assert cheight == sheight and  cwidth == swidth, \
             'Images must have same dimensions'
   return cheight, cwidth


#TODO: rework this method
def get_bit_mask(bits):
   """
   Return integer representing bit mask for n zeroed bits 
   of cover image.
   """
   mask = ''
   for i in range(8):
      if(i< 8-bits):
         mask = mask + '1'
      else:
         mask = mask + '0'
   return int(mask,2)
