import argparse
import os
import sys

import cv2

from easyocr import easyocr
from lab.draw import draw_rectangle, Rect


def parse_args():
    parser = argparse.ArgumentParser(description="Process EasyOCR.")
    parser.add_argument(
        "-l",
        "--lang",
        nargs='+',
        required=True,
        type=str,
        help="for languages",
    )
    parser.add_argument(
        "-f",
        "--file",
        required=False,
        type=str,
        help="input file",
    )

    parser.add_argument(
        "-d",
        "--dir",
        required=False,
        type=str,
        help="input dir",
    )

    parser.add_argument(
        "--detail",
        type=int,
        choices=[0, 1],
        default=1,
        help="simple output (default: 1)",
    )
    parser.add_argument(
        "--gpu",
        type=bool,
        choices=[True, False],
        default=True,
        help="Using GPU (default: True)",
    )
    args = parser.parse_args()
    return args


def run():
    confidence_threshold = 0.3

    args = parse_args()
    reader = easyocr.Reader(lang_list=args.lang, gpu=args.gpu)
    files = []
    if args.dir:
        for filename in sorted(os.listdir(args.dir)):
            files.append(os.path.join(args.dir, filename))
    if args.file:
        files.append(args.file)
    for file in files:
        img = cv2.imread(file)
        for line in reader.readtext(file, detail=args.detail):
            rect, text, confidence = line
            if confidence > confidence_threshold:
                img = draw_rectangle(img, Rect.from_point_list(rect))
                print(text)
        new_addr = os.path.join('out', file)
        os.makedirs(os.path.dirname(new_addr), exist_ok=True)
        cv2.imwrite(new_addr, img)


if __name__ == '__main__':
    run()
