# -*- coding: utf-8 -*-

"""
Renders a dictionary of key-value pairs.
"""

import math
import numpy as np
from gv_tools.util import text
from gv_tools.util.region import Region

from k_render.section import Section

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class StatCardSection(Section):
    def __init__(self, title: str, data: dict, n_columns: int = 2):
        self.title: str = title
        self.n_columns: int = n_columns
        self.data: dict = data

        # Should be common to most sections.
        self.e_pad: int = 24
        self.i_pad: int = 12

        super().__init__()

    def render_as_image(self, width: int=None, section_index: int = 0):
        """ Returns an image. """

        # Create all the elements then work out the height.
        title_height: int = 42
        field_height: int = 120
        label_height: int = 42
        field_size: int = 52
        label_size: int = 16

        section_bg = (230, 230, 230) if section_index % 2 == 0 else (240, 240, 240)

        n_field_rows = math.ceil(len(self.data) / self.n_columns)

        height = self.e_pad * 2 + title_height + (n_field_rows * (field_height + self.i_pad))

        print("Field Rows", n_field_rows)

        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        canvas[:, :] = section_bg

        # Draw the title.
        t_region = Region(self.e_pad, width - self.e_pad, self.e_pad, self.e_pad + title_height)
        canvas = text.write_into_region(canvas, self.title, t_region, color=(0, 0, 0), bg_color=None,
                                        font_size=18, h_align=text.ALIGN_LEFT)

        # Draw the data-dict as keys.

        column_width = math.floor((width - ((self.n_columns - 1) * self.i_pad) - 2 * self.e_pad) / self.n_columns)

        for i, (k, v) in enumerate(self.data.items()):

            row = math.floor(i / self.n_columns)
            col = i % self.n_columns

            x = self.e_pad + col * (column_width + self.i_pad)
            y = t_region.bottom + self.i_pad + row * (field_height + self.i_pad)
            x_hat = x + column_width
            y_hat = y + field_height

            t_region_1 = Region(x, x_hat, y, y_hat - label_height + self.i_pad)
            canvas = text.write_into_region(canvas, f"{v}", t_region_1, color=(0, 0, 0), bg_color=(255, 255, 255),
                                            font_size=field_size, h_align=text.ALIGN_CENTER)
            t_region_2 = Region(x, x_hat, y_hat - label_height, y_hat)
            canvas = text.write_into_region(canvas, f"{k}", t_region_2, color=(150, 150, 150), bg_color=(255, 255, 255),
                                            font_size=label_size, h_align=text.ALIGN_CENTER)

        return canvas
