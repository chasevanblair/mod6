from more_functions.string_functions import multiply_string
import unittest


class test_strings(unittest.TestCase):
    # I have no idea how to make this literally fail - it doesn't work as inteded if taht is what is meant by the
    # instructions. If it is supposed to fail and throw an error I can't figure out how to do that(this is when func
    # is just a pass). I'll take missed points if its wrong but I'd appreciate an explanation on how to do it
    def test_multiply_string(self):
        multiply_string("ayayay", 4)
