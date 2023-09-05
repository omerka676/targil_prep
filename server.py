from packet_handler import Filter, PacketHandler, Encryptor
from encryption_module import XorEncryptionModule
import json
import logging

def main():
    module = Encryptor(XorEncryptionModule())
    filter = Filter()
    handler = PacketHandler(filter, module)
    handler.run()


main()