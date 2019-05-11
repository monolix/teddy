# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .functions import Function
from .utils import fail

class Section:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.functions = []
    
    def __call__(self, description, returns):
        def wrapper(func):
            if not callable(func):
                fail("Cannot add a non-callable object.")

            self.functions.append(Function(func, description, returns))
        return wrapper
