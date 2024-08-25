# OSX INSTALL & RUN NOTES

## Install packages

```bash
brew install llvm
brew install libomp
```

## Makefile updates

Option 1: Update Makefile to point to installed libomp

- Find where lobomp is installed, e.g. `ls /opt/homebrew/Cellar/libomp/18.1.8/lib`
- Update LINK_FLAGS in `Makefile` to point to the libomp library, e.g. `LINK_FLAGS += -L/opt/homebrew/Cellar/libomp/18.1.8/lib -lomp -undefined dynamic_lookup`

Option 2: Link libomp and update Makefile to point to the linked library

- Find where lobomp is installed, e.g. `ls /opt/homebrew/Cellar/libomp/18.1.8/lib`
- Create a Symbolic Link for libomp in a Standard Location: `ln -s /opt/homebrew/Cellar/libomp/18.1.8/lib/libomp.* /opt/homebrew/lib/`
- Update LINK_FLAGS in `Makefile` to point to the libomp library, e.g. `LINK_FLAGS += -L/opt/homebrew/lib/ -lomp -undefined dynamic_lookup`

## Compile and run

```bash
make
bin/main --lang bff_noheads
```

lang options:

```
bff
bff_noheads
bff_noheads_4bit
bff8
bff8_noheads
forth
forthtcopy
forthtrivial
```

## Python file bindings

Set up a virtual environment and install pybind11:

```bash
python3 -m venv venv
. ./venv/bin/activate
pip install pybind11
```

Build with Python bindings:

```bash
make PYTHON=1
python3 cubff.py
```
