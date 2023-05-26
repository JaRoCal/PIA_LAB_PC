# PRACTICA12_1970947

## Esta practica tuvo el objetivo de realizar ejercicios en Python para la conexión y posterior envío de correos electrónicos.

### Gmail App Password 
Primero tuvimos que obtener una password de aplicación para poder saltarnos la verificación en dos pasos de nuestra cuenta para poder utilizar nuestra cuenta de Gmail, esto se hace en el siguiente link: 
https://myaccount.google.com/apppasswords

### Probando envíos en IDLE 
Aqui abrimos una ventana de Python IDLE y probamos si funciona la contraseña de aplicación 
creada anteriormente además validaremos la comunicación con el servidor de correo de Gmail. 
En la ventana de IDLE realizamos la ejecución de los siguientes comandos:
~~~
import smtplib
conn = smptlib.SMTP(‘smtp.gmail.com’, 587)
conn.ehlo()
~~~
Después de establecer el saludo inicial, iniciamos una sesión TLS:
~~~
conn.starttls()
~~~
Después proporcionamos la información de acceso, nuestra cuenta de Gmail y la contraseña de app 
creada previamente: 
~~~
conn.login(‘aquí va tu correo@gmail.com’, ‘aquí tu contraseña app’)
~~~
Una vez aceptadas las credenciales hicimos una prueba de envió sencilla, en una sola línea:
~~~
conn.sendmail(‘origen@gmail.com’,’destino@dominio’,’Subject: TestPractica10\n\nHola\n\n Prueba de <matricula> - <Nombre>’) 
~~~
Al final cerramos la conexión:
~~~
conn.quit()
~~~
Al final se solicito un scrip que mande correos electronicos adjuntando una imagen y ese script está a continuación...


___
### En esta sección se encuentran el script relacionado con el envío de correos electrónicos. A continuación el código y su explicación:
___

##SCRIPT
~~~
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
~~~

##EXPLICACIÓN DEL CODIGO
### Primero importamos los modulos necesarios:

~~~
import smtplib,ssl
import getpass
~~~
smtplib: Proporciona una interfaz para enviar correos electrónicos utilizando el protocolo SMTP.

ssl: Proporciona herramientas para trabajar con conexiones seguras.

getpass: Proporciona una forma segura de solicitar al usuario la contraseña sin mostrarla en la consola.

~~~
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
~~~
email.encoders: Contiene funciones para codificar archivos adjuntos en mensajes de correo electrónico.

email.mime.base: Proporciona clases para crear partes base de mensajes MIME.

email.mime.text: Proporciona una clase para crear partes de texto MIME.

email.mime.multipart: Proporciona una clase para crear partes multiparte MIME.

### Después se le olicita al usuario los datos necesarios para iniciar sesión en el correo electrónico desde el cual se enviarán los mensajes, como el correo electrónico del usuario, la contraseña, el destinatario y el asunto.
~~~
correo_de_usuario = input("Ingresar tu correo: ")
contraseña = input("ingresa la contraseña: ")
destinatario = input("Ingrese destinatario: ")
asunto = input("Ingrese asunto: ")
~~~

### Se crea un objeto MIMEMultipart que representa el mensaje de correo electrónico. Se configuran los encabezados como el asunto, el remitente y el destinatario.

### Define el contenido del correo electrónico en formato HTML. El código HTML se encuentra dentro de una cadena de texto multilínea.

### Crea una parte MIME para el contenido HTML utilizando MIMEText. El contenido HTML se pasa como primer argumento y se especifica que es HTML mediante el segundo argumento "html".

### Adjunta la parte HTML al mensaje utilizando el método attach() del objeto MIMEMultipart.

~~~
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
mensaje.attach(parte_html)
~~~

### Solicita al usuario la ubicación del archivo que se adjuntará al correo electrónico.

### Abre el archivo en modo lectura binaria y crea un objeto MIMEBase con el tipo de contenido "application/octet-stream". El archivo se lee y se establece como carga útil del objeto MIMEBase.

### Codifica el contenido del archivo adjunto en base64 utilizando encoders.encode_base64().

### Agrega el encabezado "Content-Disposition" a la parte adjunta. El nombre del archivo se extrae de la ubicación del archivo proporcionada por el usuario.

~~~
archivo = input("ubicacion del archivo a enviar   :   ") 
with open(archivo,"rb") as adjunto:
    contenido_adjunto = MIMEBase("application", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)
contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}",
)
~~~
### Adjunta la parte del archivo codificado al mensaje utilizando el método attach() del objeto MIMEMultipart.

### Convierte el mensaje completo a una cadena de texto utilizando el método as_string() del objeto MIMEMultipart. Esto es necesario para enviar el mensaje a través de SMTP.

~~~
mensaje.attach(contenido_adjunto)
mensaje_final = mensaje.as_string()
~~~

### Crea un contexto SSL utilizando ssl.create_default_context().

### Establece una conexión segura con el servidor SMTP de Gmail utilizando smtplib.SMTP_SSL(). Se proporciona el host ("smtp.gmail.com") y el puerto (465) correspondientes a Gmail.

### Inicia sesión en la cuenta de correo electrónico utilizando el método login() del objeto SMTP_SSL. Se proporciona el correo electrónico del usuario y la contraseña.

### Envía el correo electrónico utilizando el método sendmail() del objeto SMTP_SSL. Se proporcionan el correo electrónico del remitente, el destinatario y el mensaje en formato de cadena.

~~~
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(correo_de_usuario,contraseña)
    server.sendmail(correo_de_usuario, destinatario, mensaje_final)
~~~
### En resumen, el código permite enviar un correo electrónico utilizando el protocolo SMTP y adjuntar un archivo. Se utilizan las bibliotecas smtplib, ssl, getpass, email.encoders y las clases MIMEMultipart, MIMEText y MIMEBase para lograrlo.
