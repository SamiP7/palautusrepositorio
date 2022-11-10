from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        c = request.urlopen(self._url).read().decode("utf-8")
        content = toml.loads(c, _dict=dict)
        
        name = content["tool"]["poetry"]["name"]
        desc = content["tool"]["poetry"]["description"]
        depen = content["tool"]["poetry"]["dependencies"]
        devdepen = content["tool"]["poetry"]["dev-dependencies"]      
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depen, devdepen)
