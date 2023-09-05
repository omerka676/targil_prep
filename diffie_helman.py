from scapy.all import *
import socket
import math

SHARED_PRIME = 23
BASE = 5 

LOCAL_HOST = "127.0.0.1"
PORT = 9001

DST_IP = "127.0.0.1"
DST_PORT = 9001

class KeyExchange(): 
    def __init__(self,is_master, shared_base, shared_prime, key) -> None:
        self.shared_prime = shared_prime
        self.shared_base = shared_base
        self.secret = key
        self.is_master = is_master

    def perform_key_exchange(self, dst_ip, dst_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.is_master:
            return self.master_handshake(sock, LOCAL_HOST, PORT)
        else:
            return self.slave_handshake(sock,LOCAL_HOST, PORT )
    
    def calculate_public_key(self):
        return math.pow(self.shared_base, self.secret) % self.shared_prime

    def calculate_private_key(self, public_key):
        return math.pow(public_key,self.secret) % self.shared_prime


    def slave_handshake(self, sock, src_ip, src_port):
        sock.bind((src_ip, src_port))
        sock.listen(1)
        sock.accept()
        public_secret = sock.recv(256)
        sock.send(self.calculate_public_key())
        sock.close()

        return self.calculate_private_key(public_secret)

    def master_handshake(self, sock, dst_ip, dst_port):
        sock.connect((dst_ip, dst_port))
        sock.sendall(self.calculate_public_key())
        public_secret = sock.recv(256)
        sock.close()
        return self.calculate_private_key(public_secret)
