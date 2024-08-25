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

write 2d drawn frames, and then create mp4 from them:

```bash
mkdir _draw_to_2d
bin/main --lang bff_noheads --draw_to_2d _draw_to_2d --num 131044

cd _draw_to_2d
ls -1 *.ppm | sort | awk '{print "file \047" $0 "\047"}' > filelist_auto.txt
ffmpeg -f concat -safe 0 -r 12 -i filelist_auto.txt -c:v libx264 -pix_fmt yuv420p output.mp4  # r is the frame rate
open output.mp4
```

help:

```bash
bin/main flags

     --checkpoint_dir: directory to store checkpoints; default: <no value>
     --clear_interval: interval between clears; default: 2048
     --debug: print execution step by step; default: false
     --draw_to: directory to save 1d-drawn frames to (must exist); default:
     --draw_to_2d: directory to save 2d-drawn frames to (must exist, and num must be a square number); default:
     --fixed_shuffle: deterministic shuffling pattern; default: false
     --grid_width_2d: width of the 2d grid; default: 0
     --initial_program: program to seed the soup with; default: <no value>
     --interaction_pattern: file containing the allowed interactions, with two integers `a b` per line, representing that program `a` is allowed to interact with `b` (in that order).; default:
     --lang: language to run; default:
     --load: load a previous save; default: <no value>
     --log: log file; default: <no value>
     --max_epochs: max epochs; default: <no value>
     --mutation_prob: mutation_prob; default:  0.00024
     --num: number of programs to evolve; default: 131072
     --permute_programs: do not shuffle programs between runs (cyclic interactions); default: true
     --print_interval: interval between prints; default: 64
     --reset_interval: reset interval; default: <no value>
     --run: run a program; default: <no value>
     --run_steps: max number of steps for running a program; default: 32768
     --save_interval: interval between saves; default: 256
     --seed: seed; default: 0
     --stopping_bpb: bits per byte below which to stop execution; default: <no value>
     --zero_init: zero init; default: false
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
