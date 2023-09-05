from encryption_module import EncryptionModuleInterface

class Encryptor:

    def __init__(self, encryption_module:EncryptionModuleInterface) -> None:
        self.encryption_module = encryption_module
        self.key = bytes()

    def encrypt(self, plain_data:bytes) -> bytes:



        return self.encryption_module.encrypt(self.key, plain_data)

    def decrypt(self, encrypted_data:bytes) -> bytes:


        return self.encryption_module.decrypt(self.key, encrypted_data)

    def set_key(self, new_key:bytes):

        # TODO: Add some new key validations.
        self.key = new_key