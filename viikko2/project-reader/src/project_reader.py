from urllib import request
from project import Project
import tomli
import ssl

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        context = ssl._create_unverified_context()
        
        content = request.urlopen(self._url, context=context).read().decode("utf-8")
        
        toml_data = tomli.loads(content)
        
        poetry_data = toml_data["tool"]["poetry"]
        
        name = poetry_data.get("name", "")
        description = poetry_data.get("description", "")
        license = poetry_data.get("license", "")
        authors = poetry_data.get("authors", [])
        dependencies = list(poetry_data.get("dependencies", {}).keys())
        dev_dependencies = list(poetry_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        
        return Project(
            name,
            description,
            license,
            authors,
            dependencies,
            dev_dependencies
        )