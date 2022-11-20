from typing import List


class ProjectManager:
    _projects: List[str] = []

    def __init__(self, projects: List[str]):
        self._projects = projects



