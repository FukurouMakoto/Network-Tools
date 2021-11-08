# Network-Tools
A handy script for quickly finding network information. With just an IP address and your Subnet's CIDR, you can quickly find your subnet  mask, network address, broadcast address, and your usable IP range.

### Instructions
1) Clone project
2) run main.py

### Command-Line Arguments
--help
Print help menu to CLI.

--ip
Supply an IP address from your network.

--cidr
Provide the appropriate CIDR for your network. Please do not provide subnet if you are providing cidr.

--subnet
Provide the subnet mask for your network. Please do not provide CIDR if you are providing subnet.

### Recent Features
Project now uses Sys-Args to provide command line arguements. Results are now returned to the command line, which means they can now be redirected to a text file if you are using Linux. 

### Future Additions
I would like to eventually create a GUI program for this. Also considering making a Java version as well for practice.
