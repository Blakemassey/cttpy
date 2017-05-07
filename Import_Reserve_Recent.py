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
week_ago = datetime.date.today() - datetime.timedelta(days=21)
week_ago = week_ago.strftime("%Y-%m-%d %H:%M:%S")

response = br.open("https://account.celltracktech.com/accounts/login")
br.form = list(br.forms())[0]
br.form["username"] = form_data[1][0]
br.form["password"] = form_data[1][1]
response = br.submit()

br.open('https://account.celltracktech.com/data/download/1758/') #Not Deployed
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1B570_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1788/') #Not Deployed
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1D6F4_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()

br.open('https://account.celltracktech.com/data/download/1787/') #Not Deployed
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1D658_recent.csv', "w+")
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()



# br.open('https://account.celltracktech.com/data/download/1741/') #Onawa
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/27AF6_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# br.form = list(br.forms())[0]
# br.form["startDt"] = week_ago; br.form["endDt"] = today
# response = br.submit(); data = response.read()
# fileobj.write(data); fileobj.close()

# br.open('https://account.celltracktech.com/data/download/1752/') #Onawa2
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1B55A_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# br.form = list(br.forms())[0]
# br.form["startDt"] = week_ago; br.form["endDt"] = today
# response = br.submit(); data = response.read()
# fileobj.write(data); fileobj.close()

# br.open('https://account.celltracktech.com/data/download/1762/') #Norway
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1B578_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# br.form = list(br.forms())[0]
# br.form["startDt"] = week_ago; br.form["endDt"] = today
# response = br.submit(); data = response.read()
# fileobj.write(data); fileobj.close()

# br.open('https://account.celltracktech.com/data/download/1796/') #Phillips
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1DFAB_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# br.form = list(br.forms())[0]
# br.form["startDt"] = week_ago; br.form["endDt"] = today
# response = br.submit(); data = response.read()
# fileobj.write(data); fileobj.close()


# br.open('https://account.celltracktech.com/data/download/1734/') #Sheepscot
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/27ADE_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# br.form = list(br.forms())[0]
# br.form["startDt"] = week_ago; br.form["endDt"] = today
# response = br.submit(); data = response.read()
# fileobj.write(data); fileobj.close()



# br.open('http://account.celltracktech.com/ctt/devices/A1000042F1B55A/export') #Not Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1B55A_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A1000042F1DCE4/export') #Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1DCE4_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A100003E427AF6/export') #Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/27AF6_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A1000042F154DB/export') #Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/154DB_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A1000042F1B57D/export') #Returned
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1B57D_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A1000042F1D4C9/export') #Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1D4C9_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A100003E427B02/export') #Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/27B02_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A1000042F1DFAB/export') #Deployed
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1DFAB_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

##br.open('http://account.celltracktech.com/ctt/devices/A100003E427ABC/export') #Deployed
##fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/27ABC_recent.csv', "w+")
##br.select_form(name="dataExportForm")
##response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

##br.open('http://account.celltracktech.com/ctt/devices/A1000042F1B557/export') #Deployed
##fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1B557_recent.csv', "w+")
##br.select_form(name="dataExportForm")
##response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

# br.open('http://account.celltracktech.com/ctt/devices/A1000042F1CF56/export') #Returned
# fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1CF56_recent.csv', "w+")
# br.select_form(name="dataExportForm")
# response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

##br.open('http://account.celltracktech.com/ctt/devices/A1000042F1B578/export') #Deployed
##fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1B578_recent.csv', "w+")
##br.select_form(name="dataExportForm")
##response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

##br.open('http://account.celltracktech.com/ctt/devices/A1000042F1E07F/export') #Deployed
##fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1E07F_recent.csv', "w+")
##br.select_form(name="dataExportForm")
##response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()

#br.open('http://account.celltracktech.com/ctt/devices/A1000042F1B571/export') #Deployed
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/1B571_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()


#response = br.open("http://account.celltracktech.com/ctt/login")
#br.form = list(br.forms())[0]
#br.form["username"] =
#br.form["password"] =
#response = br.submit()

#br.open('http://account.celltracktech.com/ctt/devices/89014103255013072179/export') #Madagascal
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/72179_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()
#br.open('http://account.celltracktech.com/ctt/devices/89014103256345345895/export') #Cherryfield
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/45895_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()
#br.open('http://account.celltracktech.com/ctt/devices/89014103255013072187/export') #Crooked
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/72187_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()
#br.open('http://account.celltracktech.com/ctt/devices/89014103255893451055/export') #Not Deployed
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/51055_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()
#br.open('http://account.celltracktech.com/ctt/devices/89014103255013073102/export') #Not Deployed
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/73102_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()
#br.open('http://account.celltracktech.com/ctt/devices/89014103255893450958/export') #Not Deployed
#fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Reserve/Recent/50958_recent.csv', "w+")
#br.select_form(name="dataExportForm")
#response = br.submit(); data = response.read(); fileobj.write(data); fileobj.close()