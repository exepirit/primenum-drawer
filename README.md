# primenum-drawer

## Installation

    git clone https://github.com/exepirit/primenum-drawer.git
    cd primenum-drawer
    pip install -r requirements.txt

## Usage

    python run.py

Edit `run.py` to change the generation of the image.

    imagegen.generateAnimateXOR(width=1024, height=1024, pixel_size=2, colorK=(0,1,1), n=1, folder="out")

Generating an image with a specified color.

`pixel_size` - scale

`colorK` - color in `RGB/255.0`

`n` - number of images

`folder` - folder in which to put images

    imagegen.generateAnimateColorXOR(width=1024, height=1024, pixel_size=2, n=1, folder="out")

Generating an image with a color based on the pixel position. Options are similar.
