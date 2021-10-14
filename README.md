# smartprinter


***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartprinter)](https://github.com/smartlegionlab/smartprinter/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartprinter?label=pypi%20downloads)](https://pypi.org/project/smartprinter/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartprinter)
[![PyPI](https://img.shields.io/pypi/v/smartprinter)](https://pypi.org/project/smartprinter)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartprinter)](https://github.com/smartlegionlab/smartprinter/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartprinter)](https://pypi.org/project/smartprinter)

***

## Short Description:
___smartprinter___ - Cross-platform smart printer for console applications.
***

Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email:&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## Requirements:

- [Python](https://python.org) 3.6+
- [click](https://github.com/pallets/click) 8.0.1
  - `pip3 install click~=8.0.1`
- [smartpasslib](https://github.com/smartlegionlab/smartpasslib) 0.2.5
  - `pip3 install smartpassglib~=0.1.0`
  
***

## Images:

![logo](https://github.com/smartlegionlab/smartprinter/raw/master/data/images/smartprinter.png)

***

## What's new?

### ___smartprinter v0.1.0___

***

## Description:

___smartprinter___ - Cross-platform smart printer for console applications.

Has several different objects for displaying to the console or generating a string: 

- Normal output.
- Output with the ability to change the line color .
- Displaying a message inside the pager, with the ability to scroll up and down, exit the pager, and print the message
after being shown in a pager. 
- output with the ability to print a message in the center of the console, regardless of changes in its width,
indented before and after the message, indented with the specified characters.

***

## Help:

### Install and use:

- `pip3 install -r requirements.txt`
- for tests: `pip3 install requirements/requirements-dev.txt`
- for test coverage: `pytest --cov --cov-report=html`

### Use:

```python
from smartprinter.printers import Printer

printer = Printer()
printer.default.echo('Text')
printer.click.echo('Text', show=True, color='green')
printer.smart.echo('Text', show=True, char='*')
printer.pager.echo('Text', show=True)

def_printer = printer.factory.get_default()
click_printer = printer.factory.get_click()
smart_printer = printer.factory.get_smart()
pager = printer.factory.get_pager()

```

or 

```python
from smartprinter.printers import Printer

printer = Printer()
Printer.default.echo('Text')
Printer.click.echo('Text', show=True, color='green')
Printer.smart.echo('Text', show=True, char='*')
Printer.pager.echo('Text', show=True)

```

***

- Use [click](https://github.com/pallets/click) by [license](https://github.com/pallets/click/blob/main/LICENSE.rst)

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Information:



    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
