#!/usr/bin/python
# encoding: utf-8

# --                                                            ; {{{1
#
# File        : obfusk/__init__.py
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

See obfusk/*.py for examples.
"""
                                                                # }}}1

__version__       = "0.0.1"
__all__           = "immutable lazy".split()

for _m in __all__: exec("from .%s import *" % _m)
del _m

# vim: set tw=70 sw=2 sts=2 et fdm=marker :
