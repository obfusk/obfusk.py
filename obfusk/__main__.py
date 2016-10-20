#!/usr/bin/python
# encoding: utf-8

# --                                                            ; {{{1
#
# File        : obfusk/__main__.py
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

This module runs all tests when called as `python -mobfusk`.
"""
                                                                # }}}1

from __future__ import print_function

import argparse, sys

import obfusk
from obfusk import __version__

def main(*args):                                                # {{{1
  p = _argument_parser(); n = p.parse_args(args)
  import doctest
  tot_f, tot_t = 0, 0
  for m in [obfusk] + [ getattr(obfusk, m) for m in obfusk.__all__ ]:
    if n.verbose: print("Testing module %s ..." % m.__name__)
    failures, tests = doctest.testmod(m, verbose = n.verbose)
    tot_f += failures; tot_t += tests
    if n.verbose: print()
  if n.verbose:
    print("Summary:")
    print("%d passed and %d failed." % (tot_t - tot_f, tot_f))
    if tot_f == 0: print("Test passed.")
    else: print("***Test Failed*** %d failures." % tot_f)
  return 0 if tot_f == 0 else 1
                                                                # }}}1

def _argument_parser():                                         # {{{1
  p = argparse.ArgumentParser(description = "cryptanalysis")
  p.add_argument("--version", action = "version",
                 version = "%(prog)s {}".format(__version__))
  p.add_argument("--verbose", "-v", action = "store_true",
                 help = "run tests verbosely")
  return p
                                                                # }}}1

if __name__ == "__main__":
  sys.exit(main(*sys.argv[1:]))

# vim: set tw=70 sw=2 sts=2 et fdm=marker :
