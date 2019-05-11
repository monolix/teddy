# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class Function:
    def __init__(self, function, description, returns):
        self.function = function
        self.name = function.__name__
        self.example = function.__doc__
        self.description = description
        self.returns = returns.__name__
