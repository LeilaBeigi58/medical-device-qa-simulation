#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 13:49:27 2025

@author: leilabeigi
"""
import unittest

class TestDeviceConnection(unittest.TestCase):

    def test_device_connected(self):
        device_status = "connected"
        self.assertEqual(device_status, "connected")

    def test_device_not_connected(self):
        device_status = "disconnected"
        self.assertNotEqual(device_status, "connected")

if __name__ == "__main__":
    unittest.main()