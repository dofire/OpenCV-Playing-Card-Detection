# OpenCV 🃏 Playing Card Detection ♥️♠️♦️♣️

The user simply puts the card on a flat surface, and the program will 
- threshold the image
- find the card
- isolate the corners
- split it into rank and suit
- compare with the stored rank/suit images and then show the results

## Demo
<center>

| ♥️♠️ demo ♦️♣️ |
| :-: |
| <img src="assets/demo/demo1.png"> |
| <img src="assets/demo/demo2.png"> |

</center>
<br>

> For more information, refer to [Jupyter Notebook](main.ipynb)


## Setup (for testing)
- run `installation.ipynb` to install the required packages (or install packages manually)
- setup local `venv` or anaconda env, then hit run `main.py` (or just use `main.ipynb` instead)
- **(For Testing)** Because the `test` folder is quite large (100+ MB), you guys will have to download the `.zip` folder and then extract it into the root directory in order to test the code, which is under `releases` section

## Used Packages
- `Python 3.11.5`
- `opencv`
- `numpy`
- `matplotlib`
- `jupyter notebook`


## References
- [EdjeElectronics/OpenCV-Playing-Card-Detector](https://github.com/EdjeElectronics/OpenCV-Playing-Card-Detector)
- [dharm1k987/Card_Recognizer](https://github.com/dharm1k987/Card_Recognizer)
- [youtube](https://www.youtube.com/watch?v=s2jYdsjWirs)

