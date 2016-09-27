
"""
Ad-hoc parameter testing, pseudo code and tests
"""

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
        self._grey_image = None

    @property
    def json(self):
        return json.dumps(self._json_data)

    def execute(self):
        self._image = Image.open(self._file_path)
        self._cv_image = cv2.imread(self._file_path, cv2.IMREAD_COLOR)
        # self._grey_image = cv2.cvtColor(self._cv_image, cv2.COLOR_BGR2GRAY)
        self._grey_image = cv2.imread(self._file_path, cv2.IMREAD_GRAYSCALE)

        # self._cv_image = cv2.imread(self._file_path, cv2.IMREAD_GRAYSCALE)
        # plt.hist(self._cv_image.ravel(), 256, [0, 256])
        # plt.show()

        # ypixels, xpixels, bands = self._image.shape
        #
        # # get the size in inches
        # dpi = 72.
        # xinch = xpixels / dpi
        # yinch = ypixels / dpi

        color = ('b', 'g', 'r')
        features = []

        fig, ax = plt.subplots(figsize=(20, 10), dpi=72)

        plt.subplot(221)
        plt.imshow(self._image)

        # GET TWO IMAGES WITH HISTRGRAM DARK AND LIGHT
        # AND FIND A WAY TO DETECT DARK AND LIGHT




        # plt.subplot(221)
        # im = cv2.cvtColor(self._cv_image ,cv2.COLOR_BGR2GRAY)
        # # equalizeHist only works on grayscale
        # image = cv2.equalizeHist(im)
        # image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        # plt.imshow(image)

        plt.subplot(222)
        backtorgb = cv2.cvtColor(self._grey_image, cv2.COLOR_GRAY2RGB)
        plt.imshow(backtorgb)

        plt.subplot(223)
        hist, bins = np.histogram(self._grey_image, 256, [0, 256])
        plt.hist(self._grey_image.ravel(), 256, [0, 256])


        # image_bgr_channels = cv2.split(image)
        image_bgr_channels = cv2.split(self._cv_image)

        for (channel, color) in zip(image_bgr_channels, color):
            # print('channel {0} color {1} '.format(channel, color))

            histr = cv2.calcHist(channel, [0], None, [256], [0, 256])
            features.extend(histr)
            plt.subplot(224)
            plt.plot(histr, color=color)

        plt.xlim([0, 256])
        #
        # print("flattened feature vector size: %d" % (np.array(features).flatten().shape))
        # plt.figure(figsize=(20, 10))
        plt.show()




if __name__ == "__main__":
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/house.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_dark.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_high_contrast.jpg')
    generator = PythonHistrogramAnalysisExtractor('../Resources/crowd.jpg')
    generator.execute()

    generator = PythonHistrogramAnalysisExtractor('../Resources/house.jpg')
    generator.execute()



'''
So what is histogram ? You can consider histogram as a graph or plot, which gives you an overall
idea about the intensity distribution of an image.



'''

