import time

import cv2
import numpy as np

from src import process
from src.utils import display
from src.utils.Loader import Loader


# show debug windows for each step
# set to False if you want to run the program with the result windows only
debug = True

## use this if you want to use your real camera
# url = 'https://192.168.1.173:8080'
# cap = cv2.VideoCapture(url + "/video")

cap = cv2.VideoCapture("test/2cards.mp4")

frame_rate = 30

ID_WIDTH = 3
ID_HEIGHT = 4
ID_BRIGHTNESS = 10

cap.set(ID_WIDTH, 640)
cap.set(ID_HEIGHT, 480)
cap.set(ID_BRIGHTNESS, 150)


ranks = Loader.load_ranks('assets/imgs/ranks')
suits = Loader.load_suits('assets/imgs/suits')

black_img = np.zeros((300, 200))

prev_time = 0
flatten_card_set = []

while True:
    time_elapsed = time.time() - prev_time

    success, img = cap.read()

    if time_elapsed > 1. / frame_rate:
        prev_time = time.time()

        img_result = img.copy()
        img_result2 = img.copy()

        thresh = process.get_thresh(img)
        four_corners_set = process.find_corners_set(thresh, img_result, draw=True)
        flatten_card_set = process.find_flatten_cards(img_result2, four_corners_set)
        cropped_images = process.get_corner_snip(flatten_card_set)

        if debug:
            if len(flatten_card_set) <= 0:
                cv2.imshow('flat', black_img)

            for flat in flatten_card_set:
                cv2.imshow('flat', flat)

        rank_suit_list: list = list()

        if debug and len(cropped_images) <= 0:
            cv2.imshow("crop", black_img)
            cv2.imshow("rank-suit", black_img)

        for i, (img, original) in enumerate(cropped_images):

            if debug:
                hori = np.concatenate((img, original), axis=1)
                cv2.imshow("crop", hori)

            drawable = img.copy()
            original_copy = original.copy()

            rank_suit = process.split_rank_suit(drawable, original_copy, debug=debug)

            rank_suit_list.append(rank_suit)

        try:
            for rank, suit in rank_suit_list:
                rank = cv2.resize(rank, (70, 100), 0, 0)
                suit = cv2.resize(suit, (70, 100), 0, 0)
                if debug:
                    h = np.concatenate((rank, suit), axis=1)
                    cv2.imshow("rank-suit", h)
        except:
            cv2.imshow("rank-suit", black_img)

        rs = list[str]()

        for _rank, _suit in rank_suit_list:
            predict_rank, predict_suit = process.template_matching(_rank, _suit, ranks, suits)
            prediction = f"{predict_rank} {predict_suit}"
            rs.append(prediction)
            print(prediction)

        process.show_text(
            predictions=rs,
            four_corners_set=four_corners_set,
            img=img_result
        )

        # show the overall image
        time.sleep(0.05)
        cv2.imshow('Result', display.stack_images(0.55, [img_result, thresh]))

    wait = cv2.waitKey(1)
    if wait & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
