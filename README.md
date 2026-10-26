# Neural Style Transfer | VGG19

Optimize a generated image to combine content features from one image with style features from another. A pretrained torchvision VGG19 feature stack supplies the perceptual representation; the optimized image is saved locally.

## Run

Install dependencies in a virtual environment, then pass two image paths:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py --content path\to\content.jpg --style path\to\style.jpg --steps 100
```

`--steps` controls the optimization iterations. The VGG19 weights download on first use. The result is written to `outputs/stylized.png`; model weights and outputs are not committed.

## Scope

This is an optimization demo, not a trained model or a quantitative image-quality evaluation. Use images you have the right to process and share.
