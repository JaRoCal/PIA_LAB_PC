#Jaime Ronaldo Calderon Sanchez 1970947
import smtplib,ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Peticion de datos para iniciar sesión desde el correo que queramos mandar mensajes
correo_de_usuario = input("Ingresar tu correo: ")
contraseña = input("ingresa la contraseña: ")
destinatario = input("Ingrese destinatario: ")
asunto = input("Ingrese asunto: ")

#Creacion de un mensaje en html
mensaje = MIMEMultipart("alternative")
mensaje["Subject"] = asunto
mensaje["From"] = correo_de_usuario
mensaje["To"] = destinatario

html = f"""
<html>
<body>
    <b> PIA </b><br><br>
    Puertos.<br><br>
    <b>Equipo:</b> Jaime Ronaldo Calderon Sanchez<br><br>
    <b>Matricula:</b> 1970947<br>
</body>
</html>
"""
parte_html = MIMEText(html, "html")

#Agregar el html a mensaje 
mensaje.attach(parte_html)

#Ubicacion de la imagen a adjuntar 
archivo = input("ubicacion del archivo a enviar   :   ") 

#Codificacion de la imagen de forma estandar 
with open(archivo,"rb") as adjunto:
    contenido_adjunto = MIMEBase("application", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)
contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}",
)

#Agregar la imagen codificada a mensaje
mensaje.attach(contenido_adjunto)
mensaje_final = mensaje.as_string()

#Se envia el correo
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(correo_de_usuario,contraseña)
    server.sendmail(correo_de_usuario, destinatario, mensaje_final)
