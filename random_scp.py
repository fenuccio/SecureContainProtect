# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:35:02 2021

@author: angel
"""

import webbrowser
import random
def main():
    n = "000" + str(random.randint(1, 5999))
    while len(n) > 4:
        n = n.replace("0", "", 1)
    if n[0] == "0":
        n = n.replace("0", "", 1)
    website = "http://www.scpwiki.com/scp-" + n
    webbrowser.open(website)
    
main()