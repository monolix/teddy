# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class Teddy:
    def __init__(self, name, description, author, long_description=None):
        self.name = name
        self.description = description
        self.long_description = long_description
        self.author = author
    
        self._sections = {}
        self._output = ""

    def _create_section(self, name):
        self._sections[str(name)] = {}

    def _check_section(self, name):
        if str(name) in self._sections:
            return True
        
        return False

    def _add_to_section(self, section, name, info, returns, example):
        self._sections[str(section)][str(name)] = {
            "info": info,
            "returns": returns,
            "example": example
        }

    def __call__(self, info="A little bunny jumping down the hill", name=None, returns=None, section="Main"):
        
        if not self._check_section(section): self._create_section(section)

        def decorator(func):
            self._add_to_section(
                section, 
                func.__name__ if name is None else name, 
                info, 
                returns, 
                func.__doc__
            )
            return func
        return decorator

    def create(self):
        self._output = ("# {name}\n"
        "##### by _{author}_\n"
        "{description}\n"
        "{long_description}").format(
            name=self.name,
            author=self.author,
            description=self.description,
            long_description="" if self.long_description is None else self.description + "\n\n"
        )

        for section, contents in self._sections.items():
            self._output += "## {}\n".format(section)

            for name, info in contents.items():
                self._output += "### `{}`\n".format(name)
                self._output += "> {}\n\n".format(info["info"])
                self._output += "Returns: **{}**\n".format(info["returns"])
                if info["example"] is not None:
                    self._output += "\n**Example**\n"
                    self._output += "```python"
                    self._output += info["example"]
                    self._output += "\n```\n"

    def dump(self, filename="docs.md"):
        self.create()

        with open(filename, "w") as f:
            f.write(self._output)
