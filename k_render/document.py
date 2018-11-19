# -*- coding: utf-8 -*-

"""
<Description>
"""
from typing import List

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class Document:
    def __init__(self):
        self.sections: List = []
        self.fixed_width: int = 1240
        self.fixed_height: int = 1754

    def render(self, tag="image"):
        """ Join the sections together and produce an output. """

        pass
