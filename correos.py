import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del correo
correo_origen = 'satlanacional@gmail.com'
correo_smtp = 'smtp.gmail.com'
puerto_smtp = 587

# Obtener la contraseña de aplicación de manera segura
contraseña = getpass.getpass('Introduce tu contraseña de aplicación de Google: ')

# Obtener el destinatario y el mensaje
correo_destino = input('Introduce el correo del destinatario: ')
asunto = input('Introduce el asunto del correo: ')
mensaje = input('Introduce el mensaje del correo: ')

# Crear el mensaje
msg = MIMEMultipart()
msg['From'] = correo_origen
msg['To'] = correo_destino
msg['Subject'] = asunto
msg.attach(MIMEText(mensaje, 'plain'))

try:
    # Conectar al servidor SMTP
    server = smtplib.SMTP(correo_smtp, puerto_smtp)
    server.starttls()
    server.login(correo_origen, contraseña)
    
    # Enviar el correo
    server.sendmail(correo_origen, correo_destino, msg.as_string())
    print('Correo enviado exitosamente')
    
except Exception as e:
    print(f'Ocurrió un error: {e}')
    
finally:
    server.quit()
