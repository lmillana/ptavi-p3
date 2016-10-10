#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class SmallSMILHandler():

    def get_file(self, filename):
        try:
            filename = sys.argv[1]
            return filename
        except Index_Error:
            sys.exit("Usage: python3 karaoke.py file.smil")

if __name__ == "__main__":
    file = get_file()
