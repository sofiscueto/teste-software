import unittest

from atividade1testUnit import eh_par

class TestEh_Par(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(2))

    def test_impar(self):
        self.assertFalse(eh_par(3))

if __name__ == "__main__":
    unittest.main()