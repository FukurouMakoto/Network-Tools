from functions import *


def main():
	#ip_address = input("Please enter your ip address: ")
	#CIDR = input("Please enter your network mask in CIDR notation: ")
	ip_address = get_ip_address()
	subnet = get_subnet()
	#subnet = supply_subnet(subnet)
	data_format(ip_address,subnet)

if __name__ == '__main__':
	main()

