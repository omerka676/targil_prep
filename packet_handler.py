from itertools import filterfalse
from scapy.all import *
from filter import Filter, Verifier
from encryptor import Encryptor

class PacketHandler:

    def __init__(self, packet_filter:Filter, encryption_module:Encryptor, opposite_enc_ip:str) -> None:
        self.filter = packet_filter
        self.encryption_module = encryption_module
        self.opposite_enc_ip = opposite_enc_ip


    def handle_packets(self, pkt):
        filter_res = self.filter.filter(pkt)
        if filter_res == Verifier.NOT_VALID:
            return
        
        if filter_res == Verifier.ENCRYPT:
            # Copy all the packet from ip layer
            pkt = pkt[IP]
            
            encrypted_packet = self.encryption_module.encrypt(bytes(pkt))
            new_packet = Ether()/IP(dst=self.opposite_enc_ip)
            new_packet.add_payload(encrypted_packet)
        else:
            decrypted_packet = self.encryption_module.decrypt(pkt[Raw].load)
            new_packet = Ether()
            new_packet = bytes(new_packet) + decrypted_packet

        #change mac
        
        send(new_packet)    
    
    def run(self):
        sniff(filter='tcp', prn=self.handle_packets)