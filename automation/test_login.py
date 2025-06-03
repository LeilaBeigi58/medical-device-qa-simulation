#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 13:42:02 2025

@author: leilabeigi
"""
import unittest

class TestLoginFunctionality(unittest.TestCase):

    def test_successful_login(self):
        username = "user1"
        password = "secure123"
        self.assertTrue(self.mock_login(username, password))

    def test_failed_login(self):
        username = "user1"
        password = "wrongpass"
        self.assertFalse(self.mock_login(username, password))

    def mock_login(self, username, password):
        # Mock user database
        valid_users = {"user1": "secure123", "nurse2": "medsafe"}
        return valid_users.get(username) == password

if __name__ == "__main__":
    unittest.main()