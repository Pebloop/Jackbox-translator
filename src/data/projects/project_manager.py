from typing import List

from src.data.projects.metaproject import MetaProject
from src.data.projects.project import Project


class ProjectManager:
    _projects: List[MetaProject] = []
    _project: Project = None

    def __init__(self, projects: List[MetaProject]):
        self._projects = projects

    def get_projects(self) -> List[MetaProject]:
        return self._projects

    def create_project(self, project: Project):
        self._projects.append(MetaProject(project.get_name(), project.get_language(), project.get_game()))
        self._project = project
        self._project.create()
