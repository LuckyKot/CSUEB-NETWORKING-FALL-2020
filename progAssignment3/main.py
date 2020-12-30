from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587) # Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


tls = "STARTTLS \r\n"
clientSocket.send(tls.encode())
recvTls = clientSocket.recv(1024)
print("TLS response: ", recvTls)

secureClientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

username = "*email goes here*"
credentials = ("\x00" + username + "\x00" + input("Password: ")).encode()
credentials = base64.b64encode(credentials)
authMsg = "AUTH PLAIN ".encode() + credentials + "\r\n".encode()
secureClientSocket.send(authMsg)
recvAuth = secureClientSocket.recv(1024)
print(recvAuth.decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <*mail here*> \r\n"
secureClientSocket.send(mailFrom.encode())
recvMF = secureClientSocket.recv(1024)
print("MAIL FROM response: ", recvMF)

# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
RCPT = "RCPT TO: <*mail here*> \r\n"
secureClientSocket.send(RCPT.encode())
recvRCPT = secureClientSocket.recv(1024)
print("RCPT TO response: ", recvRCPT)
# Fill in end
# Send DATA command and print server response.
# Fill in start
dataReq = "DATA \r\n"
secureClientSocket.send(dataReq.encode())
recvData = secureClientSocket.recv(1024)
print("DATA response: ", recvData)
# Fill in end
# Send message data.
# Fill in start
secureClientSocket.send((msg+'\r\n'+endmsg).encode())
recvSent = secureClientSocket.recv(1024)
print("Sent response: ", recvSent)
# Fill in end
# Message ends with a single period.
# Fill in start
#clientSocket.send(endmsg.encode())
#recvDot = clientSocket.recv(1024)
#print("Dot response: ", recvDot)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
dataReq = "QUIT \r\n"
secureClientSocket.send(dataReq.encode())
recvQuit = secureClientSocket.recv(1024)
print("QUIT response: ", recvQuit)
clientSocket.close()
secureClientSocket.close()
# Fill in end