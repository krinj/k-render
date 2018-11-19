#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
<Description>
"""
from k_render import K_RENDER_MODE_IMAGE
from k_render.dict_section import DictSection
from k_render.document import Document
from k_render.heading_section import HeadingSection

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

    section = HeadingSection("WTC: Test Report", ["Version 1 test report", "More information"])
    document.add(section)

    section = DictSection("DataSet 1", dict1, 4)
    document.add(section)

    section = DictSection("DataSet 2", dict2, 2)
    document.add(section)

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

