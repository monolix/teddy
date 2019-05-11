# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .section import Section
from .utils import fail

from pkg_resources import resource_string
from jinja2 import Template

__all__ = ["Teddy", "Section"]

class Teddy:
    def __init__(self, name, description, \
        author, long_description=None):
        self.name = name
        self.description = description
        self.long_description = long_description
        self.author = author

        self.sections = []
    
    def add_section(self, *sections):
        for section in sections:
            if not isinstance(section, Section):
                fail("Cannot add a non-section.")
            
            self.sections.append(section)

    def dump(self, filename="docs.html", template="default.html"):
        path = "/".join(("templates", template))
        resource = resource_string(__name__, path)
        
        template_ = Template(resource.decode("utf-8"))
        templated = template_.render(teddy=self)

        with open(filename, "w") as f:
            f.write(templated)
