import os
import logging
import glob
import numpy as np
import cv2
from queue import Queue
from threading import Thread
from time import time

from process_image import process_image

class ImgProcessWorker(Thread):
    def __init__(self,queue,dst_path):
        Thread.__init__(self)
        self.queue = queue
        self.new_path = dst_path
    def run(self):
        while True:
            image_path,idx = self.queue.get()
            try:
                process_image(image_path,idx,self.new_path)
            finally:
                self.queue.task_done()



def main():
    ts = time()
    IMAGES_PATH = './miniimagenet_1000/'
    DST_PATH = 'new_miniimagenet'
    new_path = os.path.join(os.getcwd(),DST_PATH)
    if not os.path.exists(new_path):
        os.makedirs(new_path,exist_ok=True)
    NUM_WORKERS = 8
    img_files = []
    queue = Queue()

    file_types = [
        '*.jpg',
        '*.png',
        '*.gif'
    ]

    for file_type in file_types:
        img_files.extend(glob.glob(IMAGES_PATH+file_type))
    for x in range(NUM_WORKERS):
        worker = ImgProcessWorker(queue,new_path)
        worker.daemon = True
        worker.start()
    for ith,img_file in enumerate(img_files):
        queue.put((img_file,ith))
    queue.join()
    elapsed_time = time()-ts
    print("Elapsed Time with Worker:{}".format(elapsed_time))


if __name__ =='__main__':
    main()
