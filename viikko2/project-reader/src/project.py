class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, items):
        if not items:
            return "-"
        return "\n- " + "\n- ".join(items)

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license or '-'}\n"
            f"\nAuthors:{self._stringify_list(self.authors)}\n"
            f"\nDependencies:{self._stringify_list(self.dependencies)}\n"
            f"\nDevelopment dependencies:{self._stringify_list(self.dev_dependencies)}"
        )