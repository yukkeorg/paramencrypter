import pytest
from Crypto.Random import get_random_bytes

from paramencrypter.PE import ParamEncrypter


def test_paramencrypter():
    key = get_random_bytes(16)
    nonce = get_random_bytes(16)

    pe = ParamEncrypter(key, nonce)

    data = "uid=AA12345&pno=09012345678"

    encoded_data = pe.encode(data)
    decoded_data = pe.decode(encoded_data)

    assert data == decoded_data
