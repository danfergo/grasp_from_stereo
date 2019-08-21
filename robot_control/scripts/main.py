#!/usr/bin/env python

import rospy
from controller import RobotController
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
from math import pi

def main():  # for test
    try:
        rospy.init_node("robot_controller")

        robo = RobotController()

        # pose = Pose()
        # pose.point = Point(j)
        # pose.orientation = quaternion_from_euler(0, 0, 0)

        while not rospy.is_shutdown():
            robo.move_to_pose([-0.55, -0, 0.25, 3.067, 0, 0])


        # urc.ratet = 1
        # urc.Init_node()
        #
        # cn = 0
        # # pos = [0.446, -0.305, 0.142, 2.505, 1.968, 0]
        # pos = [-0.25, -0.6, 0.152, 3.067, 0, 0]
        # tempPos = copy.deepcopy(pos)
        #
        # urc.move2Pos(tempPos)
        #
        # while not rospy.is_shutdown():
        #     tempPos[2] = pos[2] + cn * 0.01
        #     urc.move2Pos(tempPos)
        #     cn += 1
        #     if cn == 5:
        #         cn = 0

    except KeyboardInterrupt:
        rospy.signal_shutdown('KeyboardInterrupt')
        raise


if __name__ == '__main__':
    main()


