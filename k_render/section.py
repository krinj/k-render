# -*- coding: utf-8 -*-

"""
<Description>
"""


class Section:
    def __init__(self):
        pass

    def render(self, tag: str="image", width: int=800, section_index: int = 0):
        return self.render_as_image(width, section_index)
        pass

    def render_as_image(self, width: int = None, section_index: int = 0):
        pass
