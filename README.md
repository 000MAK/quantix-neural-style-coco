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

## Results

No reference output is published yet. Style transfer has no single accuracy metric; publish the content/style images, iterations and loss weights with any example.

## Repository contents

| File | Purpose |
|---|---|
| `.gitignore` | Keeps data, weights and outputs out of Git |
| `LICENSE` | MIT licence for the code |
| `main.py` | Training and evaluation script |
| `requirements.txt` | Python dependencies |

## License

Code is released under the MIT License (see `LICENSE`). Datasets keep their own licences and are downloaded at run time, not redistributed here.

## Related

Part of a set of compact, reproducible ML/DL baselines by [000MAK](https://github.com/000MAK). Flagship research project: [QMASE martial-arts analytics engine](https://github.com/000MAK/quantix-martial-arts-engine).
