import argparse


# TODO:
# We need to refactor the code to handle when classless subnets are being used.

def num_to_binary(num):  # Converts number provided to binary
    try:  # Catch integer values passed to num
        int(num)
    except ValueError:
        return "ERROR: You must enter a number!"
    else:
        x = []
        tests = [128, 64, 32, 16, 8, 4, 2, 1]
        if num > sum(tests):
            return "ERROR: Subnet Octets are limited to 255 bytes!"
        elif num == 0:
            return ''.join([str(0) * 8])
        elif num == 255:
            return ''.join([str(1) * 8])
        else:
            while num > 0:
                for item in tests:
                    if num >= item:
                        x.append(1)
                        num -= item
                    else:
                        x.append(0)

        return ''.join([str(i) for i in x])


def supply_subnet(subnet):  # IN PROGRESS
    if '.' in str(subnet):  # Will convert accept a subnet or convert CIDR into subnet
        return subnet
    else:
        return slash_to_subnet(subnet)


def ip_address_to_binary(address):  # Converts IP address to binary
    x = address.split('.')
    return '.'.join([num_to_binary(int(i)) for i in x])


def slash_to_subnet(slash):  # Converts CIDR notation to subnet
    x = []
    slash = int(slash)
    tests = [128, 64, 32, 16, 8, 4, 2, 1]
    while slash > 8:
        x.append(255)
        slash -= 8
    x.append(sum(tests[0:slash]))
    while len(x) != 4:
        x.append(0)
    return '.'.join([str(i) for i in x])


def find_network_address(address, slash):  # Finds the network address
    a = address.split('.')
    b = slash.split('.')
    c = []
    for i in range(0, 4):
        if b[i] == '255':
            c.append(a[i])
        elif b[i] == '0':
            c.append('0')
        else:
            interesting_octet = b.index(b[i])
            magic_number = get_magic_number(interesting_octet, b)
            c.append(get_interesting_octet_value_network(a, interesting_octet, magic_number))
    return '.'.join([str(i) for i in c])


def find_broadcast_address(ip_address, slash):  # Finds the broadcast address
    a = ip_address.split('.')  # IP Address
    b = slash.split('.')  # Subnet Mask
    c = []
    for i in range(0, 4):
        if b[i] == '255':
            c.append(a[i])
        elif b[i] == '0':
            c.append('255')
        else:
            interesting_octet = b.index(b[i])
            magic_number = get_magic_number(interesting_octet, b)
            c.append(get_interesting_octet_value_broadcast(a, interesting_octet, magic_number))
    return '.'.join([str(i) for i in c])


def get_magic_number(interesting_octet, subnet):
    magic_number = 256 - int(subnet[interesting_octet])
    return magic_number


def get_interesting_octet_value_broadcast(ip_address, interesting_octet, magic_number):
    return int(ip_address[interesting_octet]) + magic_number - 1


def get_interesting_octet_value_network(ip_address, interesting_octet, magic_number):
    return int(int(ip_address[interesting_octet]) / magic_number) * magic_number


def find_ip_range_start(network_address):  # Finds where the IP range begins
    a = network_address.split('.')
    a[3] = int(a[3]) + 1
    return '.'.join([str(i) for i in a])


def find_ip_range_end(broadcast_address):  # Finds where the IP range ends
    a = broadcast_address.split('.')
    a[3] = int(a[3]) - 1
    return '.'.join([str(i) for i in a])


def parse_cli():
    ip_help = "xxx.xxx.xxx.xxx format"
    cidr_help = "standard cidr format minus the / (24, 16 etc.)"
    subnet_help = "can enter full subnet mask here (255.255.255.0)"
    title = "Network-Tools"
    parser = argparse.ArgumentParser(description=title, prog=title)
    parser.add_argument('--ip', help=ip_help)
    parser.add_argument('--cidr', help=cidr_help)
    parser.add_argument('--subnet', help=subnet_help)
    args = parser.parse_args()
    return args


def get_ip_address(args):  # Returns ip address passed by user
    return args.ip


def get_subnet(args):  # Returns subnet passed by user
    # if '.' in sys.argv[2]:
    if args.subnet is None:
        return args.cidr.strip('/')
    elif args.cidr is None:
        return args.subnet
    elif args.subnet is not None and args.cidr is not None:
        return args.subnet


def data_format(ip_address, cidr):
    print(f"Supplied IP address: {ip_address}")
    print(f"Supplied subnet/CIDR: {cidr}")
    print(f"IP address in binary: {ip_address_to_binary(ip_address)}")
    subnet_mask = supply_subnet(cidr)  # To test new code replace cidr with supply_subnet(cidr)
    print(f"Subnet Mask: {supply_subnet(subnet_mask)}")
    network_address = find_network_address(ip_address, subnet_mask)
    print(f"Network address: {network_address}")
    broadcast_address = find_broadcast_address(network_address, subnet_mask)
    print(f"Broadcast address: {broadcast_address}")
    ip_range_start = find_ip_range_start(network_address)
    ip_range_end = find_ip_range_end(broadcast_address)
    print(f"Usable Host IP range: {ip_range_start} - {ip_range_end}")
