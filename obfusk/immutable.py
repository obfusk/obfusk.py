#!/usr/bin/python
# encoding: utf-8

# --                                                            ; {{{1
#
# File        : obfusk/immutable.py
# Maintainer  : Felix C. Stegerman <flx@obfusk.net>
# Date        : 2016-10-20
#
# Copyright   : Copyright (C) 2016  Felix C. Stegerman
# Version     : v0.0.1
# License     : LGPLv3+
#
# --                                                            ; }}}1

                                                                # {{{1
r"""
Python (2+3) functional programming (& other tools) library

Immutable data tools

Examples
========

Immutable                                                       # {{{2
---------

>>> class X(Immutable):
...   __slots__ = "foo bar baz".split()
>>> class Y(X):
...   args_are_mandatory = True

>>> x = X(foo = 42)
>>> x.foo
42

>>> X(spam = 99)
Traceback (most recent call last):
  ...
TypeError: unknown keys: spam
>>> Y(foo = 42)
Traceback (most recent call last):
  ...
TypeError: missing keys: bar, baz
>>> x.foo = 99
Traceback (most recent call last):
  ...
AttributeError: 'X' object attribute 'foo' is read-only
>>> x.spam = 99
Traceback (most recent call last):
  ...
AttributeError: 'X' object has no attribute 'spam'

>>> x = X(foo = 42, bar = 37); y = x.copy(); z = x.copy(baz = 99)
>>> x == y
True
>>> x != z
True
>>> x.baz is None
True
>>> z.baz == 99
True

>>> x = X(foo = 42, bar = 37)
>>> list(x.iteritems())
[('foo', 42), ('bar', 37), ('baz', None)]
>>> list(x.items())
[('foo', 42), ('bar', 37), ('baz', None)]

>>> x, y = X(foo = "foo"), X(foo = "bar")
>>> x == x
True
>>> x == y
False
>>> x > y
True
>>> x >= y
True
>>> x >= x
True
>>> y < x
True
>>> y <= x
True

>>> repr(X(foo = 42, bar = "hi!"))
"X(foo = 42, bar = 'hi!', baz = None)"


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
>>> isinstance(x, Maybe)
True
>>> isinstance(y, Maybe)
True

                                                                # }}}2


Links
=====

https://en.wikipedia.org/wiki/Immutable_object
"""
                                                                # }}}1

from __future__ import print_function

import sys

__all__ = "Immutable".split()

# === Immutable ===

class Immutable(object):                                        # {{{1
  """immutable base class"""

  __slots__, args_are_mandatory = [], False

  @property
  def ___slots(self):
    return [x for x in self.__slots__ if not x.startswith("_")]

  def __init__(self, data = None, **kw):
    x = data if data is not None else {}; x.update(kw)
    ks = set(x.keys()); ss = set(self.___slots)
    for k in self.___slots:
      if k in x:
        self._Immutable___set(k, x[k]); del x[k]
      else:
        self._Immutable___set(k, None)
    if len(x):
      raise TypeError("unknown keys: {}".format(
        ", ".join(sorted(x.keys())) ))
    if self.args_are_mandatory and ks != ss:
      raise TypeError("missing keys: {}".format(
        ", ".join(sorted(ss - ks)) ))

  def ___set(self, k, v):
    super(Immutable, self).__setattr__(k, v)

  def __setattr__(self, k, v):
    if k in self.___slots:
      raise AttributeError(
        "'{}' object attribute '{}' is read-only".format(
          self.__class__.__name__, k))
    else:
      raise AttributeError(
        "'{}' object has no attribute '{}'".format(
          self.__class__.__name__, k))

  def copy(self, **kw):
    return type(self)(dict(self.iteritems()), **kw)

  def iteritems(self):
    return ((k, getattr(self, k)) for k in self.___slots)

  if sys.version_info.major == 2:
    def items(self): return list(self.iteritems())
  else:
    def items(self): return self.iteritems()

  def __eq__(self, rhs):
    if not isinstance(rhs, type(self)): return NotImplemented
    return dict(self.iteritems()) == dict(rhs.iteritems())

  def __lt__(self, rhs):
    if not isinstance(rhs, type(self)): return NotImplemented
    return sorted(self.iteritems()) < sorted(rhs.iteritems())

  def __le__(self, rhs):
    if not isinstance(rhs, type(self)): return NotImplemented
    return sorted(self.iteritems()) <= sorted(rhs.iteritems())

  def __gt__(self, rhs):
    if not isinstance(rhs, type(self)): return NotImplemented
    return sorted(self.iteritems()) > sorted(rhs.iteritems())

  def __ge__(self, rhs):
    if not isinstance(rhs, type(self)): return NotImplemented
    return sorted(self.iteritems()) >= sorted(rhs.iteritems())

  def __repr__(self):
    return '{}({})'.format(self.__class__.__name__,
      ", ".join( "{} = {}".format(k, repr(v))
                   for (k,v) in self.iteritems() ) )

  def __hash__(self):
    return hash(tuple(self.iteritems()))
                                                                # }}}1

# === END ===

if __name__ == "__main__":
  import doctest
  failures, tests = doctest.testmod(verbose = "-v" in sys.argv[1:])
  sys.exit(0 if failures == 0 else 1)

# vim: set tw=70 sw=2 sts=2 et fdm=marker :
