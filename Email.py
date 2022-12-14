import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def email():
    # Создание объекта
    msg = MIMEMultipart()

    message = "Письмо отправлено из PyCharm"

    # Установка параметров сообщения
    password = 'Pj8B372zDvZJGgpNCyfv'
    msg['From'] = "karyamba@bk.ru"
    msg['To'] = 'karyamba@bk.ru'
    msg['Subject'] = 'Бот вышел в онлайн'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(host='smtp.mail.ru', port=587)

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))
