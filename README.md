[]: {{{1

    File        : README.md
    Maintainer  : Felix C. Stegerman <flx@obfusk.net>
    Date        : 2016-10-20

    Copyright   : Copyright (C) 2016  Felix C. Stegerman
    Version     : v0.0.1

[]: }}}1

[![PyPI version](https://badge.fury.io/py/obfusk.svg)](https://badge.fury.io/py/obfusk)
[![Build Status](https://travis-ci.org/obfusk/obfusk.py.png)](https://travis-ci.org/obfusk/obfusk.py)

## Description

obfusk.py - functional programming (& other tools) library for python (2+3)

See `obfusk/*.py` for the code (with examples).

## Examples

```python
>>> # Immutable base class
>>> from obfusk import Immutable
>>> class Maybe(Immutable): pass
>>> class Just(Maybe):
...   __slots__ = "value".split()
...   def __init__(self, value):
...     super(Just, self).__init__(value = value)
>>> class Nothing(Maybe): pass
>>> x, y = Just(42), Nothing()
>>> x
Just(value = 42)
>>> y
Nothing()
>>> x.value
42
```

```python
>>> # lazy list
>>> fibs = llist([0, 1], rec = lambda fibs:
...        ( m+n for m,n in izip(fibs, fibs[1:]) ))
>>> list(fibs[:10])
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

...

## Specs & Docs

```bash
$ python -mobfusk -v                # run tests
$ python -mcoverage run -m obfusk   # test coverage
$ python -mcoverage html            # generate html report
$ pydoc obfusk                      # view docs
```

## TODO

  * proper algebraic data types?
  * ...

## License

LGPLv3+ [1].

## References

[1] GNU Lesser General Public License, version 3
--- https://www.gnu.org/licenses/lgpl-3.0.html

[]: ! ( vim: set tw=70 sw=2 sts=2 et fdm=marker : )
