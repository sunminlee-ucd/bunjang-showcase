"""Render a reproducible, synthetic example using the public scoring module."""
import json
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from image_similarity import features, similarity


def feature_vector(image):
    stream = BytesIO()
    image.save(stream, format="PNG")
    return features(stream.getvalue())


def font(size):
    # Pillow's bundled font keeps this runnable without system font files.
    return ImageFont.load_default(size=size)


def main():
    output = Path(__file__).resolve().parents[1] / "assets"
    output.mkdir(exist_ok=True)
    reference = Image.new("RGB", (120, 120), "red")
    partial = reference.copy()
    ImageDraw.Draw(partial).rectangle((60, 0, 119, 59), fill="blue")
    candidates = [
        ("Identical red", reference.copy()),
        ("Blue corner", partial),
        ("Solid blue", Image.new("RGB", (120, 120), "blue")),
    ]
    query = feature_vector(reference)
    scores = []
    for name, image in candidates:
        vector = feature_vector(image)
        distances = {
            "rgb_grid": sum(abs(a-b) for a, b in zip(query[:432], vector[:432])) / 432,
            "hsv_histogram": sum(abs(a-b) for a, b in zip(query[432:480], vector[432:480])) / 6,
            "horizontal_edges": sum(abs(a-b) for a, b in zip(query[480:], vector[480:])) / 144,
        }
        scores.append({"candidate": name, "score": similarity(query, vector), "distances": distances})

    canvas = Image.new("RGB", (1200, 630), "#f4f6f8")
    draw = ImageDraw.Draw(canvas)
    draw.text((40, 28), "Brand Lens | visual similarity sample", font=font(29), fill="#142c26")
    draw.text((40, 72), "Generated color patches. Actual output from the public Python module.", font=font(19), fill="#44535d")

    panels = [("Reference", reference, None)] + [(name, image, item) for (name, image), item in zip(candidates, scores)]
    for index, (label, image, result) in enumerate(panels):
        left = 40 + index * 285
        draw.rounded_rectangle((left, 120, left+265, 420), radius=14, fill="white", outline="#d8e0e4")
        draw.text((left+18, 138), label, font=font(21), fill="#142c26")
        canvas.paste(image.resize((160, 160)), (left+52, 184))
        score_text = "Compare each candidate" if result is None else f"Similarity: {result['score']:.6f}"
        draw.text((left+18, 370), score_text, font=font(18), fill="#142c26")

    draw.text((40, 450), "624 features: RGB layout (432) + HSV histogram (48) + horizontal edges (144)", font=font(20), fill="#142c26")
    draw.text((40, 490), "score = max(0, 1 - 0.45 x RGB distance - 0.35 x HSV distance - 0.20 x edge distance)", font=font(19), fill="#44535d")
    draw.text((40, 540), "A similarity score is not a probability, an exact-model match, or an authenticity verdict.", font=font(19), fill="#142c26")
    draw.text((40, 576), "Synthetic code demo only. No marketplace images, network requests, credentials, or paid AI calls.", font=font(18), fill="#44535d")
    canvas.save(output / "image-similarity-demo.png")
    result = {"input": "generated RGB color patches", "feature_dimensions": len(query), "candidates": scores}
    (output / "image-similarity-demo.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
