import json
import time
import pyautogui

pyautogui.PAUSE = 0.5

def open_all_student(name_list):
    for i in range(len(name_list)):
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.write(name_list[i])
        pyautogui.press('esc')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'enter')


def open_a_student(name: str):
    pyautogui.press('home')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write(name)
    pyautogui.press('esc')
    found = pyautogui.locateOnScreen('found3.png')
    alter = pyautogui.locateOnScreen('found4.png')
    if found or alter:
        pyautogui.press('esc')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'enter')
        return True
    else:
        return False


def clear_notepad():
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.hotkey('alt', 'tab')


def find_and_open(elm: str, enter: int):
    pyautogui.press('end')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write(elm)
    for i in range(enter):
        pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.press('enter')


name_list = [
    "ADHYASTA NAUFAL FAADHILAH",
    "GERRY CIPUTRA LUNARDI",
    "GIRINDRA SYUKRAN PRAHASTO",
    "ZIKRI KHOLIFAH NUR",
    "FAKHRUL MAULIDAN GUSTIANA",
    "KIKI DWI PRASETYO",
    "DILA ADELIA"
]

if __name__ == "__main__":
    file = None
    with open('praktikan.json') as file:
        data = json.load(file)
    
    pyautogui.alert("Assited mode start")
    pyautogui.hotkey('alt', 'tab')
    try:
        nilai = pyautogui.locateOnScreen('nilai.png')
        while not nilai:
            wp = pyautogui.locateOnScreen('wp.png')
            nilai = pyautogui.locateOnScreen('nilai.png')
            
            index = 0
            if wp:
                pyautogui.alert("Assited mode end")
                break
            if nilai:
                clear_notepad()
                kelas = pyautogui.prompt("Masukkan kelas")
                try:
                    open_a_student(data[kelas][index])
                    np = pyautogui.locateOnScreen('np.png')
                    while not np:
                        np = pyautogui.locateOnScreen('np.png')
                        wp = pyautogui.locateOnScreen('wp.png')
                        if wp:
                            pyautogui.alert("Assited mode end")
                            break
                        if np:
                            isi_nilai = pyautogui.prompt("Masukkan nilai")
                            isi_nilai = isi_nilai.split(",")
                            clear_notepad()
                            for i in range(len(isi_nilai)):
                                time.sleep(2)
                                find_and_open('Make', i)
                                time.sleep(2)
                                coor = pyautogui.locateOnScreen('class_diagram.png')
                                if coor:
                                    pyautogui.press('tab')
                                for x in range(7):
                                    pyautogui.press('tab')
                                pyautogui.write(isi_nilai[i])
                                pyautogui.press('enter')
                                time.sleep(1)
                                pyautogui.hotkey('ctrl', 'w')
                                pyautogui.press('end')
                            res = sum([float(x) for x in isi_nilai])
                            pyautogui.hotkey('ctrl', 'w')
                            pyautogui.hotkey('ctrl', 'pagedown')
                            pyautogui.write(str(res))
                            pyautogui.press('enter')
                            pyautogui.hotkey('ctrl', 'pageup')
                            # if open_a_student(data[kelas][index]):
                            #     start = pyautogui.locateOnScreen('start.png')
                            #     while not start:
                            #         start = pyautogui.locateOnScreen('start.png')
                            #         wp = pyautogui.locateOnScreen('wp.png')
                                    
                            #         if wp:
                            #             pyautogui.alert("Assisted mode end")
                            #             break
                            #         if start:
                            #             isi_nilai = pyautogui.prompt("Masukkan nilai")
                            #         isi_nilai = isi_nilai.split(",")
                            #         for i in range(len(isi_nilai)):
                            #             time.sleep(3)
                            #             find_and_open('Make', i)
                            #             time.sleep(3)
                            #             coor = pyautogui.locateOnScreen('class_diagram.png')
                            #             if coor:
                            #                 pyautogui.press('tab')
                            #             for i in range(7):
                            #                 pyautogui.press('tab')
                            #             pyautogui.write(isi_nilai[i])
                            #             pyautogui.press('enter')
                            #             time.sleep(3)
                            np = None
                            index += 1
                            if index == len(data[kelas]):
                                break
                            open_a_student(data[kelas][index])
                except KeyError:
                    pyautogui.alert("Kelas tidak ditemukan")
            
            nilai = None
            index += 1
        index = 0
    except KeyboardInterrupt:
        print('\n')
