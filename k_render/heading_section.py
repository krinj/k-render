# -*- coding: utf-8 -*-

"""
<Description>
"""
from typing import List

import numpy as np
from gv_tools.util import text
from gv_tools.util.region import Region

from k_render.section import Section

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class HeadingSection(Section):
    def __init__(self, title: str, subtitles: List[str] = None):
        super().__init__()
        self.title = title
        self.subtitles = subtitles
        if self.subtitles is None:
            self.subtitles = []
        self.e_pad = 24
        self.i_pad = 5

    def render_as_image(self, width: int=None, section_index: int = 0):
        """ Returns an image. """

        # Create all the elements then work out the height.
        title_height: int = 56
        subtitle_height: int = 20

        height = self.e_pad * 2 + title_height + len(self.subtitles) * subtitle_height

        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        canvas[:, :] = (255, 255, 255)

        # Draw the title.
        t_region = Region(self.e_pad, width - self.e_pad, self.e_pad, self.e_pad + title_height)
        canvas = text.write_into_region(canvas, self.title, t_region, color=(0, 0, 0),
                                        font_size=42, h_align=text.ALIGN_LEFT)

        for i, subtitle in enumerate(self.subtitles):
            y = t_region.bottom + subtitle_height * i
            s_region = Region(t_region.left, t_region.right, y, y + subtitle_height)
            canvas = text.write_into_region(canvas, subtitle, s_region, color=(70, 70, 70),
                                            font_size=16, h_align=text.ALIGN_LEFT)
        return canvas
