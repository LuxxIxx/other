import unittest
from cases import test_01CreatOrder

if __name__ == '__main__':
    # <editor-fold desc="ÔËÐÐwebÖ§¸¶">
    testcases = unittest.TestLoader().loadTestsFromTestCase(test_01CreatOrder.test_01CreatOrder)
    with open('../report/payReport01.txt', "w+") as txtfile:
        unittest.TextTestRunner(stream=txtfile, verbosity=2).run(testcases)
    # </editor-fold>
