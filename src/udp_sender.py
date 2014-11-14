# 
# Python UDP message sender.
# 
import socket
import argparse

if __name__ == '__main__':
    #-------------------------------------------------------------------
    # Parser
    #-------------------------------------------------------------------
    parser = argparse.ArgumentParser() 
    parser.add_argument ('-a', '--multicast_addr', default = '224.0.0.1',  help = 'Multicast group address.')
    parser.add_argument ('-p', '--multicast_port', default = 10000, help = 'Multicast group port.')
    
    parser.add_argument ('-m', '--message', required = True,  help = 'The UDP message.')
    args = parser.parse_args()
    
    #-------------------------------------------------------------------
    # Sending message with UDP
    #-------------------------------------------------------------------
    multicast_addr = str(args.multicast_addr)
    multicast_port = int(args.multicast_port)
    udp_message = args.message.encode()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.sendto(udp_message, (multicast_addr, multicast_port))




