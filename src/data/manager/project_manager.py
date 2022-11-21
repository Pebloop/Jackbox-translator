from typing import List

from src.data.project import Project


class ProjectManager:
    _projects: List[str] = []
    _project: Project = None

    def __init__(self, projects: List[str]):
        self._projects = projects

    def get_projects(self) -> List[str]:
        return self._projects

    def create_project(self, project: Project):
        self._projects.append(project.get_name())
        self._project = project
        self._project.create()

