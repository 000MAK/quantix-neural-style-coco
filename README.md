# Neural Style Transfer

Optimize a generated image to match content and style feature statistics using pretrained VGG19; initial run downloads weights from torchvision.

## Run

Use Python 3.10+ in a virtual environment; install `pip install -r requirements.txt`, then run `python main.py --help` (or see project-specific command below). Dataset files, model weights and outputs are kept locally and ignored by Git.

Training code uses a fixed random seed/split and writes held-out metrics and model artifacts to `outputs/`.
