"""This module contains method to remove URLs from a sample string."""
import re


def remove_urls_from_string(string_value):
    """Remove URLs from a sample string"""
    string = re.sub(r"http\S+", "", string_value)
    string = re.sub(r"www.\S+", "", string)
    return string
