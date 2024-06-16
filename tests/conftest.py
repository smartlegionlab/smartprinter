# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest
from collections import namedtuple

from smartprinter import printers


@pytest.fixture(name='context')
def context():
    context = namedtuple('Context', ('text', 'show', 'color', 'char', ))
    return context(text='Test', show=True, color='red', char='-')


@pytest.fixture(name='base_printer')
def base_printer():
    return printers.BasePrinter()


@pytest.fixture(name='click_printer')
def click_printer():
    return printers.ClickPrinter()


@pytest.fixture(name='pager_printer')
def pager_printer():
    return printers.PagerPrinter()


@pytest.fixture(name='smart_printer')
def smart_printer():
    return printers.SmartPrinter()


@pytest.fixture(name='factory')
def printers_factory():
    return printers.PrintersFactory()
