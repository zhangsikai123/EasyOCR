import cv2

from lab.draw import draw_rectangle, Rect


def test_draw_rectangle():
    addr = './examples/chinese.jpg'
    addr_new = './out/chinese.jpg'
    img = cv2.imread(addr)
    img = draw_rectangle(img, Rect(165, 75, 469, 189))
    cv2.imwrite(addr_new, img)
