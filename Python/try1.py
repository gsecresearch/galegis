# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:06:40 2016

@author: Devin
"""
import requests
hey = requests.get('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=')

"""
attempting a post request
"""

hcon = requests.post('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=', data={'ctl00$ContentPlaceHolder1$Results$ctl02$lnkView':''})

"""
Maybe this is the key:  name="__VIEWSTATEENCRYPTED" id="__VIEWSTATEENCRYPTED" value="" />\r\n<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION"
"""

hcon1 = requests.post('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=', data={'ctl00$ContentPlaceHolder1$Results$ctl02$lnkView':'__doPostBack'})


hcon2 = requests.post('http://media.ethics.ga.gov/search/Lobbyist/Lobbyist_results.aspx?&Year=2016&LastName=thom&FirstName=&City=&FilerID=', data={'ctl00$ContentPlaceHolder1$Results$ctl02$lnkView':'javascript:__doPostBack'})
hco