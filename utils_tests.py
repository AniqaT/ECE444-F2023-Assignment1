from utils import utils

class utils_tests ():
    def test_reversed():
        assert utils.reversed(95) == 59, "Should be 59"
        assert utils.reversed(59.5) == "Input must be an int", "Should be \"Input must be an int\""
        assert utils.reversed("75") == "Input must be an int", "Should be \"Input must be an int\""
        assert utils.reversed(87) == 78, "Should be 78"
        assert utils.reversed(79) == 97, "Should be 97"
        assert utils.reversed(87) == 78, "Should be 78"

    def test_formatter():
        assert utils.formatter(95) == ['0b1011111', '0o137'], "Should be ['0b1011111', '0o137']"
        assert utils.formatter(59.5) == "Input must be an int", "Should be \"Input must be an int\""
        assert utils.formatter("75") == "Input must be an int", "Should be \"Input must be an int\""

if __name__ == "__main__":
    utils_tests.test_reversed()
    utils_tests.test_formatter()
    print("All tests passed")