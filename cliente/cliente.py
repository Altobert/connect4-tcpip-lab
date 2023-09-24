
'librerias autorizadas'
import socket
import sys

objetoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

datos_servidor = ('localhost', 10000)
print >>sys.stderr, 'conectando a %s puerto %s' % datos_servidor
socket.connect(datos_servidor)


try:
     mensaje = 'Aquí va el mensaje'
     print >>sys.stderr, 'enviando "%s"' % mensaje
     objetoSocket.sendall(mensaje) # enviando el mensaje
 
     cantidad_recibida = 0
     cantidad_esperada = len(mensaje) # recibiendo la respuesta
 
     while cantidad_recibida < cantidad_esperada: 
        data = objetoSocket.recv(19) 
        cantidad_recibida += len(data) 
        print >>sys.stderr, 'recibiendo "%s"' % data

finally:
     print >>sys.stderr, 'cerrando socket'
     objetoSocket.close()