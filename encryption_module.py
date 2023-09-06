
class EncryptionModuleInterface:
    
    @staticmethod
    def encrypt(key:bytes, plain_data:bytes) -> bytes:
        """
        Encrypt plain data with key in the same size.
        """
        return bytes()

    @staticmethod
    def decrypt(key:bytes, encrypted_data:bytes) -> bytes:
        """
        Decrypt encrypted data with key in the same size.
        """
        return bytes()
        

class XorEncryptionModule(EncryptionModuleInterface):

    @staticmethod
    def xor_bytes(key, value):
        return bytes([_a ^ _b for _a, _b in zip(key, value)])


    @staticmethod
    def encrypt(key:bytes, plain_data:bytes) -> bytes:
        return XorEncryptionModule.xor_bytes(plain_data, key)

    @staticmethod
    def decrypt(key:bytes, encrypted_data:bytes) -> bytes:
        return XorEncryptionModule.xor_bytes(encrypted_data, key)
    