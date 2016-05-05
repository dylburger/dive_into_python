#!/usr/bin/env python3

""" Try and catch an import error for a library that I don't have installed
"""
try:
    import chardet
except ImportError:
    chardet = None

if chardet:
    print("chardet module is installed")
else:
    print("chardet module not installed on this system")
