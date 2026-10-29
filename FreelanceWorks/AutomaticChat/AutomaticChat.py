# Quick-chat panel for Rocket League trades, sends preset messages in one click

import sys
import time

import pyautogui
from PyQt5 import QtCore, QtWidgets

# chat box and chat tab positions in the game, change for your screen
SOHBET = (1637, 728)
SEKME = (1854, 760)
BEKLEME = 0.6

# (button label, messages, click the chat tab first?)
SATIRLAR = [
    [
        ("NotNC!", ["Dont put your Sun Ray", "Or hot rocks not noncrate!"], False),
        ("Ibuyer", ["I'm buyer not seller!"], False),
        ("OrWant?", ["Do u have or want?"], False),
        ("Thanks.", ["Thanks!"], False),
        ("MixHas!", ["U mixed 'has'-'my wants'!"], False),
        ("Gameflip!", ["Ty for your purchase!", "Pls confirm the trade <3", "Ty for choosing me!"], True),
    ],
    [
        ("Iseller", ["I'm seller not buyer!"], False),
        ("Np.MyFr.", ["Np mate!"], False),
        ("Okay.", ["Okay."], False),
        ("Isold", ["I sold all sorry :("], False),
        ("N.Inter", ["I'm not interested."], False),
        ("Wdyw?", ["What do u want?"], False),
    ],
    [
        ("Yes!", ["Yes."], False),
        ("No!", ["No!"], False),
        ("Pls.Wait!", ["Pls just wait your turn!"], False),
        ("PlsWritewdyw!", ["Pls write wdyw H:xx W:xx"], False),
        ("P.Quickly!", ["Pls quickly!"], False),
        ("IwillInte!", ["I will interested everyone!"], False),
    ],
    [
        ("HMDYW?", ["How many do u want?"], False),
        ("HMDYH?", ["How many do u have?"], False),
        ("F.Price!", ["Firm price sorry :("], False),
        ("Sure.L!", ["Sure lets go!"], False),
        ("Sorry!", ["Sorry I can't help u :("], False),
        ("W.Color?", ["What color do u want?"], False),
    ],
    [
        ("Hello!", ["Hey, How can I help u?"], True),
        ("Hello!2", ["Hey, How can I help u?"], False),
        ("Lobby!", ["Hey guys trader is me Wdyw?"], True),
        ("Lobby!2", ["Hey guys trader is me Wdyw?"], False),
        ("Bb!", ["Have a great day!"], True),
        ("Bb!2", ["Have a great day!"], False),
    ],
]


def gonder(mesajlar, sekme):
    if sekme:
        pyautogui.click(*SEKME)
        time.sleep(0.1)
    for i, mesaj in enumerate(mesajlar):
        if i > 0:
            time.sleep(BEKLEME)
        pyautogui.click(*SOHBET)
        pyautogui.write(mesaj)
        pyautogui.press("enter")


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rocket Bot")
        # keep the window above the game
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        v_box = QtWidgets.QVBoxLayout()
        for satir in SATIRLAR:
            h_box = QtWidgets.QHBoxLayout()
            for etiket, mesajlar, sekme in satir:
                buton = QtWidgets.QPushButton(etiket)
                buton.clicked.connect(lambda _, m=mesajlar, s=sekme: gonder(m, s))
                h_box.addWidget(buton)
            v_box.addLayout(h_box)
        self.setLayout(v_box)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())
