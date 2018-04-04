# Requires: userprefs.blend in .
# Function: return a key value of userprefs or return the entire dict
# Author: cdknight

import json

def get_property(key):
    """Returns the value of a connfiguration key"""
    with open('userprefs.json') as userprefs:
        json_obj = json.load(userprefs)

    return json_obj[key]

def get_property_list():
    """Return the entire configuration dict"""
    with open('userprefs.json') as userprefs:
        return json.load(userprefs)