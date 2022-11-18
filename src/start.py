import PySimpleGUI as sg

from src.appdata import AppData
from src.events.event_language_changed import EventLanguageChanged
from src.layouts.page_start import PageStart


def launch_window():
    """ Launch the window.
    This is the main loop of the app
    """
    data: AppData = AppData()

    window = sg.Window("TranslatorBox", layout=data.get_page().display(), finalize=True)

    while True:
        while len(data.get_events()) > 0:
            evn = data.pop_event()
            evn.execute()
            data.get_page().refresh(evn)
        event, values = window.read()
        print(event, values)
        data.push_event(EventLanguageChanged("FR"))

        if event == sg.WIN_CLOSED:
            break

    window.close()
