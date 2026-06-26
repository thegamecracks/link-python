# Python wrapper for [Ableton Link]

[![Build](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml)
[![PyPI](https://img.shields.io/pypi/v/LinkPython-extern?label=View%20on%20pypi&style=flat-square)](https://pypi.org/project/LinkPython-extern/)

This fork was created to streamline the user experience for installing LinkPython
by uploading pre-built wheels on PyPI. More information about LinkPython
can be found [in their repository].

## Python compatibility

|                | v1.0.0 | v1.0.1 | v1.0.4 | v1.1.0 | v1.2.0 | v1.3.0a1 | main |
|----------------|:------:|:------:|:------:|:------:|:------:|:--------:|:----:|
| CPython 3.6    |  ✅   |  ✅    |  ✅   |  ❌    |  ❌   |    ❌    |  ❌  |
| CPython 3.7    |  ✅   |  ✅    |  ✅   |  ✅    |  ❌   |    ❌    |  ❌  |
| CPython 3.8    |  ✅   |  ✅    |  ✅   |  ✅    |  ✅   |    ❌    |  ❌  |
| CPython 3.9    |  ✅   |  ✅    |  ✅   |  ✅    |  ✅   |    ✅    |  ✅  |
| CPython 3.10   |  ✅   |  ✅    |  ✅   |  ✅    |  ✅   |    ✅    |  ✅  |
| CPython 3.11   |  ❌   |  ✅    |  ✅   |  ✅    |  ✅   |    ✅    |  ✅  |
| CPython 3.12   |  ❌   |  ❌    |  ✅   |  ✅    |  ✅   |    ✅    |  ✅  |
| CPython 3.13\* |  ❌   |  ❌    |  ❌   |  ✅    |  ✅   |    ✅    |  ✅  |
| CPython 3.14   |  ❌   |  ❌    |  ❌   |  ❌    |  ✅   |    ✅    |  ✅  |
| CPython 3.15   |  ❌   |  ❌    |  ❌   |  ❌    |  ❌   |    ❌    |  ❌  |
| CPython 3.16+  |  ❌   |  ❌    |  ❌   |  ❌    |  ❌   |    ❌    |  ❌  |

\* CPython 3.13's experimental free-threading builds are not supported.

## Installation

Distributions are available on PyPI with the [LinkPython-extern] package.
Example install command:

```sh
pip install LinkPython-extern
```

## Building from source

If you want to build this package from source, you will need CMake installed.
You however do not need to manually build the project, as scikit-build-core will
handle invoking cmake when you install it with pip. To install directly
from the main branch:

```sh
pip install git+https://github.com/thegamecracks/link-python
```

If building from the repository directly, make sure to clone all submodules using:

```sh
git clone --recurse-submodules https://github.com/thegamecracks/link-python
# or, if already cloned:
git submodule update --init --recursive
```

## License:
This depends on [Link] and [pybind11]. Please mind the licenses of those libraries and their dependencies.

[Ableton Link]: https://github.com/ableton/link.git
[in their repository]: https://github.com/gonzaloflirt/link-python
[LinkPython-extern]: https://pypi.org/project/LinkPython-extern/
[Link]: https://github.com/ableton/link.git
[pybind11]: https://github.com/pybind/pybind11
