import smtplib
from email.message import EmailMessage
import datetime
from email.mime.application import MIMEApplication

def backup():
    msg = EmailMessage()
    now = datetime.datetime.now()

    password = 'Pj8B372zDvZJGgpNCyfv'
    msg['From'] = "karyamba@bk.ru"
    msg['To'] = 'karyamba@bk.ru'
    msg['Subject'] = 'Резервная копия пиццы'
    filename = 'tiny_pizza.db'
    db = MIMEApplication(open('tiny_pizza.db','rb').read())
    db.add_header('Content-Disposition','attachment',filename='tiny_pizza.db')

    msg.set_content(f'Копия базы на эту дату {now}')
    # msg.attach(db)
    msg.add_attachment(open(filename).read())

    server = smtplib.SMTP(host='smtp.mail.ru', port=587)
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()


