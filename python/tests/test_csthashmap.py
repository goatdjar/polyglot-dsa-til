import unittest

# Import your class from your file
from dsa_utils.csthashmap import CustomHashMap

class TestCustomHashMap(unittest.TestCase):

    def setUp(self):
        """Runs before every single test to give us a fresh hashmap."""
        self.hm = CustomHashMap(initial_capacity=4)

    def test_insert_and_retrieve(self):
        """Test that we can add items and get them back."""
        self.hm["key1"] = "value1"
        self.hm["key2"] = "value2"

        self.assertEqual(self.hm["key1"], "value1")
        self.assertEqual(self.hm["key2"], "value2")
        self.assertEqual(len(self.hm), 2)

    def test_update_existing_key(self):
        """Test that inserting an existing key updates the value instead of duplicating."""
        self.hm["score"] = 10
        self.hm["score"] = 25  # Update

        self.assertEqual(self.hm["score"], 25)
        self.assertEqual(len(self.hm), 1)

    def test_missing_key_raises_key_error(self):
        """Test that looking up a non-existent key throws a KeyError."""
        with self.assertRaises(KeyError):
            _ = self.hm["ghost_key"]

    def test_deletion(self):
        """Test that items can be successfully removed."""
        self.hm["temporary"] = "delete me"
        self.assertEqual(len(self.hm), 1)

        del self.hm["temporary"]

        self.assertEqual(len(self.hm), 0)
        with self.assertRaises(KeyError):
            _ = self.hm["temporary"]

    def test_delete_missing_key_raises_key_error(self):
        """Test that deleting a non-existent key throws a KeyError."""
        with self.assertRaises(KeyError):
            del self.hm["not_there"]

    def test_contains_operator(self):
        """Test that the 'in' keyword correctly identifies present/absent keys."""
        self.hm["found_it"] = True

        self.assertTrue("found_it" in self.hm)
        self.assertFalse("lost_it" in self.hm)

    def test_hash_collision_handling(self):
        """
        Test separate chaining. We force a collision by creating keys
        that map to the exact same bucket index.
        """
        # Create two distinct objects that will result in the same index modulo 4
        # Since hash(0) == 0 and hash(4) == 4, both:
        # 0 % 4 == 0 and 4 % 4 == 0
        key_a = 0
        key_b = 4

        self.hm[key_a] = "apple"
        self.hm[key_b] = "banana"

        # Even though they land in the same bucket chain, we should
        # still be able to retrieve both cleanly.
        self.assertEqual(self.hm[key_a], "apple")
        self.assertEqual(self.hm[key_b], "banana")
        self.assertEqual(len(self.hm), 2)

        # Deleting one shouldn't destroy the other
        del self.hm[key_a]
        self.assertFalse(key_a in self.hm)
        self.assertTrue(key_b in self.hm)
        self.assertEqual(self.hm[key_b], "banana")


if __name__ == "__main__":
    unittest.main()
