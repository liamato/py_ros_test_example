# ROS test Python example

The idea behind this repo is to serve as a bare bones example of how to create test for ROS.

Looking at the commit log you will find the steps followed to:
 - Create a library exposed to ROS
 - Create a simple node that uses the library
 - Create unitary tests for the library using `unittest`
 - Create node level unitary tests using `rostest` + `unittest`

When level is mentioned in the commits, it's referring to the [ROS levels of testing](http://wiki.ros.org/action/fullsearch/Quality/Tutorials/UnitTesting#Levels_of_testing).

Beware that there is some outdated information on some of the ROS wiki pages. Witch is the reason for this repo, not having to filter the available info each time that a test for ROS has to be written.


### Executing the tests

#### Unitary tests
To execute a unitary test, the command to run is this:
```bash
rosrun <package_name> <test_executable>
```
In the case of this example the command would be:
```bash
rosrun cpp_ros_test_example cpp_ros_test_example-counter-test
```

#### All unitary tests

To execute all the unitary tests, the command to run is this (assumed the use of [catking_tools](https://catkin-tools.readthedocs.io/en/latest/index.html)):
```bash
catkin build <package_name> --catkin-make-args run_tests
```

In the case of this example the command would be:
```bash
catkin build py_ros_test_example --catkin-make-args run_tests
```


#### Node level unitary tests
To execute a node level unitary test, the command to run is this:
```bash
rostest <package_name> <test_name>
```
Take into account that the test_name should be the name of a [launchfile](http://wiki.ros.org/roslaunch/XML) with [test tags](http://wiki.ros.org/roslaunch/XML/test), usually with `.test` as extension.

In the case of this example the command for one of the .test would be:
```bash
rostest py_ros_test_example example_node_api.test
```

#### All tests
To build all the tests of a package, the command to run is this (assumed the use of [catking_tools](https://catkin-tools.readthedocs.io/en/latest/index.html)):
```bash
catkin test <package_name>
```
In the case of this example the command would be:
```bash
catkin test py_ros_test_example
```

### Related info

 - [unittest ROS Wiki page](http://wiki.ros.org/unittest)
 - [rostest ROS Wiki page](http://wiki.ros.org/rostest)
 - [roslaunch XML test tag](http://wiki.ros.org/roslaunch/XML/test)
 - [Integration of tests on catkin](http://docs.ros.org/en/hydro/api/catkin/html/howto/format2/python_nose_configuration.html)
 - [rostest command line](http://wiki.ros.org/rostest/Commandline)
 - [Standard test nodes](http://wiki.ros.org/rostest/Nodes)
 - [C++ example repo](https://github.com/liamato/cpp_ros_test_example)
 - [Another example repo](https://github.com/steup/Ros-Test-Example)