from functions import *


def main():
	#ip_address = input("Please enter your ip address: ")
	#CIDR = input("Please enter your network mask in CIDR notation: ")
	args = parse_cli()
	ip_address = get_ip_address(args)
	subnet = get_subnet(args)
	#subnet = supply_subnet(subnet)
	data_format(ip_address,subnet)

if __name__ == '__main__':
	main()

