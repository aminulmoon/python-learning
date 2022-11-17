import searchconsole
account = searchconsole.authenticate(client_config='client_secret_key.json')
webproperty = account['https://chilavie.com/']
report = webproperty.query.range('today', days=-14).dimension('query').get()
print(report.rows)
