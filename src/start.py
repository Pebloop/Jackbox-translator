import PySimpleGUI as sg
import src.layouts.page_start as page_start


def launch_window():
    window = sg.Window("TranslatorBox", page_start.layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()
