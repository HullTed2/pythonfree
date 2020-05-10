#!/usr/bin/env python
from __future__ import print_function, unicode_literals

#String formatting examples

ip_addr1 = '172.16.1.1'
ip_addr2 = '192.168.10.3'
ip_addr3 = '10.3.5.99'

print(ip_addr1,ip_addr2,ip_addr3)

# Green curly braces are formating to variables and creating 20 columns

print('\n')
print('-' * 80)
print('{my_ip:^20}{ip:^20}{ip_alt:>20}'.format(ip_alt=ip_addr1, ip=ip_addr2, my_ip=ip_addr3))
print('-' * 80)
print('\n')

# Splitting teh ip address and prinint out

octets = ip_addr1.split('.')

print('\n')
print('-' * 80)
print('{:10}{:10}{:10}{:10}'.format(octets[0], octets[1], octets[2], octets[3]))
print('-' * 80)
print('\n')

# more efficent way to print the list out *

print('\n')
print('-' * 80)
print('{:10}{:10}{:10}{:10}'.format(*octets))
print('-' * 80)
print('\n')

# Old way to do it, teh format method as replaced below method

print('\n')
print('-' * 80)
print('%s %s' % (ip_addr1, ip_addr2))
print('-' * 80)
print('\n')

# Only in 3.6 and above you can use f,

port1 = 80

print('\n')
print('-' * 80)
print(f'My IP address is: {ip_addr1:^20} {port1:^8}')
print('-' * 80)
print('\n')
