from io import BytesIO
from PIL import Image
from image_similarity import features, similarity


def swatch(color):
    output = BytesIO()
    Image.new('RGB', (24, 24), color).save(output, format='PNG')
    return features(output.getvalue())


red = swatch('red')
blue = swatch('blue')
print('Brand Lens image excerpt — generated color swatches, no marketplace requests')
print({'identical_red': similarity(red, red), 'red_vs_blue': similarity(red, blue)})
print('A similarity score is not a product model or authenticity verdict.')
