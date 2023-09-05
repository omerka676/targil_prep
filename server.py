from packet_handler import Filter, PacketHandler, XorModule 

def main():
    module = XorModule(b'\x67')
    filter = Filter()
    handler = PacketHandler(filter, module)
    handler.run()

main()