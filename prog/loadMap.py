import pandas as pd 
import csv

"""
    we need the following:
        pathsTouching = {fromGlobalId, toGlobalId, altitude, name, direction}
            - NOTE: a->b is different from b->a. Odd people fly East.
        neighbors[globalID] = pathsTouching[]
"""

def loadPoints(filename : str):
    ans = {}