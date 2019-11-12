import unittest
from tkinter import Tk
import report
from haha import *

root = Tk()
a = report.Project(root)



class TestNewAlgorithm(unittest.TestCase):
    def test_sort(self):

        array_test = [('11','Anil', 'Chhetri', 'pepsicola', 'Ethiccal hacking', '981324578'),
                      ('15', 'Aashish', 'Sunsari', '98965645', 'Computing')]
        expected_result = [('15', 'Aashish', 'Sunsari', '98965645', 'Computing'),
                           ('11','Anil', 'Chhetri', 'pepsicola', 'Ethiccal hacking', '981324578')]

        a.combo_sort.set('fname')
        ac_result=a.bubble_sort(array_test)
        self.assertEqual(expected_result,ac_result)


    def test_search(self):
        array_test = [('11', 'Babita', 'Lamjung', '9810133910', 'Hacking'),
                      ('12', 'Adana', 'Kathmandu', '9803635098', 'Security')]
        expected_result = [('11', 'Babita', 'Lamjung', '9810133910', 'Hacking')]

        l_search = LinearSearch(array_test, 'Babita', "fname")
        actual = l_search.aList
        print(expected_result)
        print(actual)
        self.assertEqual(expected_result, actual)



if __name__ == '_main_':
    unittest.main()
