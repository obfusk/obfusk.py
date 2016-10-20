#!/usr/bin/python
# encoding: utf-8

# --                                                            ; {{{1
#
# File        : obfusk/lazy.py
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

Lazy(ness) tools

Examples
========

Lazy List                                                       # {{{2
---------

>>> list(llist(xrange(0, 10, 2)))
[0, 2, 4, 6, 8]
>>> list(llist( n*n for n in itertools.count(0) )[:10])
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list(llist([0], rec = lambda xs: ( x+1 for x in xs ))[:10])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> fibs = llist([0, 1], rec = lambda fibs:
...        ( m+n for m,n in izip(fibs, fibs[1:]) ))
>>> list(fibs[:10])
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> list(fibs[:10:2])
[0, 1, 3, 8, 21]

                                                                # }}}2


Links
=====

https://en.wikipedia.org/wiki/Lazy_evaluation
"""
                                                                # }}}1

from __future__ import print_function

import itertools, sys, threading

if sys.version_info.major == 2:                                 # {{{1
  izip    = itertools.izip
else:
  izip    = zip
  xrange  = range
                                                                # }}}1

__all__ = "llist".split()

# === Lazy List ===

class llist(object):                                            # {{{1
  """Lazy list."""

  class iterator(object):
    __slots__ = "l n".split()

    def __init__(self, l): self.l, self.n = l, 0
    def __iter__(self): return self

    def __next__(self):
      try:
        m = self.n; self.n += 1; return self.l[m]
      except IndexError: raise StopIteration
    next = __next__

  __slots__ = "data it lock".split()

  def __init__(self, it, rec = None):
    """Initialise with iterable; for recursive definitions, rec can be
    passed a lambda that takes the llist and returns an iterable (to
    chain to the first one)."""
    self.data, self.it, self.lock = [], None, threading.RLock()
    self.it = iter(itertools.chain(it, rec(self)) if rec else it)

  def __iter__(self): return type(self).iterator(self)

  def __getitem__(self, k):
    """Item at index or islice."""
    if isinstance(k, slice):
      return itertools.islice(self, k.start, k.stop, k.step)
    elif not isinstance(k, int):
      raise TypeError("llist indices must be integers or slices")
    while k >= len(self.data):
      try:
        if self.it is None:
          raise ValueError("llist: recursion before initialisation")
        with self.lock: self.data.append(next(self.it))
      except StopIteration: break
    return self.data[k]
                                                                # }}}1

# === END ===

if __name__ == "__main__":
  import doctest
  failures, tests = doctest.testmod(verbose = "-v" in sys.argv[1:])
  sys.exit(0 if failures == 0 else 1)

# vim: set tw=70 sw=2 sts=2 et fdm=marker :
