# LinkPython-extern

[![PyPI](https://img.shields.io/pypi/v/LinkPython-extern?label=View%20on%20pypi&style=flat-square)](https://pypi.org/project/LinkPython-extern/)
[![Build](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/thegamecracks/link-python/actions/workflows/build_wheels.yml)
[![Tests](https://github.com/thegamecracks/link-python/actions/workflows/pytest.yml/badge.svg)](https://github.com/thegamecracks/link-python/actions/workflows/pytest.yml)

A Python wrapper for [Ableton Link], forked from gonzaloflirt's [link-python]
to streamline the user experience with new methods, type stubs, and pre-built
wheels.

```py
from link import Link

link = Link(120)
clock = link.clock()
micros = clock.micros()

state = link.captureAppSessionState()
beat = state.beatAtTime(micros, 4)
phase = state.phaseAtTime(micros, 4)
```

You can see the full API documentation in [`__init__.pyi`], or look at
the [LinkHut.py] example which is equivalent to Ableton Link's
[linkhut] example.

For asyncio usage, consider trying out artfwo's [aalink] project!

## Installation

This project can be installed from PyPI under the [LinkPython-extern] name:

```sh
pip install LinkPython-extern
```

Note that we are *not* the same as [LinkPython], which is a different fork
of link-python by munshkr.

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

## License

This project is written under [Unlicense] but also depends on,
among other libraries, [Ableton Link] and [pybind11].
Please mind the licenses of those libraries and their dependencies.

[Ableton Link]: https://github.com/ableton/link.git
[link-python]: https://github.com/gonzaloflirt/link-python
[`__init__.pyi`]: https://github.com/thegamecracks/link-python/blob/master/src-py/link/__init__.pyi
[LinkHut.py]: https://github.com/thegamecracks/link-python/blob/master/example/LinkHut.py
[linkhut]: https://github.com/Ableton/link/blob/master/examples/linkhut/main.cpp
[aalink]: https://github.com/artfwo/aalink
[LinkPython-extern]: https://pypi.org/project/LinkPython-extern/
[LinkPython]: https://github.com/munshkr/link-python
[Unlicense]: https://github.com/thegamecracks/link-python/blob/master/LICENSE.md
[pybind11]: https://github.com/pybind/pybind11
