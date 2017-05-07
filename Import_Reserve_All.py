import csv
import os

os.chdir('C:\Work\Python\Scripts\cttpy\input')

with open('form_data.csv', 'rb') as f:
    reader = csv.reader(f)
    form_data = list(reader)


import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]

response = br.open("http://account.celltracktech.com/ctt/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[0][0]
br.form["password"] = form_data[0][1]

response = br.submit()
br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255013072179/all.csv',
                                   'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/72179_all.csv')[0] #Madagascal
br.retrieve('http://account.celltracktech.com/ctt/devices/89014103256345345895/all.csv',
                                   'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/45895_all.csv')[0] #Cherryfield
br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255013072187/all.csv',
                                   'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/72187_all.csv')[0] #Crooked

br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255893451055/all.csv',
                                   'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/51055_all.csv')[0] #Not Deployed
br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255013073102/all.csv',
                                   'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/73102_all.csv')[0] #Not Deployed
br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255893450958/all.csv',
                                   'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/50958_all.csv')[0] #Not Deployed


br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]

response = br.open("http://account.celltracktech.com/ctt/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[1][0]
br.form["password"] = form_data[1][1]

response = br.submit()
br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1B57D/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1B57D_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1D4C9/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1D4C9_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F154DB/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/154DB_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A100003E427B02/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/27B02_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A100003E427AF6/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/27AF6_all.csv')[0]


br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1DFAB/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1DFAB_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A100003E427ABC/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/27ABC_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A100003E427ADE/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/27ADE_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A100003E427AD4/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/27AD4_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1CBA5/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1CBA5_all.csv')[0]


br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1B557/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1B557_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1CF56/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1CF56_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1B578/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1B578_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1E07F/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1E07F_all.csv')[0]

br.retrieve('http://account.celltracktech.com/ctt/devices/A1000042F1B571/all.csv', #Not Deployed
'C:/Work/R/Data/BAEA/Telemetry/Reserve/All/1B571_all.csv')[0]