import unittest
from io import BytesIO
from PIL import Image
from image_similarity import features, similarity


def solid(color):
    output = BytesIO()
    Image.new('RGB', (24, 24), color).save(output, format='PNG')
    return output.getvalue()


class ImageSimilarityTests(unittest.TestCase):
    def test_reencoded_identical_color_retains_a_perfect_match(self):
        left = features(solid('red'))
        right = features(solid((255, 0, 0)))
        self.assertEqual(similarity(left, right), 1.0)

    def test_different_colors_rank_below_identical_image(self):
        red = features(solid('red'))
        blue = features(solid('blue'))
        self.assertLess(similarity(red, blue), similarity(red, red))
        self.assertEqual(similarity(red, blue), similarity(blue, red))

    def test_corrupt_upload_is_rejected(self):
        with self.assertRaises(ValueError):
            features(b'not an image')

    def test_malformed_feature_vectors_are_rejected(self):
        with self.assertRaises(ValueError):
            similarity([0.0], [0.0])


if __name__ == '__main__':
    unittest.main()
