import json
from typing import List
import time
import timeit
import pyautogui
from pyautogui import ImageNotFoundException

name_list = [
    "ADHYASTA NAUFAL FAADHILAH",
    "GERRY CIPUTRA LUNARDI",
    "GIRINDRA SYUKRAN PRAHASTO",
    "ZIKRI KHOLIFAH NUR",
    "FAKHRUL MAULIDAN GUSTIANA",
    "KIKI DWI PRASETYO",
    "DILA ADELIA"
]


grade_list = [
    [1, 4, 4, 1, 1.5],
    [3.5, 4, 1, 1, 1],
    [4, 4, 4, 1, 3],
    [4, 4, 4, 1, 3],
    [4, 4, 4, 1, 2],
    [4, 4, 4, 1, 2],
    [4, 4, 4, 1, 2]
]

datas = [
    {
        "kelas": "07",
        "modul": "6",
        "praktikan": [
            "ANDI ACHMAD ADJIE",
            "ALFI SYAHRIN PRATAMA",
            "ZAIDAN SAID",
            "RIZKY ARIA MU`ALLIM",
            "MUHAMMAD IKHSAN",
            "QAIS KALYANA LINTANG",
            "ARIA REYHAN JAYADININGRAT"
        ],
        "nilai": [
            [
                10,
                0,
                0,
                4,
                0,
                0
            ],
            [
                1,
                0,
                4,
                1,
                0,
                0
            ],
            [
                0,
                0,
                2,
                0,
                0,
                2
            ],
            [
                4,
                4,
                4,
                4,
                19,
                4
            ],
            [
                1,
                0,
                4,
                4,
                2,
                0
            ],
            [
                2,
                2,
                4,
                4,
                20,
                3
            ],
            [
                3,
                4,
                4,
                4,
                2,
                20
            ]
        ]
    }
]

def open_all_student(name_list: List):
    for i in range(len(name_list)):
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write(name_list[i])
        pyautogui.press('esc')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'enter')

def open_a_student(name: str):
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write(name)
    pyautogui.press('esc')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'enter')

def find_and_open(elm: str, enter: int):
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write(elm)
    for i in range(enter):
        pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.press('enter')


if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    time.sleep(1)
    try:
        start = timeit.default_timer()
        data = json.load('nilai.json')
        for data in datas:
            pyautogui.hotkey('alt', 'tab')
            for num in range(len(data['praktikan'])):
                open_a_student(data['praktikan'][num])
                pyautogui.hotkey('ctrl', 'pagedown')
                for quest in range(len(data['nilai'][0])):
                    time.sleep(3)
                    find_and_open('Make', quest)
                    time.sleep(3)
                    coor = pyautogui.locateOnScreen('class_diagram.png')
                    if coor:
                        pyautogui.press('tab')
                    for i in range(7):
                        pyautogui.press('tab')
                    pyautogui.write(str(data['nilai'][num][quest]))
                    pyautogui.press('enter')
                    time.sleep(3)
                    pyautogui.press('end')
                time.sleep(3)
                pyautogui.hotkey('ctrl', 'w')
                pyautogui.hotkey('ctrl', 'pagedown')
                pyautogui.write(str(sum(data['nilai'][num])))
                pyautogui.press('enter')
                pyautogui.hotkey('ctrl', 'pageup')
        stop = timeit.default_timer()
        pyautogui.alert(text=f'Selesai dalam waktu {stop-start}', title='Selesai')
    except KeyboardInterrupt:
        print('\n')
