#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
<Description>
"""
import cv2
import os

from k_render import K_RENDER_MODE_IMAGE
from k_render.dict_section import DictSection
from k_render.document import Document
from k_render.gallery_section import GallerySection
from k_render.heading_section import HeadingSection
from k_render.stat_card_section import StatCardSection

__author__ = "Jakrin Juangbhanich"
__copyright__ = "Copyright 2018, GenVis Pty Ltd."
__email__ = "krinj@genvis.co"

if __name__ == "__main__":
    print("Running cmd_render")
    document = Document()

    dict1 = {
        "Stat1": 1934,
        "Stat2": 54326,
        "Stat3": 342654,
        "Stat4": 44565,
        "Stat5": 341,
        "Stat6": 546,
        "Stat7": 1445,
    }

    dict2 = {
        "Stat1": 1934,
        "Stat2": 54326,
        "Stat3": 342654,
        "Stat4": 44565,
        "Stat5": 341,
        "Stat6": 546,
        "Stat7": 1445,
    }

    dict3 = {
        "Faces": 9,
        "Body": 12,
        "Cars": 0,
        "Heat": 0
    }

    section = HeadingSection("WTC: Test Report", ["Version 1 test report", "More information"])
    document.add(section)

    section = DictSection("DataSet 1", dict1, 4)
    document.add(section)

    section = StatCardSection("DataSet 2", dict3, 4)
    document.add(section)

    images = []
    image_files = os.listdir("gallery_images")
    for image_file in image_files:
        image = cv2.imread(f"gallery_images/{image_file}")
        images.append(image)

    section = GallerySection("Gallery", images, 12)
    document.add(section)

    document.add_page_cap()

    section = DictSection("DataSet 3", dict2, 2)
    document.add(section)

    section = DictSection("DataSet 4", dict2, 2)
    document.add(section)

    section = DictSection("DataSet 5", dict2, 2)
    document.add(section)

    section = DictSection("DataSet 6", dict2, 2)
    document.add(section)

    section = DictSection("DataSet 7", dict2, 2)
    document.add(section)

    section = DictSection("DataSet 8", dict2, 2)
    document.add(section)

    section = DictSection("DataSet 9", dict2, 2)
    document.add(section)

    document.render(K_RENDER_MODE_IMAGE)

