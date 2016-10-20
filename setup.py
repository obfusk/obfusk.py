from setuptools import setup, find_packages
import obfusk

setup(
  name            = "obfusk",
  url             = "https://github.com/obfusk/obfusk.py",
  description     = "functional programming (& other tools)" +
                      " library for python (2+3)",
  version         = obfusk.__version__,
  author          = "Felix C. Stegerman",
  author_email    = "flx@obfusk.net",
  license         = "LGPLv3+",
  classifiers     = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",
    "License :: OSI Approved :: GNU Lesser General Public License" +
      " v3 or later (LGPLv3+)",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
  ],
  keywords        = "functional development tools lazy immutable",
  packages        = find_packages(),
  extras_require  = { "test": ["coverage"] },
)
