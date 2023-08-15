import unittest


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """


    @staticmethod
    def parametrize(param):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        return param

if __name__ == '__main__':
    unittest.main()