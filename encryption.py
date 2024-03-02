import hashlib

class Encryption:
    def convert(Self,data):
        data=hashlib.md5(data.encode())
        data=data.hexdigest()
        return data