import mechanize, datetime
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]
today = datetime.date.today().strftime("%Y-%m-%d 23:59:59")
week_ago = datetime.date.today() - datetime.timedelta(days=7)
week_ago = week_ago.strftime("%Y-%m-%d %H:%M:%S")

response = br.open("https://account.celltracktech.com/accounts/login")
br.form = list(br.forms())[0]
br.form["username"] = "BRIMassey"
br.form["password"] = "Bald_2015"
response = br.submit()

br.open('https://account.celltracktech.com/data/download/1799/') #Ellis
fileobj = open('C:/Work/R/Data/BAEA/Telemetry/Deployed/Recent/1E07F_recent.csv', "w+")

response = br.open('https://account.celltracktech.com/data/download/1799/')
br.select_form(name="dataExportForm")
br.form = list(br.forms())[0]
br.form["startDt"] = week_ago; br.form["endDt"] = today
response = br.submit(); data = response.read()
fileobj.write(data); fileobj.close()
