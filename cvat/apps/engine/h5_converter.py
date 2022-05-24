import io
import cv2
import h5py
import numpy as np
from PIL import Image
import os

import time
def converter_webm(filename):

    input_path = os.path.dirname(filename)
    # output_path = input_path.rstrip("/raw")
    output_path = input_path

    '''if filename.endswith(".h5"):
        fn=filename.split(".h5")[0]
        fn=fn.split("/")[-1]
        hdf = h5py.File(filename,'r')
        keys = []
        with h5py.File(filename, 'r') as f:
            f.visit(keys.append)
        keys=keys[2:]
        print(output_path+"/"+fn+'.webM')
        out = cv2.VideoWriter(output_path+"/"+fn+'.webM',cv2.VideoWriter_fourcc(*'vp80'), 10, (3584,1896))
        list_of_array=map(lambda x:hdf[x][:], keys)
        for arr in list(list_of_array):
            img = Image.open(io.BytesIO(arr))
            img_cv2 = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
            imS = cv2.resize(img_cv2, (3584,1896))
            out.write(imS)
            img.close()
        out.release()
        cv2.destroyAllWindows()'''

# filename='.\\input_h5\\2020.08.21_at_11.07.12_camera-mi_244.rrec_0.h5' #'.\\input_h5'
# output_path='.\\output_mp4' #'.\\output_mp4'
# h5_to_webm(filename,output_path)


    if filename.endswith(".h5"):
        fn=filename.split(".h5")[0]
        fn=fn.split("/")[-1]
        hdf = h5py.File(filename,'r')
        keys = []
        with h5py.File(filename, 'r') as f:
            f.visit(keys.append)
        keys=keys[2:]
    

        list_of_array=map(lambda x:hdf[x][:], keys)
        list_of_array_bytesio=[io.BytesIO(x) for x in list_of_array ]

        img = Image.open(list_of_array_bytesio[0])
        img_cv2 = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        h,w,c=img_cv2.shape
        #print("shapeeeeeeeeeeee", h,w,c)

        out = cv2.VideoWriter(output_path+"/"+fn+'.webM',cv2.VideoWriter_fourcc(*'vp80'), 10, (w,h))
        for byte in list_of_array_bytesio:
            startt=time.time()
            img = Image.open(byte)
            img_cv2 = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
            imS = cv2.resize(img_cv2, (w,h))
            out.write(imS)
            img.close()     
            endd=time.time()  
            print("timeperframe", endd-startt)
        out.release()
        cv2.destroyAllWindows()