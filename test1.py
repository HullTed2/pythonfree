from __future__ import print_function, unicode_literals

print("Hello World")
ip_addr1 = '8.8.8.8'
print(ip_addr1)


try:
    ip_addr = raw_input("Enter an IP address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")
    
print(ip_addr)
