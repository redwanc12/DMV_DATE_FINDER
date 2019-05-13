import smtplib
from check_avail import openFinder
from token_finder import tokenFinder

for i in range(10):

    data = tf.nextDayWithOpens()

    of = openFinder()
    dates = of.findDates(data)

    
    for each in dates:
        body += (each['openings'] + ' Opening at ' + each['time'] + ' at ' + each['location'] + ' on ' + each['day'] + '\n')


class notif(object):
    def __init__(self):
        self.email = n/a
        self.password = n/a
        self.tf = tokenFinder()
        self.tf.authenticateClient()
    
    def logIn(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(self.email, self.password)

    def sendEmail(self, subject, body):
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                msg = f'Subject: {subject}\n\n{body}'
                smtp.sendmail(self.email, 'redwanc12@gmail.com@gmail.com', msg)

    def dateToBody(self, date):
        body = ''
        for each in dates:
            body += (each['openings'] + ' Opening at ' + each['time'] + ' at ' + each['location'] + ' on ' + each['day'] + '\n')
        return body

    def close(self):
        self.tf.closeDriver()
    