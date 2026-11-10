from app.utils import encrypt_with_public_key, decrypt_with_private_key, RSAUtil

class AuthUtils:
    
    def __init__(self):
        self.public_key = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp5a7V/IWYbttPgaWRnma\nbB0n1UYNgews2P+VEVRWSCERRgVwtKZWlJGVHiGH1/59xdVXiAKaxumSQjFkdZsX\njMJRj2YeI4ZZ8AWqFa2Jk9jHdcFhbpxAIxq3wHsmF+jk1H1S9iGt837j2UDYkefN\n6zH60NhPSy2vE923mWH8GDb+ssS1wcgkzZJ+NKqs+6Kbp6+oLK+EXfTtNqY7hvsU\nvx6ayE/VUCbnvECmLyTBNBdAs3i2dwNs3zA7ha7v6PkZV2FqyWuOYq8PRN3iCUpw\n8WpUUJzjYinobS7pkD3J+o0EtQ5oFy8ahPO2vi+igVTFIjQW8+vGayxIkh1uldcv\nMwIDAQAB\n-----END PUBLIC KEY-----'
        self.private_key = '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAp5a7V/IWYbttPgaWRnmabB0n1UYNgews2P+VEVRWSCERRgVw\ntKZWlJGVHiGH1/59xdVXiAKaxumSQjFkdZsXjMJRj2YeI4ZZ8AWqFa2Jk9jHdcFh\nbpxAIxq3wHsmF+jk1H1S9iGt837j2UDYkefN6zH60NhPSy2vE923mWH8GDb+ssS1\nwcgkzZJ+NKqs+6Kbp6+oLK+EXfTtNqY7hvsUvx6ayE/VUCbnvECmLyTBNBdAs3i2\ndwNs3zA7ha7v6PkZV2FqyWuOYq8PRN3iCUpw8WpUUJzjYinobS7pkD3J+o0EtQ5o\nFy8ahPO2vi+igVTFIjQW8+vGayxIkh1uldcvMwIDAQABAoIBABRdLQOZP539k98r\nFryWjyye+FWijwagB60QlXEHIfrexcYP6CuTYMbpz8hbA7I70tWkwF+fDWapQCP5\n836U624nuJhnrLbdXvVbAtlifmqwN0B4UJoLs4FwgC6L6EuUeaXWWqvc2NHTM+WU\nyxwjojJ3nsYc2rnEYddUpDgnn2XjqnwZWsvQeU1MixtkH2wkESw2UVZjcA1cW8zr\n41VEd2D/JOPY+B6ZUcT5jlesL6M4cfphnnFMAEE3BHNttMAO7pwWtmHyu2LtS57g\nya1zrh/Jb8SZW8NbUA+jFtnr3B24dJtg9ox9j6KsVjbh8JsKEl3iglF346PwjzGr\nBEod1skCgYEAxz+NS31IEBF4Kz7hemlujO0pSGEj+sD88HOWKBrBtrYcryOOiqd0\nCfKQBZPKjwONNHPnonLwbcYcCIAkoLY8on8Wq6nHwOXHTWiIaEQnSNrvKpaQgNBE\nulgANf8zQHtccArwnY/q7QTum9AIP1BG2Jb7O1KNgHtP/9iHGR3TTZkCgYEA11Kw\nb0LNztK09/iXZGwPyTfyCCP8317xz1yjL9n6sVQRuWYKmmmlHKAIkgl8Y+ASzzky\n1G64+/DOc6d9eiM8UnyAvOJdV65r4OimJVx9CUa7NqYIc5WrhxD7ghvLpBRdNLIq\nt2cRYcdzY1FKCr2gRlS0kV9M2KCxYUs0cti5aqsCgYAtUuuVTH5kCVVIoRkxe2JG\ndHx7ln1UwSnImMKDhPKj2XFU9cWrDMR8rszMN/5P4gLw95yte2/tyK7/0AaE+G96\nl2ZUzl4+JwbbOPgun7JABG17RpzAcJ/xs6r4nYDPHkC8zABIF0Ddgc21a/E0VdKH\n2nBz4ieGHoboMB0rPXmfoQKBgQC2RHS9edslXA98aJ4ej6q9NfJXGb+QhZpDYbNx\nah9fxD5MpigLlaoClSUsGYOGN8M0TsLMN/22ppzcIceBgBor6OBBA4zoD+mZtNYP\ngj8Ffy4ykFFPJj7QUnvUIxs6hVJwrPCj10dLcb4nMERw2xu07Tb8Z6NxLHV6WmLH\nZNVviQKBgCQ6jizCtRCvQjsngKjelnpqxC5zbI2Ec/rOGHmFl6Nsne2S4KMQstCa\n6xwOWMdeIRWkVFXBijmXfhvYHXk7amxjyNLRNPPq1DK45ip5FdvxAtSrTMhW7A9b\ncGqm3y8lsWFOhBgntdr+PWKPZDWHbrXTCRZSc8E/7b0Lc/r9670y\n-----END RSA PRIVATE KEY-----'
        self.rsa_util = RSAUtil()
        self.rsa_util.load_public_key(self.public_key)
        self.rsa_util.load_private_key(self.private_key)
        return None
        return None

    
    def encrypt(self, data_str):
        return self.rsa_util.encrypt(data_str)
        return None

    
    def decrypt(self, data_str):
        return self.rsa_util.decrypt(data_str)
        return None

    
    def sign(self, data_str):
        return self.rsa_util.sign(data_str)
        return None

    
    def verify(self, data_str, signature):
        return self.rsa_util.verify(data_str, signature)
        return None


if __name__ == '__main__':
    re = AuthUtils().encrypt('你好啊')
    print(re)
    ree = AuthUtils().decrypt(re)
    print(ree)
    re = AuthUtils().sign('你好啊')
    print(re)
    ree = AuthUtils().verify('你好啊', re)
    print(ree)

