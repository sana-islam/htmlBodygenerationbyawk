>>> import smtplib
>>> sender='gpecm@xxxxxxxx.com'
>>> receivers=['sana.islam@xxxxxxxxx.com']
>>> message = """From: From Person <me@xxxxxxxx.com>
... To: To Person <sana.islam@grameenphone.com>,<kamonashih@xxxxxxxx.com>
... MIME-Version: 1.0
... Content-type: text/html
... Subject: ECM Submit & Delivery Status
...
... ECM Submit & Delivery Status: \n
...
... <html><body>
... <table border=1 cellspacing=2 cellpadding=2>
... <tr>
... <td>date</td>
... <td>submit_success</td>
... <td>submit_fail</td>
... <td>dr_success</td>
... <td>dr_fail</td>
... <td>Diff</td>
... </tr>
... <tr>
... <td>2019-09-22</td>
... <td>3787937</td>
... <td>3929</td>
... <td>3460219</td>
... <td>330833</td>
... <td>-3115</td>
... </tr>
... </table></body></html>
... """
>>> smtpObj = smtplib.SMTP('your smtp ip//192.168.207.211','25')
>>> smtpObj.sendmail(sender, receivers, message)

################### other way #############################

#!/usr/bin/env python

import smtplib
sender='gpecm@grameenphone.com'
receivers=['sana.islam@# XXX: .com','kamonashis@xxxxxxxxx.com']
smtpObj = smtplib.SMTP('192.168.207.211','25')

with open('/usr/local/scripts/pendingRecord.html', 'r') as myfile:
     data = myfile.read()

smtpObj.sendmail(sender, receivers, data)
print data;
