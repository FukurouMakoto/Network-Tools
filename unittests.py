import unittest
import main

class test_network_tools(unittest.TestCase):

	def test_num_to_binary(self):
		#Properly convert proper numbers	
		self.assertEqual(main.num_to_binary(192),"11000000")
		self.assertEqual(main.num_to_binary(168),"10101000")
		self.assertEqual(main.num_to_binary(1),"00000001")
		self.assertEqual(main.num_to_binary(252),"11111100")

		# Properly raise errors for numbers greater than 255		
		self.assertEqual(main.num_to_binary(300),"ERROR: Subnet Octets are limited to 255 bytes!")
		self.assertEqual(main.num_to_binary(400),"ERROR: Subnet Octets are limited to 255 bytes!")
		self.assertEqual(main.num_to_binary(358),"ERROR: Subnet Octets are limited to 255 bytes!")
		self.assertEqual(main.num_to_binary(256),"ERROR: Subnet Octets are limited to 255 bytes!")

		#Properly raise errors for non-integer inputs
		self.assertEqual(main.num_to_binary("My name is Bob"),"ERROR: You must enter a number!")
		self.assertEqual(main.num_to_binary("My name is Bobby Shmurda"),"ERROR: You must enter a number!")
		self.assertEqual(main.num_to_binary("I just want to be a llama"),"ERROR: You must enter a number!")

		#Properly convert string numbers into integers
		self.assertEqual(main.num_to_binary("8"),"00001000")
		self.assertEqual(main.num_to_binary("16"),"00010000")
		self.assertEqual(main.num_to_binary("24"),"00011000")
		self.assertEqual(main.num_to_binary("32"),"00100000")

		#Properly raise error in slightly unique case
		self.assertEqual(main.num_to_binary("256"),"ERROR: Subnet Octets are limited to 255 bytes!")
		self.assertEqual(main.num_to_binary("356"),"ERROR: Subnet Octets are limited to 255 bytes!")
		self.assertEqual(main.num_to_binary("400"),"ERROR: Subnet Octets are limited to 255 bytes!")
		self.assertEqual(main.num_to_binary("277"),"ERROR: Subnet Octets are limited to 255 bytes!")

if __name__ == "__main__":
    unittest.main()

