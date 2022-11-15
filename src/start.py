import PySimpleGUI as sg

from src.appdata import AppData
from src.events.event_language_changed import EventLanguageChanged
from src.layouts.page_start import PageStart


def launch_window():
    data: AppData = AppData()

    window = sg.Window("TranslatorBox", layout=data.get_page().display())
    print(data.get_page().display())

    while True:
        #data.push_event(EventLanguageChanged("en", "fr"))
        event, values = window.read()
        print(event, values)
        for event in data.get_events():
            data.get_page().refresh(event)
        data.clear_events()
        if event == sg.WIN_CLOSED:
            break

    window.close()
