import cv2

from src.utils.NameImg import NameImg


class Loader:

    @staticmethod
    def load_ranks(dirpath: str):
        """Loads rank images from directory specified by filepath. Stores
        them in a list of Train_ranks objects."""

        if dirpath is not None:
            dirpath = dirpath.removesuffix('/')
            dirpath = dirpath + '/'

        train_ranks = []
        i = 0

        for rank_name in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            filepath = dirpath + rank_name + '.jpg'

            name_img = NameImg(
                name=rank_name, 
                img=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            )
            train_ranks.append(name_img)

            i = i + 1

        return train_ranks
    

    @staticmethod
    def load_suits(dirpath):
        """Loads suit images from directory specified by filepath. Stores
        them in a list of Train_suits objects."""

        if dirpath is not None:
            dirpath = dirpath.removesuffix('/')
            dirpath = dirpath + '/'

        train_suits = []
        i = 0

        for suit_name in ['Spades', 'Diamonds', 'Clubs', 'Hearts']:
            filepath = dirpath + suit_name + '.jpg'

            name_img = NameImg(
                name=suit_name, 
                img=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            )
            train_suits.append(name_img)
            i = i + 1

        return train_suits
