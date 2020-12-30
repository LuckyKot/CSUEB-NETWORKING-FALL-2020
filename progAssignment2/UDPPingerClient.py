from datetime import datetime
from socket import *

s = socket(AF_INET, SOCK_DGRAM)

address = '192.168.1.72'
port = 3228

message = "message "
sequence_number = 0
while sequence_number < 10:
    sequence_number = sequence_number + 1
    print sequence_number
    ping = ' '
    time = datetime.now()
    ping = message + str(sequence_number) + ' ' + str(time)
    s.sendto(ping, (address, port))
    s.settimeout(1)
    try:
        response, sa = s.recvfrom(1024)
        print response
        newtime = datetime.now()
        newtime = newtime - time
        print 'response time (RTT):' + str(newtime)
    except timeout:
        print 'Request time out'