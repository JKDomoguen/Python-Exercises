import os
import numpy as np
from PIL import Image as Image2
import cv2
import glob
import time


def process_image(image_file,
                  ith,
                  new_path):
    '''
    Process each image to their RGB and gray decomposition
    then save them
    :param: str image_file : directory of the image
    :param: int ith: Index of each image
    :param: str new_path : directory where to save processed files
    :param: str display: Option which processed file to display
    '''

    new_path_img = os.path.join(new_path,str(ith))

    rgb_image = cv2.imread(image_file)
    red_img = rgb_image[:,:,0]
    green_img = rgb_image[:,:,1]
    blue_img = rgb_image[:,:,2]
    gray_img = 0.3*red_img + .59*green_img + 0.11*blue_img
    all_black = np.zeros((rgb_image.shape[0],rgb_image.shape[1]))
    red_img = np.stack((red_img,all_black,all_black),axis=2)
    green_img = np.stack( (all_black,green_img,all_black),axis=2)
    blue_img = np.stack( (all_black,all_black,blue_img),axis=2)
    cv2.imwrite(new_path_img+'_gray_image.jpg',gray_img)
    cv2.imwrite(new_path_img+'_red_image.jpg',red_img)
    cv2.imwrite(new_path_img+'_green_image.jpg',green_img)
    cv2.imwrite(new_path_img+'_blue_image.jpg',blue_img)


def load_images_then_save(img_files,dst_path):
    root_path = os.getcwd()
    new_path = os.path.join(root_path,dst_path)
    if not os.path.exists(new_path):
        os.makedirs(dst_path,exist_ok=True)

    st = time.time()
    for ith,img_file in enumerate(img_files):
        process_image(img_file,ith,new_path)
    elapsed_time = time.time() - st
    print("Elapsed Time Without:{}".format(elapsed_time))



if __name__ == '__main__':
    # img_path = "./miniimagenet_1000/"
    # new_path = "saved_folder_new"
    # start_time = time.time()
    # load_images_then_save(img_path,new_path)
    # elapsed_time = time.time()-start_time
    # print("Elpased Time:{}".format(elapsed_time))
    img_path = './'
