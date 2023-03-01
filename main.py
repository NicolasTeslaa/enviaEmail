from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "texto dentro do email"

#parâmetros
senha = "adsawdasd"
msg['From'] = "quem envia"
msg['To'] = "quem recebe"
msg['Subject'] = "assunto"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')