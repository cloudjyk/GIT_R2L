#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from USE_TEST import mydict
import unittest
def setUp():
    print('\nsetUp...')

def tearDown():
    print('\ntearDown...')

class TestDict(unittest.TestCase):
    # def setUp(self):
    #     print('setUp...')

    # def tearDown(self):
    #     print('tearDown...')

    def test_init(self):
        setUp()
        d=mydict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
        tearDown()
    def test_key(self):
        setUp()
        d=mydict()
        d['key']='value'
        self.assertTrue(isinstance(d,dict))
        tearDown()
    def test_getattr(self):
        setUp()
        d=mydict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        tearDown()
    def test_keyerror(self):
        setUp()
        d=mydict()
        # d.key='value'
        with self.assertRaises(KeyError):
            value = d['key']
        tearDown()
    def test_attrerror(self):
        setUp()
        d=mydict()
        with self.assertRaises(AttributeError):
            value = d.empty
        tearDown()
if __name__ == '__main__':
    unittest.main()