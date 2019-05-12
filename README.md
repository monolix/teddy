<!--
 Copyright (c) 2019 Monolix
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

![logo]

![code-size]

**Teddy** is a lightweight in-code doc generator for Python, based on [Jinja Templates](http://jinja.pocoo.org/).

## Install
To install it, clone the repo and use `setup.py` file.
```bash
git clone https://github.com/monolix/teddy
cd teddy/src
python3 setup.py install
```

## Usage
Let's make a calculator.
```python
def add(a, b):
    return float(a + b)

def sub(a, b):
    return float(a - b)

def mult(a, b):
    return float(a * b)

def div(a, b):
    return float(a / b)
```
That's enough. Client will pay for other features.

Now it needs documentation. Before crying, try using Teddy.
```python
from teddy import Teddy, Section

doc = Teddy("Calculator", "Simple maths calculator.", "Gilfoyle")

ops = Section("Operations", "Operations the calculator can do.")

@ops("Adds two numbers", returns=float)
def add(a, b):
    """>>> add(5, 4) 
9.0"""
    return float(a + b)

@ops("Subtracts two numbers", returns=float)
def sub(a, b):
    """>>> sub(5, 2)
3.0"""
    return float(a - b)

@ops("Multiplies two numbers", returns=float)
def mult(a, b):
    """>>> mult(7, 8)
56.0"""
    return float(a * b)

@ops("Divides two numbers", returns=float)
def div(a, b):
    """>>> mult(8, 4)
2.0"""
    return float(a / b)

doc.add_section(ops)
doc.dump("test.html")
```
After that, run da kode and look at the new generated file:

![example]

It's nicely responsive, thanks to [Water CSS].

> You'll always need to run the code at least once to generate the documentation.

You can use Teddy with Flask, too! Use your imagination.

## Contributing
**Sharing is caring!** If you find some bugs or if you want to change something, everything is under the MIT License, you're free to do that. Just fork the repo and pull request us.

<!-- Assets -->
[logo]: https://i.imgur.com/637dqKWl.png
[code-size]: https://img.shields.io/github/languages/code-size/monolix/teddy.svg?color=success&label=size
[example]: https://i.imgur.com/K6ZIkSpl.png
[Water CSS]: https://github.com/kognise/water.css
