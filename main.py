from functions import *

def main():
	#ip_address = input("Please enter your ip address: ")
	#CIDR = input("Please enter your network mask in CIDR notation: ")
	ip_address = input("Please enter your ip address: ")
	subnet = input("Please enter your subnet mask in CIDR notation: ")
	#subnet = supply_subnet(subnet)
	format(ip_address,subnet)  

if __name__ == '__main__':
	main()

