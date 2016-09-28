# -*- coding: utf-8 -*-

"""
Extract information from a photo using the histogram of the photo.
"""

import cv2
import os
import json
from PIL import Image, ImageStat, ImageChops, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
from fractions import Fraction
from decimal import Decimal


class PythonHistrogramAnalysisExtractor:

    def __init__(self, file_path):
        self._file_path = file_path
        self._json_data = list()
        self._image = None
        self._cv_image = None
        self._grey_image = None

        self._grey_hist = None
        self._grey_bins = None

    @property
    def json(self):
        return json.dumps(self._json_data)

    def _detect_exposure_loss(self):
        """
        Hardcoded check of darkest bin and lightest bin
        """
        mean = np.mean(self._grey_hist)
        darkest_bin = self._grey_hist[0]
        lightest_bin = self._grey_hist[255]
        if lightest_bin >= mean:
            self._json_data.append({'over_exposed_loss': True})
        if darkest_bin >= mean:
            self._json_data.append({'under_exposed_loss': True})

    def _calc_weighted_exposure(self):
        """
        Group the bins into 5 groups and compare intensities
        """
        bins0to51_very_dark = 0
        bins52to102_dark = 0
        bins103to152_middle = 0
        bins153to203_middle = 0
        bins204to255_very_light = 0

        for bin_num in range(0, 51):
            bins0to51_very_dark += self._grey_hist[bin_num]
        for bin_num in range(52, 102):
            bins52to102_dark += self._grey_hist[bin_num]
        for bin_num in range(103, 152):
            bins103to152_middle += self._grey_hist[bin_num]
        for bin_num in range(103, 152):
            bins153to203_middle += self._grey_hist[bin_num]
        for bin_num in range(204, 255):
            bins204to255_very_light += self._grey_hist[bin_num]

        # fraction = Fraction(bins0to51_very_dark, bins204to255_very_light)
        # print(fraction.limit_denominator())

        self._json_data.append({
            'very_dark_vs_very_light_ratio': self._ratio(bins0to51_very_dark, bins204to255_very_light)
        })

    def _ratio(self, a, b):
        a = float(a)
        b = float(b)

        if a >= b:
            left = round(a/b, 1)
            right = round(b/b, 1)
        else:
            left = round(a/a, 1)
            right = round(b/a, 1)

        return '{0}:{1}'.format(left, right)


    def execute(self):
        self._image = Image.open(self._file_path)
        self._cv_image = cv2.imread(self._file_path, cv2.IMREAD_COLOR)
        self._grey_image = cv2.imread(self._file_path, cv2.IMREAD_GRAYSCALE)

        color = ('b', 'g', 'r')
        features = []

        fig, ax = plt.subplots(figsize=(20, 10), dpi=72)

        plt.subplot(221)
        plt.imshow(self._image)

        plt.subplot(222)
        backtorgb = cv2.cvtColor(self._grey_image, cv2.COLOR_GRAY2RGB)
        plt.imshow(backtorgb)

        plt.subplot(223)
        self._grey_hist, self._grey_bins = np.histogram(self._grey_image, 256, [0, 256])
        plt.hist(self._grey_image.ravel(), 256, [0, 256])

        self._detect_exposure_loss()
        self._calc_weighted_exposure()

        # plt.subplot(224)
        # im = cv2.cvtColor(self._cv_image ,cv2.COLOR_BGR2GRAY)
        # # equalizeHist only works on grayscale
        # image = cv2.equalizeHist(im)
        # image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        # hist, bins = np.histogram(image, 256, [0, 256])
        # plt.hist(image.ravel(), 256, [0, 256])

        #np.amax(histr)

        # light vs dark intensity

        image_bgr_channels = cv2.split(self._cv_image)
        for (channel, color) in zip(image_bgr_channels, color):
            histr = cv2.calcHist(channel, [0], None, [256], [0, 256])
            features.extend(histr)
            plt.subplot(224)
            plt.plot(histr, color=color)

        plt.xlim([0, 256])
        plt.show()


if __name__ == "__main__":
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/house.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_dark.jpg')
    generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_under.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/pacers_high_contrast.jpg')
    # generator = PythonHistrogramAnalysisExtractor('../Resources/crowd.jpg')
    # generator.execute()

    # generator = PythonHistrogramAnalysisExtractor('../Resources/house.jpg')
    generator.execute()
    print(generator.json)

    # generator = PythonHistrogramAnalysisExtractor('../Resources/tanks.jpg')
    # generator.execute()





