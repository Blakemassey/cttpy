import csv
import os

os.chdir('C:\Work\Python\Scripts\cttpy\input')

with open('form_data.csv', 'rb') as f:
    reader = csv.reader(f)
    form_data = list(reader)

import mechanize, datetime
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
today = datetime.date.today().strftime("%Y-%m-%d 23:59:59")
week_ago = datetime.date.today() - datetime.timedelta(days=60)
week_ago = week_ago.strftime("%Y-%m-%d %H:%M:%S")

response = br.open("https://account.celltracktech.com/accounts/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[0][0]
br.form["password"] = form_data[0][1]
response = br.submit()

br.open('https://account.celltracktech.com/data/download/593/') #Madagascal
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/72179_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/692/') #Cherryfield
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/45895_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]

response = br.open("https://account.celltracktech.com/accounts/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[1][0]
br.form["password"] = form_data[1][1]
response = br.submit()


br.open('https://account.celltracktech.com/data/download/1759/') #Musquash
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1B571_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1784/') #Eskutassis
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1D4C9_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1743/') #Three
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/27B02_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1799/') #Ellis
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1E07F_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1727/') #Sandy
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/27AD4_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1767/') #Wilson
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1CBA5_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1751/') #Crooked
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1B557_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1726/') #Webb
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/27ABC_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1747/') #Hebron
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/154DB_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1793/') #Branch
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1DCE4_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()


#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255013072187/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/72187_recent.csv')[0] #Crooked (Removed April 2014)
#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255893451055/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/51055_recent.csv')[0] #Not Deployed
#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255013073102/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/73102_recent.csv')[0] #Not Deployed
#br.retrieve('http://account.celltracktech.com/ctt/devices/89014103255893450958/recent.csv',
#                               'C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/50958_recent.csv')[0] #Not Deployed