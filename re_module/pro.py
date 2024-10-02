'''
Write a function that extracts all valid IP addresses 
from a given text using regular expressions.
'''

from re import findall

def extract_ip_address(text):
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    ip_address = findall(pattern, text)

    valid_ips = [ip for ip in ip_address if all(0 <= int(octet) <= 255 for octet in ip.split('.'))]

    return valid_ips

if __name__ == '__main__':
    text = "Some random text with IPs like 192.168.1.1, 256.300.1.1, and 10.0.0.255, plus invalid ones like 999.999.999.999."
    print(f"Valid IP address found: {extract_ip_address(text)}")

