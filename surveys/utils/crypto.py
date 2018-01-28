import random
import string
import hashlib
import hmac
import base64
import re


def hmac_sha1_base64(text, key):
    key = bytes(key, 'utf-8')
    text = bytes(text, 'utf-8')
    hmac_digester = hmac.new(key, text, hashlib.sha1)
    digest = hmac_digester.digest()
    base64_encoded = base64.b64encode(digest)
    return str(base64_encoded, 'utf-8')


def percent_encoding(string):
    # see https://www.ietf.org/rfc/rfc3986.txt
    result = ''
    accepted = [c for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~'.encode('utf-8')]
    for char in string.encode('utf-8'):
        result += chr(char) if char in accepted else '%{}'.format(hex(char)[2:]).upper()
    return result


def percent_decoding(string):
    def substitute(match):
        hex_string = '0x{}'.format(match.group(0)[1:])
        ascii_number = int(hex_string, 0)
        return chr(ascii_number)
    return re.sub(r'%([\d\w]{2})', substitute, string)


def random_chars(n):
    # return n number of random characters as a string
    return ''.join(random.choice(string.ascii_letters) for x in range(n))
