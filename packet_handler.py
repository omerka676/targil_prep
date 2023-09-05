from itertools import filterfalse
from scapy.all import *
from filter import Filter, Verifier
from xor_module import XorModule

class PacketHandler(): 
    def __init__(self, packet_filter : Filter, encryption_module : XorModule) -> None:
        self.filter = packet_filter
        self.encryption_module = encryption_module


    def handle_packets(self, pkt):
        filter_res = self.filter.filter()
        if filter_res == Verifier.NOT_VALID:
            return
        
        if filter_res == Verifier.ENCRYPT:
            payload = self.encryption_module.encrypt(bytes(pkt[RAW].payload))
        else:
            payload = self.encryption_module.decrypt(bytes(pkt[RAW].payload))

        pkt[RAW].payload = payload
        #change mac
        
        send(pkt)    
    
    def run(self):
        sniff(filter='tcp', prn=self.handle_packets)