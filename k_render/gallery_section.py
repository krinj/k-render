# -*- coding: utf-8 -*-

"""
Renders a dictionary of key-value pairs.
"""
import cv2
import math
from typing import List

import numpy as np
from gv_tools.util import text, visual
from gv_tools.util.region import Region

from k_render.section import Section

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class GallerySection(Section):
    def __init__(self, title: str, images: List[np.ndarray], n_columns: int = 16):
        self.title: str = title
        self.n_columns: int = n_columns
        self.images: List[np.ndarray] = images

        # Should be common to most sections.
        self.e_pad: int = 24
        self.i_pad: int = 5

        super().__init__()

    def render_as_image(self, width: int=None, section_index: int = 0):
        """ Returns an image. """

        # Create all the elements then work out the height.
        title_height: int = 42

        section_bg = (230, 230, 230) if section_index % 2 == 0 else (240, 240, 240)

        size = (width - ((self.n_columns - 1) * self.i_pad) - 2 * self.e_pad) // self.n_columns
        n_rows = math.ceil(len(self.images) / self.n_columns)

        height = self.e_pad * 2 + title_height + (n_rows * (size + self.i_pad))

        print("Field Rows", n_rows)
        print("Field height", height)

        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        canvas[:, :] = section_bg

        # Draw the title.
        t_region = Region(self.e_pad, width - self.e_pad, self.e_pad, self.e_pad + title_height)
        canvas = text.write_into_region(canvas, self.title, t_region, color=(0, 0, 0), bg_color=None,
                                        font_size=18, h_align=text.ALIGN_LEFT)

        # Draw the data-dict as keys.

        for i, image in enumerate(self.images):

            row = math.floor(i / self.n_columns)
            col = i % self.n_columns

            x = self.e_pad + col * (size + self.i_pad)
            y = t_region.bottom + self.i_pad + row * (size + self.i_pad)
            x_hat = x + size
            y_hat = y + size

            f_region = Region(x, x_hat, y, y_hat)
            crop_image = cv2.resize(image, (size, size))
            canvas = visual.safe_implant_with_region(canvas, crop_image, f_region)

        return canvas
