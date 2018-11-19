# -*- coding: utf-8 -*-

"""
Renders a dictionary of key-value pairs.
"""

import math
import numpy as np
from k_render.section import Section

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class DictSection(Section):
    def __init__(self, data: dict, n_columns: int = 2):
        self.title: str = "Hello World"
        self.n_columns: int = n_columns
        self.data: dict = data

        # Should be common to most sections.
        self.e_pad: int = 10
        self.i_pad: int = 5

        super().__init__()

    def render_as_image(self, width: int=None):
        """ Returns an image. """

        # Create all the elements then work out the height.
        title_height: int = 16
        field_height: int = 12

        n_field_rows = math.floor(len(self.data) / self.n_columns)
        height = self.e_pad * 2 + title_height + (field_height * (n_field_rows + self.i_pad))

        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        canvas[:, :] = (255, 255, 255)
        return canvas
