from functions import *


def main():
	args = parse_cli()
	ip_address = get_ip_address(args)
	subnet = get_subnet(args)
	data_format(ip_address, subnet)


if __name__ == '__main__':
	main()
