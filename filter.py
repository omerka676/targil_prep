from enum import Enum
from scapy import *

class Verifier(Enum):
    ENCRYPT = 1 
    DECRYPT = 2
    NOT_VALID = 3


class Filter():
    def filter(self, pkt) -> Verifier:
        return Verifier.NOT_VALID 

    def _filter_ip_layer(self, ip_layer) -> Verifier:
        return Verifier.NOT_VALID
    
    def _filter_ports(self, pkt) -> bool:
        return False