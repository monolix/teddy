# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import sys

def fail(message):
    print("[TEDDY:Error] {}".format(message), flush=True)
    sys.exit(1)
