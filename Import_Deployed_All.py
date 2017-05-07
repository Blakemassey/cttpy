import csv
import os

os.chdir('C:\Work\Python\Scripts\cttpy\input')

with open('form_data.csv', 'rb') as f:
    reader = csv.reader(f)
    form_data = list(reader)

import mechanize, datetime, time
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
today = datetime.date.today().strftime("%Y-%m-%d 23:59:59")
start = "2013-09-01 12:00:00"

response = br.open("https://account.celltracktech.com/accounts/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[0][0]
br.form["password"] = form_data[0][1]
response = br.submit()

br.open('https://account.celltracktech.com/data/download/594/'), #Crooked (Removed April 2014)
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/72187_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/593/') #Madagascal
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/72179_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/692/') #Cherryfield
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/45895_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
start = "2015-03-01 12:00:00"

response = br.open("https://account.celltracktech.com/accounts/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[1][0]
br.form["password"] = form_data[1][1]
response = br.submit()

br.open('https://account.celltracktech.com/data/download/1762/') #Norway
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1B578_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1796/') #Phillips
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1DFAB_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1759/') #E_Musquash
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1B571_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1784/') #Eskutassis
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1D4C9_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1743/') #Three
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/27B02_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1799/') #Ellis
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1E07F_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1727/') #Sandy
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/27AD4_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1734/') #Sheepscot
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/27ADE_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1767/') #Wilson
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1CBA5_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1751/') #Crooked
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1B557_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1726/') #Webb
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/27ABC_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1741/') #Onawa
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/27AF6_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1747/') #Hebron
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/154DB_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1793/') #Branch
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1DCE4_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1752/') #Onawa2
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/All/1B55A_all.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = start; br.form["endDt"] = today
response = br.submit(); data = response.read()
time.sleep(5)
fileobj.write(data); fileobj.close()

#
#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255893451055/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/All/51055_all.csv')[0] #Not Deployed
#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255013073102/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/All/73102_all.csv')[0] #Not Deployed
#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255893450958/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/All/50958_all.csv')[0] #Not Deployed