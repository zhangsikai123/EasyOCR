from dataclasses import dataclass
from typing import List

import cv2
import numpy as np


@dataclass
class Rect:
    left: float
    top: float
    right: float
    bottom: float

    @staticmethod
    def from_point_list(data: List):
        bbox = Rect(0, 0, 0, 0)
        bbox.left = float('inf')
        bbox.right = -float('inf')
        bbox.top = float('inf')
        bbox.bottom = -float('inf')
        for pos in data:
            bbox.left = min(pos[0], bbox.left)
            bbox.right = max(pos[0], bbox.right)
            bbox.top = min(pos[1], bbox.top)
            bbox.bottom = max(pos[1], bbox.bottom)
        return bbox

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top


def draw_rectangle(img: np.ndarray, rect: Rect):
    """
    bbox: [left, top, right, bottom]
    """
    try:
        return cv2.rectangle(img=img, rec=(int(rect.left), int(rect.top), int(rect.width), int(rect.height)), color=(0, 255, 0))
    except Exception as e:
        import pdb
        pdb.set_trace()
        raise e
