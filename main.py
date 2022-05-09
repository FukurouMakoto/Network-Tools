#from test_rename import * For test refactoring
from functions import * #Full Version

def main():
	args = parse_cli()
	ip_address = get_ip_address(args)
	subnet = get_subnet(args)
	data_format(ip_address, subnet)


if __name__ == '__main__':
	main()
