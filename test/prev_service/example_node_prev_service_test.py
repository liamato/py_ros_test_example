#! /usr/bin/env python
import unittest

import rospy as rp
import rostest

from std_msgs.msg import Int32
from std_srvs.srv import Trigger

PKG = 'py_ros_test_example'
NAME = 'example_node_prev_service'

class TestExampleNodePrevSrv(unittest.TestCase):
    def test_previous_service(self):
        rp.init_node(NAME, anonymous=True)
        service = rp.ServiceProxy("example_node/previous", Trigger)
        service.wait_for_service(1)
        service()
        val = rp.wait_for_message("example_node/value", Int32, 1).data
        self.assertEquals(val, -1, "val != -1")
        service()
        val = rp.wait_for_message("example_node/value", Int32, 1).data
        self.assertEquals(val, -2, "val != -2")

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestExampleNodePrevSrv)
