# Python wrapper for [Ableton Link][1]

[![Build](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml)
[![PyPI](https://img.shields.io/pypi/v/LinkPython-extern?label=View%20on%20pypi&style=flat-square)](https://pypi.org/project/LinkPython-extern/)

This fork was created to streamline the user experience for installing LinkPython
by uploading pre-built wheels on PyPI. More information about LinkPython
can be found [in their repository][2].

## Python 3.11 support

As of v1.0.1, pybind11 has been updated to 2.10.1+ which means this package has
support for Python 3.11.

## Installation

Distributions are available on PyPI with the [LinkPython-extern][3] package.
Example install command:

```sh
pip install LinkPython-extern
```

## Building from source

If you want to build this package from source, you will need CMake installed.
You however do not need to manually build the project, as setuptools will
handle invoking cmake when you install it with pip. To install directly
from the main branch:

```sh
pip install git+https://github.com/thegamecracks/link-python
```

## License:
This depends on [Link][1] and [pybind11][4]. Please mind the licenses of those libraries and their dependencies.

[1]: https://github.com/ableton/link.git
[2]: https://github.com/gonzaloflirt/link-python
[3]: https://pypi.org/project/LinkPython-extern/
[4]: https://github.com/pybind/pybind11
