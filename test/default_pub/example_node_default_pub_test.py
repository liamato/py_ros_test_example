#! /usr/bin/env python
import unittest

import rospy as rp
import rostest

from std_msgs.msg import Int32

PKG = 'py_ros_test_example'
NAME = 'example_node_default_pub'

class TestExampleNodeDefaultPub(unittest.TestCase):
    def test_default_pub(self):
        rp.init_node(NAME, anonymous=True)
        val = rp.wait_for_message("example_node/value", Int32, 1).data
        self.assertEquals(val, 0, "val != 0")

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestExampleNodeDefaultPub)
