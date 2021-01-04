#
# arista.avd.defined
#
# Example:
# A is undefined
# B is none
# C is "c"
# D is "d"
#
# Jinja test examples:
# {% if A is arista.avd.defined %}  =>  false
# {% if B is arista.avd.defined %}  =>  false
# {% if C is arista.avd.defined %}  =>  true
# {% if D is arista.avd.defined %}  =>  true
#
# {% if A is arista.avd.defined("c") %}  =>  false
# {% if B is arista.avd.defined("c") %}  =>  false
# {% if C is arista.avd.defined("c") %}  =>  true
# {% if D is arista.avd.defined("c") %}  =>  false

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2.runtime import Undefined

def defined(value, test_value=None):
    if isinstance(value, Undefined) or value is None:
        #Invalid value - return false
        return False
    elif test_value is not None and value != test_value:
        #Valid value but not matching the optional argument
        return False
    else:
        #Valid value and is matching optional argument if provided - return true
        return True

class TestModule(object):
    def tests(self):
        return {
            'defined': defined,
        }
