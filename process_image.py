import os
import numpy as np
from PIL import Image as Image2
import cv2
import glob


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

    gray_img = cv2.imread(image_file,0)
    rgb_image = cv2.imread(image_file)
    red_img = rgb_image[:,:,0]
    green_img = rgb_image[:,:,1]
    blue_img = rgb_image[:,:,2]
    all_black = np.zeros((rgb_image.shape[0],rgb_image.shape[1]))
    red_img = np.stack((red_img,all_black,all_black),axis=2)
    green_img = np.stack( (all_black,green_img,all_black),axis=2)
    blue_img = np.stack( (all_black,all_black,blue_img),axis=2)
    cv2.imwrite(new_path+'_gray_image.jpg',gray_img)
    cv2.imwrite(new_path+'_red_image.jpg',red_img)
    cv2.imwrite(new_path+'_green_image.jpg',green_img)
    cv2.imwrite(new_path+'_blue_image.jpg',blue_img)


def load_images_then_save(src_path,dst_path):
    root_path = os.getcwd()
    new_path = os.path.join(root_path,dst_path)
    if not os.path.exists(new_path):
        os.makedirs(dst_path,exist_ok=True)

    file_types = [
        '*.jpg',
        '*.png',
        '*.gif'
    ]
    img_files = []
    for file_type in file_types:
        img_files.extend(glob.glob(src_path+file_type))


    for ith,img_file in enumerate(img_files):
        dst_path_img = os.path.join(new_path,str(ith))
        process_image(img_file,ith,dst_path_img)
