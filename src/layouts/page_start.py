import PySimpleGUI as sg
from src.language import get_text

def load_projects_layout():
    return sg.Text(get_text("NO_PROJECTS"))

layout = [
    [
        sg.Text(get_text("CURRENT_PROJECTS")),
        load_projects_layout()
    ]
]