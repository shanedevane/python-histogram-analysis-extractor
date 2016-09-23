# -*- coding: utf-8 -*-

import cv2
import os
import json
from PIL import Image, ImageStat, ImageChops, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt


class PythonHistrogramAnalysisExtractor:

    def __init__(self, file_path):
        self._file_path = file_path
        self._json_data = dict()
        self._image = None
        self._cv_image = None

    @property
    def json(self):
        return json.dumps(self._json_data)

    def execute(self):
        self._image = Image.open(self._file_path)
        self._cv_image = cv2.imread(self._file_path, -1)
        # self._cv_image = cv2.imread(self._file_path, cv2.IMREAD_GRAYSCALE)
        # plt.hist(self._cv_image.ravel(), 256, [0, 256])
        # plt.show()

        # color = ('b', 'g', 'r')
        # features = []
        #
        # image_bgr_channels = cv2.split(self._cv_image)
        #
        # for (channel, color) in zip(image_bgr_channels, color):
        #     histr = cv2.calcHist(channel, [0], None, [256], [0, 256])
        #     features.extend(histr)
        #     plt.plot(histr, color=color)
        #     plt.xlim([0, 256])
        #
        # print("flattened feature vector size: %d" % (np.array(features).flatten().shape))
        # plt.show()

        # hist, bins = np.histogram(self._cv_image, 256, [0, 256])
        # plt.hist(self._cv_image.ravel(), 256, [0, 256])
        # plt.show()

        # color = ('b','g','r')
        # for channel,col in enumerate(color):
        #     histr = cv2.calcHist([img],[channel],None,[256],[0,256])
        #     plt.plot(histr,color = col)
        #     plt.xlim([0,256])
        # plt.title('Histogram for color scale picture')
        # plt.show()




if __name__ == "__main__":
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_dark.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_high_contrast.jpg')
    generator = PythonHistrogramAnalysisExtractor('../Resources/crowd.jpg')
    generator.execute()




'''
So what is histogram ? You can consider histogram as a graph or plot, which gives you an overall
idea about the intensity distribution of an image.



'''

