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
        self.dst_path = dst_path
    def run(self):
        while True:
            image_path,idx = self.queue.get()
            try:
                process_image(image_path,idx,dst_path)
            finally:
                self.queue.task_done()




if __name__ '__main__':
    #
    IMAGES_PATH = './miniImagenet'
    multiThread(IMAGES_PATH)
