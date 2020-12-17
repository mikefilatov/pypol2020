# imports
import os
import time

import pandas as pd

import requests
from bs4 import BeautifulSoup

import ipywidgets as widgets


# my first function in project
def foo_1(x):
    """
    function that takes argument and add something
    
    Args:
    x (any type) = input value
    
    Returns:
    str(x) * 2
    """
    print(str(x) + ' something')
    return str(x) * 2

# constant list of values    
list_of_examples = ['1', '2', '3', 'all']