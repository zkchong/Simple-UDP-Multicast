import socket
import struct
import argparse

if __name__ == '__main__':
    #-------------------------------------------------------------------
    # Parser
    #-------------------------------------------------------------------
    parser = argparse.ArgumentParser() 
    parser.add_argument ('-a', '--multicast_addr', default = '224.0.0.1',  help = 'Multicast group address.')
    parser.add_argument ('-p', '--multicast_port', default = 10000, help = 'Multicast group port.')
    parser.add_argument ('-b', '--buffer_size', default = 4096, help = 'Buffer size.')
    
    args = parser.parse_args()
    
    #-------------------------------------------------------------------
    # Listen to incoming message
    #-------------------------------------------------------------------
    multicast_addr = str(args.multicast_addr)
    multicast_port = int(args.multicast_port)
    buffer_size = int(args.buffer_size)
    
    # Setup listener to multicast addr.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((multicast_addr, multicast_port))
    mreq = struct.pack("4sl", socket.inet_aton(multicast_addr), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print ('# Listening UDP message on %s:%s.' % (multicast_addr, multicast_port))

    while True:
        data, addr  = sock.recvfrom(buffer_size)
        print ('Received: "%s" from %s' % (data, addr))
