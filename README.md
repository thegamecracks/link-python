# Python wrapper for [Ableton Link][1]

[![Build](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml)
[![PyPI](https://img.shields.io/pypi/v/LinkPython-extern?label=View%20on%20pypi&style=flat-square)](https://pypi.org/project/LinkPython-extern/)

This fork was created to streamline the user experience for installing LinkPython
by uploading pre-built wheels on PyPI. More information about LinkPython
can be found [in their repository][2].

## Python compatibility

|               | v1.0.0 | v1.0.1 | v1.0.4 | v1.1.0 | main |
|---------------|:------:|:------:|:------:|:------:|:----:|
| CPython 3.6   |   ✅   |   ✅   |   ✅   |  ❌  | ❌   |
| CPython 3.7   |   ✅   |   ✅   |   ✅   |  ✅  | ✅   |
| CPython 3.8   |   ✅   |   ✅   |   ✅   |  ✅  | ✅   |
| CPython 3.9   |   ✅   |   ✅   |   ✅   |  ✅  | ✅   |
| CPython 3.10  |   ✅   |   ✅   |   ✅   |  ✅  | ✅   |
| CPython 3.11  |   ❌   |   ✅   |   ✅   |  ✅  | ✅   |
| CPython 3.12  |   ❌   |   ❌   |   ✅   |  ✅  | ✅   |
| CPython 3.13  |   ❌   |   ❌   |   ❌   |  ✅¹ | ✅¹  |
| CPython 3.14+ |   ❌   |   ❌   |   ❌   |  ❌  | ❌   |

¹ Free-threaded builds of CPython are not yet supported.

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
