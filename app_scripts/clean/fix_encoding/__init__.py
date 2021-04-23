"""This module fixes broken encoding"""
import ftfy


def ftfy_fix_encoding(string_value):
    """Fixes broken encoding."""
    return ftfy.fix_encoding(string_value)
