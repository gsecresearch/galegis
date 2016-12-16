# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:31:19 2016

@author: Devin
"""

import requests
import json

rp = requests.post('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=',json={'pathname':'ctl00$ContentPlaceHolder1$Results$ctl04$lnkView'})

rp1 = requests.post('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=',json={'ctl00_ContentPlaceHolder1_Results_ctl02_lnkView':'__doPostBack'})

"""
Is the key the name of the object and then the action simply blank?  
"""

rp2 = requests.post('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=',json={'javascript:__doPostBack(ctl00$ContentPlaceHolder1$Results$ctl02$lnkView)':''})

"""
This says you need a header:  http://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
"""
