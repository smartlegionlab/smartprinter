# smartprinter <sup>v0.4.0</sup>

Cross-platform python library, smart printer for console applications.

---

![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Termux-666?style=flat-square)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartprinter)](https://github.com/smartlegionlab/smartprinter/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartprinter)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartprinter)](https://github.com/smartlegionlab/smartprinter/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/smartlegionlab/smartprinter?style=social)](https://github.com/smartlegionlab/smartprinter/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smartprinter?style=social)](https://github.com/smartlegionlab/smartprinter/network/members)
[![PyPI](https://img.shields.io/pypi/v/smartprinter)](https://pypi.org/project/smartprinter)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartprinter?label=pypi%20downloads)](https://pypi.org/project/smartprinter/)
[![PyPI Downloads](https://static.pepy.tech/badge/smartprinter)](https://pepy.tech/projects/smartprinter)
[![PyPI - Format](https://img.shields.io/pypi/format/smartprinter)](https://pypi.org/project/smartprinter)

---

**smartprinter** - Cross-platform python library, smart printer for console applications.

Has several different objects for displaying to the console or generating a string: 

- Normal output.
- Output with the ability to change the line color .
- Displaying a message inside the pager, with the ability to scroll up and down, exit the pager, and print the message
after being shown in a pager. 
- output with the ability to print a message in the center of the console, regardless of changes in its width,
indented before and after the message, indented with the specified characters.

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/smartperinter/blob/master/DISCLAIMER.md)

---

## Help

### Install and use:

- `pip install -r requirements.txt`
- for tests: `pip install requirements/requirements-dev.txt`
- for test coverage: `pytest --cov --cov-report=html`

### Use:

- `pip3 install smartprinter`

```python
from smartprinter.printers import Printer, PrintersFactory

printer = Printer()
printer.base.echo('Text')
printer.click.echo('Text', show=True, color='green')
printer.smart.echo('Text', show=True, char='*')
printer.pager.echo('Text', show=True)

def_printer = PrintersFactory.get_base()
click_printer = PrintersFactory.get_click()
smart_printer = PrintersFactory.get_smart()
pager = PrintersFactory.get_pager()

```

or 

```python
from smartprinter.printers import Printer

printer = Printer()
Printer.base.echo('Text')
Printer.click.echo('Text', show=True, color='green')
Printer.smart.echo('Text', show=True, char='*')
Printer.pager.echo('Text', show=True)

```

---

## Coverage

![logo](https://github.com/smartlegionlab/smartprinter/raw/master/data/images/smartprinter.png)

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/smartprinter/blob/master/LICENSE)**

Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)