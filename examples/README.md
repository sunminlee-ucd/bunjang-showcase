# Lightweight image similarity — source-derived example

`image_similarity.py` is the standalone feature/scoring module from the private application, with its algorithm unchanged. Tests and a console demo use generated images; no seller photographs or collected listing data are published.

## Run

With Python 3.10 or newer, from this directory:

```sh
python -m pip install -r requirements.txt
python -m unittest -v test_image_similarity
python demo.py
```

No API keys, cloud accounts, marketplace requests, or paid model calls are needed.

## What to inspect

The feature vector combines a coarse RGB grid, HSV histogram bins, and horizontal grayscale differences. A weighted distance becomes a bounded similarity score for features produced by this module.

Tests check identical/different synthetic images, symmetry, corrupt uploads, and malformed vector lengths. They do not measure matching accuracy on real garments or prove product identity. The module is a candidate-ranking aid, not an authenticity classifier or a hardened general-purpose upload service.

Collection, authentication, Firestore integration, and Cloud Run job orchestration remain in the private application. This folder demonstrates only the image feature mechanism.
