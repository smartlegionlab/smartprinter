# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from smartprinter.printers import (
    DefaultPrinter,
    ClickPrinter,
    PagerPrinter,
    SmartPrinter
)


def def_print(text=''):
    printer = DefaultPrinter()
    return printer.echo(text)


def click_print(text='', show=True, color=None):
    printer = ClickPrinter()
    return printer.echo(text=text, show=show, color=color)


def pager_print(text='', show=True, color=None):
    printer = PagerPrinter()
    return printer.echo(text=text, show=show, color=color)


def smart_print(text='', char='-', show=True):
    printer = SmartPrinter()
    return printer.echo(text=text, char=char, show=show)
