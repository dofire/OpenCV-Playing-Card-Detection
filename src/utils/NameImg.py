import cv2


class NameImg:

    name: str
    img: cv2.typing.MatLike

    """A class to hold the name and image of a rank or suit."""

    def __init__(self, name: str, img: cv2.typing.MatLike) -> None:
        self.name = name
        self.img = img
