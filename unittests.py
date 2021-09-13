import unittest
import main

class test_network_tools(unittest.TestCase):

	def test_num_to_binary(self):
		self.assertEqual(main.num_to_binary(192),'11000000')
		self.assertEqual(main.num_to_binary(168),'10101000')
		self.assertEqual(main.num_to_binary(1),'00000001')
		self.assertEqual(main.num_to_binary(252),'11111100')
		self.assertEqual(main.num_to_binary(300),'ERROR: Subnet Octets are limited to 255 bytes!')
		self.assertEqual(main.num_to_binary(400),'ERROR: Subnet Octets are limited to 255 bytes!')
		self.assertEqual(main.num_to_binary(358),'ERROR: Subnet Octets are limited to 255 bytes!')
		self.assertEqual(main.num_to_binary(256),'ERROR: Subnet Octets are limited to 255 bytes!')






if __name__ == '__main__':
    unittest.main()

