# -*- coding: utf-8 -*-

"""
<Description>
"""
import os

import cv2
from typing import List

import img2pdf
import numpy as np
from gv_tools.util import visual, text
from gv_tools.util.region import Region

from k_render.section import Section

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class Document:
    def __init__(self):
        self.sections: List[Section] = []
        self.fixed_width: int = 1240
        self.fixed_height: int = 1754
        self.page_padding: int = 64
        self.footer_height: int = 32

        self.footer_text: str = "Test Footer Text"

    def add(self, section: Section):
        self.sections.append(section)

    def render(self, tag="image"):
        """ Join the sections together and produce an output. """
        section_width = self.fixed_width - self.page_padding * 2
        section_height = self.fixed_height - self.page_padding * 2 - self.footer_height

        page_sections = []
        section_list = []

        for i, s in enumerate(self.sections):
            section_image = s.render(tag, section_width, i)
            next_height = sum([image.shape[0] for image in section_list]) + section_image.shape[0]

            if next_height > section_height:
                if len(section_list) == 0:
                    page_sections.append([section_image])
                else:
                    page_sections.append(section_list)
                    section_list = [section_image]
            else:
                section_list.append(section_image)

        # Add any dangling sections.
        if len(section_list) > 0:
            page_sections.append(section_list)

        image_list = []

        for pi, sections in enumerate(page_sections):
            print(pi)
            page_num = pi + 1
            canvas = np.zeros((self.fixed_height, self.fixed_width, 3), dtype=np.uint8)
            canvas[:, :] = (255, 255, 255)

            # Render a page.
            # Stitch the images together.
            y = self.page_padding
            for i, image in enumerate(sections):
                y_hat = y + image.shape[0]
                region = Region(self.page_padding, section_width + self.page_padding, y, y_hat)
                visual.safe_implant_with_region(canvas, image, region)
                y = y_hat

            # Create the footer for this page.
            y = self.fixed_height - self.page_padding - self.footer_height
            f_region = Region(self.page_padding, section_width + self.page_padding, y, y + self.footer_height)
            canvas = text.write_into_region(canvas, self.footer_text, f_region, color=(0, 0, 0), h_align=text.ALIGN_LEFT, font_size=14)
            canvas = text.write_into_region(canvas, f"Page {page_num}", f_region, color=(0, 0, 0), h_align=text.ALIGN_RIGHT, font_size=14)

            image_name = f"test_render_{pi}.png"
            image_list.append(image_name)
            cv2.imwrite(image_name, canvas)

        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(image_list))

        for image_path in image_list:
            os.remove(image_path)
