import base64
import zlib
from Crypto.Cipher import AES


class ParamEncrypter:
    def __init__(self, key, nonce):
        self.key = key
        self.nonce = nonce

    def encode(self, params):
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce)

        params = params.encode('utf-8')
        params = zlib.compress(params)
        params = cipher.encrypt(params)
        result = base64.urlsafe_b64encode(params)
        return result

    def decode(self, encoded_params):
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.nonce)

        params = base64.urlsafe_b64decode(encoded_params)
        params = cipher.decrypt(params)
        params = zlib.decompress(params)
        result = params.decode('utf-8')
        return result

