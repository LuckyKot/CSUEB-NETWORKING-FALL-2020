from socket import *

# if len(sys.argv) <= 1:
#    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
#    sys.exit(2)
# Create a server socket, bind it to a port and start listening

# in case you want to use it as specified above
# serAddr = sys.argv[1]

# Fill in start.
tcpSerSock = socket(AF_INET, SOCK_STREAM)
serAddr = '127.0.0.1'
serPort = 5555
tcpSerSock.bind((serAddr, serPort))
tcpSerSock.listen(5)
# Fill in end.
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)  # Fill in start. # Fill in end.
    message = message.decode()
    print("Message:" + message)
    # Extract the filename from the given message
    # print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print("Filename:" + filename)
    fileExist = "false"
    filetouse = "/" + filename
    print("Filetouse:" + filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        for msg in range(0, len(outputdata)):
            outputdata[msg] = outputdata[msg].encode()
            tcpCliSock.send(outputdata[msg])
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)  # Fill in start. # Fill in end.
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                print("connected")
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('rwb', None)
                print("created")
                request = ("GET /" + " HTTP/1.0\r\nHost: " + filename + "\r\n\r\n")
                print(request)
                request = request.encode()
                c.send(request)
                fileobj.write(request)
                # Read the response into buffer
                # Fill in start.
                buffer = fileobj.readlines()
                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                # Fill in start.
                for line in buffer:
                    tmpFile.write(line)
                    tcpCliSock.send(line)
            # Fill in end.
            except:
                print("Illegal request")
        else:
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n".encode())
            tcpCliSock.send("Content-Type:text/html\r\n".encode())
            tcpCliSock.send("\r\n".encode())
    # HTTP response message for file not found
    # Fill in start.
    # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
# Fill in end
