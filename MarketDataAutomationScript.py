import requests
import datetime
import time


i = datetime.datetime.now()
i2 = datetime.datetime.now() - datetime.timedelta(days=1)
today = i.strftime('%Y%m%d')
yest = i2.strftime('%Y%m%d')

payload = {'USER': 'user', 'PASSWORD': 'password'}

fxrate = "fxrate_symbols_file"
cash = "cash_symbols_file"
futures = "futures_symbols_file"

fxdata = {'fromDate': '20170609', 'toDate': today,
'path': fxrate,
 'server': 'server-url',
'seriesType': 'forwards'}

cashdata = {'fromDate': '20170609', 'toDate': today,
'path': cash, 'server': 'server-url',
'seriesType': 'forwards'}

futuresdata = {'fromDate': '20170609', 'toDate': today,
'path': futures, 'server': 'server-url',
'seriesType': 'forwards'}

devloginUrl = 'devloginUrl'
devpublishUrl = 'devpublishUrl'

modloginUrl = 'modloginUrl'
modpublishUrl = 'modpublishUrl'

with requests.Session() as s:
	env = raw_input("DEV or MOD?").upper()

	if env == "DEV":
		p = s.post(devloginUrl, data=payload, verify=False)

		print "\n" + "PUBLISHING FXRATES IN DEV" + "\n"
		r = s.post(devpublishUrl, data=fxdata, verify=False)
		print "\n" + r.text + "\n"
		print "\n" + "COMPLETED FXRATES PUBLICATION IN DEV" + "\n"
		# time.sleep(5)

		print "\n" + "PUBLISHING CASH PRICES IN DEV" + "\n"
		r = s.post(devpublishUrl, data=cashdata, verify=False)
		print "\n" + r.text + "\n"
		print "\n" + "COMPLETED CASH PRICES PUBLICATION IN DEV" + "\n"

		print "\n" + "PUBLISHING FUTURES PRICES IN DEV" + "\n"
		r = s.post(devpublishUrl, data=futuresdata, verify=False)
		print "\n" + r.text + "\n"
		print "\n" + "COMPLETED FUTURES PRICES PUBLICATION IN DEV" + "\n"

	elif env == "MOD":
		p = s.post(modloginUrl, data=payload, verify=False)
		
		print "\n" + "PUBLISHING FXRATES IN MODEL" + "\n"
		r = s.post(modpublishUrl, data=fxdata, verify=False)
		print "\n" + r.text + "\n"
		print "\n" + "COMPLETED FXRATES PUBLICATION IN MODEL" + "\n"
		# time.sleep(5)

		print "\n" + "PUBLISHING CASH PRICES IN MODEL" + "\n"
		r = s.post(modpublishUrl, data=cashdata, verify=False)
		print "\n" + r.text + "\n"
		print "\n" + "COMPLETED CASH PRICES PUBLICATION IN MODEL" + "\n"

		print "\n" + "PUBLISHING FUTURES PRICES IN MODEL" + "\n"
		r = s.post(modpublishUrl, data=futuresdata, verify=False)
		print "\n" + r.text + "\n"
		print "\n" + "COMPLETED FUTURES PRICES PUBLICATION IN MODEL" + "\n"