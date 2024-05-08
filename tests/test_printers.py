# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import shutil

from smartprinter import printers


class TestBsePrinter:
    def test_echo(self, capsys, base_printer, context):
        msg = base_printer.echo(context.text)
        out: str = capsys.readouterr()[0]
        assert out.rstrip('\n') == context.text and msg == context.text


class TestClickPrinter:
    def test_echo(self, capsys, click_printer, context):
        msg = click_printer.echo(text=context.text, show=context.show, color=context.color)
        out = capsys.readouterr()[0]
        assert msg != context.text and out.rstrip('\n') == context.text


class TestPagerPrinter:
    def test_echo(self, pager_printer, capsys, context):
        msg = pager_printer.echo(text=context.text, show=context.show, color=context.color)
        out = capsys.readouterr()[0]
        assert msg == context.text and out == f'{context.text}\n{context.text}\n'


class TestSmartPrinter:
    def test_echo(self, smart_printer, capsys, context):
        msg = smart_printer.echo(text=context.text, show=context.show, char=context.char)
        out = capsys.readouterr()[0]
        assert msg == out.rstrip('\n')

    def test__term_width(self, smart_printer):
        w = shutil.get_terminal_size()[0]
        assert w == smart_printer._term_width()


class TestPrintersFactory:
    def test_get_default(self, factory):
        assert isinstance(factory.get_base(), printers.BasePrinter)

    def test_get_click(self, factory):
        assert isinstance(factory.get_click(), printers.ClickPrinter)

    def test_get_smart(self, factory):
        assert isinstance(factory.get_smart(), printers.SmartPrinter)

    def test_get_pager(self, factory):
        assert isinstance(factory.get_pager(), printers.PagerPrinter)
