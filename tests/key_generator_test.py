# some unit tests to check the key generator
import unittest
from key_generator import generate, test_key

#test the key generator
class TestKeyGenerator(unittest.TestCase):
    # test the key generator
    def test_generate(self):
        # test the key generator
        key = generate(128)
        # check the length of the key
        self.assertTrue(len(key) >= 128)
        # check the key
        self.assertTrue(test_key(key))

    # test the key generator
    def test_generate_256(self):
        # test the key generator
        key = generate(256)
        # check the length of the key
        self.assertTrue(len(key) >= 256)
        # check the key
        self.assertTrue(test_key(key))

    # test the key generator
    def test_generate_512(self):
        # test the key generator
        key = generate(512)
        # check the length of the key
        self.assertTrue(len(key) >= 512)
        # check the key
        self.assertTrue(test_key(key))

    # test length of key returned
    def test_length(self):
        # test the key generator
        key = generate(128)
        # check the length of the key
        self.assertTrue(len(key) >= 128)
    
    #test the key uniqueness
    def test_uniqueness(self):
      keys = [generate(128) for _ in range(10)]
      assert len(set(keys)) == 10, 'Keys are not unique'

#run the tests
if __name__ == '__main__':
    unittest.main()