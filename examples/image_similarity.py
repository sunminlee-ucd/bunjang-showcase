"""Lightweight visual matching: color, layout and edges, not model identity."""
import math
from io import BytesIO
from PIL import Image, ImageOps, UnidentifiedImageError


def features(raw):
    try:
        with Image.open(BytesIO(raw)) as image:
            if image.width*image.height > 20000000:
                raise ValueError('이미지가 너무 큽니다.')
            image=ImageOps.exif_transpose(image).convert('RGB')
            small=ImageOps.fit(image,(12,12))
            grid=[v/255 for pixel in small.getdata() for v in pixel]
            hist=image.resize((64,64)).convert('HSV').histogram()
            bins=[sum(hist[channel*256+i:channel*256+i+16])/4096 for channel in range(3) for i in range(0,256,16)]
            gray=list(ImageOps.fit(image,(13,12)).convert('L').getdata())
            edges=[(gray[y*13+x]-gray[y*13+x+1])/255 for y in range(12) for x in range(12)]
            return grid+bins+edges
    except (UnidentifiedImageError,OSError,Image.DecompressionBombError) as exc:
        raise ValueError('JPEG·PNG·WebP 사진을 선택해주세요.') from exc


def similarity(a,b):
    if len(a)!=624 or len(b)!=624:
        raise ValueError('이미지 특징 형식 오류')
    grid=sum(abs(x-y) for x,y in zip(a[:432],b[:432]))/432
    hist=sum(abs(x-y) for x,y in zip(a[432:480],b[432:480]))/6
    edge=sum(abs(x-y) for x,y in zip(a[480:],b[480:]))/144
    return round(max(0,1-(.45*grid+.35*hist+.2*edge)),6)
