def num_to_binary(num):
	x = []
	tests = [128, 64, 32, 16, 8, 4, 2, 1]
	if num > sum(tests):
		return "ERROR: Subnet Octets are limited to 255 bytes!"
	elif num == 0:
		return ''.join([str(0) for i in range(0, 8)])
	elif num == 255:
		return ''.join([str(1) for i in range(0, 8)])
	else:
		while num > 0:
			for item in tests:
				if num >= item:
					x.append(1)
					num -= item
				else:
					x.append(0)

	return ''.join([str(i) for i in x])
def supply_subnet(subnet):
	if '.' in subnet:
		return subnet
	else:
		return slash_to_subnet(slash)

def ip_address_to_binary(address):
	x = address.split('.')
	return '.'.join([num_to_binary(int(i)) for i in x])

def slash_to_subnet(slash):
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

def find_network_address(address, slash):
	a = address.split('.')
	b = slash_to_subnet(slash).split('.')
	c = []
	for i in range(0, 4):
		if b[i] == '255':
			c.append(a[i])
		elif b[i] == '0':
			c.append('0')
		else:
			c.append('1')
	return '.'.join([str(i) for i in c])

def find_broadcast_address(ip_address, slash):
	a = ip_address.split('.') 
	b = slash_to_subnet(slash).split('.')
	c = []
	for i in range(0, 4):
		if b[i] == '255':
			c.append(a[i])
		elif b[i] == '0':
			c.append('255')
		else: 
			c.append('1')
	return '.'.join([str(i) for i in c])
def find_ip_range_start(network_address):
	a = network_address.split('.')
	a[3] = int(a[3]) + 1
	return '.'.join([str(i) for i in a])
def find_ip_range_end(broadcast_address):
	a = broadcast_address.split('.')
	a[3] = int(a[3]) - 1
	return '.'.join([str(i) for i in a])
def format(ip_address, CIDR):
	print(f"Supplied IP address: {ip_address}")
	print(f"Supplied slash CIDR: {CIDR}")
	print(f"IP address in binary: {ip_address_to_binary(ip_address)}")
	subnet_mask = slash_to_subnet(CIDR)
	print(f"Subnet Mask: {slash_to_subnet(CIDR)}")
	network_address = find_network_address(ip_address, CIDR)
	print(f"Network address: {network_address}")
	broadcast_address = find_broadcast_address(ip_address, CIDR)
	print(f"Broadcast address: {broadcast_address}")
	ip_range_start = find_ip_range_start(network_address)
	ip_range_end = find_ip_range_end(broadcast_address)
	print(f"Usable Host IP range: {ip_range_start} - {ip_range_end}")	
