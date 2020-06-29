import os
import shutil
path = "/home/webroot/ryu/PyTorch-YOLOv3/output"
file_list = os.listdir(path)

filename1 = file_list[0]
filename2 = '1.png'

src = '/home/webroot/ryu/PyTorch-YOLOv3/output/'
dir = '/home/webroot/ryu/static/img/'

shutil.move(src+filename1, dir+filename2)
