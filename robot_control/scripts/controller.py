import rospy
import copy
from std_msgs.msg import String
from geometry_msgs.msg import Pose


class RobotController:
    def __init__(self):
        print('hello world')

        # parameters for ur5 movement; i.e. movel(pose, a=1.2, v=0.25, t=0, r=0); tool denotes the endpoint (I think)
        self.vel = 0.25  # tool speed
        self.ace = 0.2  # tool acceleration
        self.t = 0  # the time (seconds) to make the move
        self.r = 0  # blend radius
        self.move_type = "movel"  # movel:move to position(linear in tool-space); movej:linear in joint-space

        self.cont = 10
        self.pos = [0.446, -0.305, 0.142, 2.505, 1.968,
                    0]  # ur pose       (either joint positions q=[Base,Shoulder, Elbow, Wrist1, Wrist2, Wrist3],
        #                       or pose[x,y,z,Rx,Ry,Rz], it holds q==p(x,y,z,Rx,Ry,Rz))
        # self.pos_type = 0  # ur pose type  (0:pose 1:joint positions)
        # pose = p[0.2,0.3,0.5,0,0,3.14] -> position in base frame of x = 200 mm, y = 300 mm, z = 500 mm, rx = 0, ry = 0, rz = 180 deg
        # self.pub = None
        # self.rate = None

        self.rate = rospy.Rate(1)

        self.pub = rospy.Publisher("/ur_driver/URScript", String, queue_size=10)


    def move_to_pose(self, pose):
        pose_cmd = "p[ {} , {} , {} , {} , {} , {} ]".format(*pose)
        cmd = "movej({})".format(pose_cmd)
        self.pub.publish(cmd)
        self.rate.sleep()
        print(cmd)
# def Init_node(self):
#     pub =



# def Pos2UrMoveCmd(self, pos):  # return the command for ur5 to move to pos
#     pose = pos
#     if self.pos_type == 0:
#         cmd = self.move_type + "(p[" + str(pose[0]) + "," + str(pose[1]) + "," + str(pose[2]) + "," + str(
#             pose[3]) + "," + str(pose[4]) + "," + str(pose[5]) + "]," + "a=" + str(self.ace) + "," + "v=" + str(
#             self.vel) + "," + "t=" + str(self.t) + "," + "r=" + str(self.r) + ")"
#     else:
#         cmd = self.move_type + "([" + str(pose[0]) + "," + str(pose[1]) + "," + str(pose[2]) + "," + str(
#             pose[3]) + "," + str(pose[4]) + "," + str(pose[5]) + "]," + "a=" + str(self.ace) + "," + "v=" + str(
#             self.vel) + "," + "t=" + str(self.t) + "," + "r=" + str(self.r) + ")"
#     print("----cmd to ur5:", cmd)
#     return cmd

# def move2Pos(self, pos):
#     cmd = self.Pos2UrMoveCmd(pos)
#     self.pos = pos  # update current pos of ur
#     self.pub.publish(cmd)
#     self.rate.sleep()

# def get_ur_pos(self):

# URScrip programming functions:
# #get_actual_tcp_pose()    #TCP:tool center point
#     Returns the current measured tool pose
#     Returns the 6d pose representing the tool position and orientation
#     specified in the base frame. The calculation of this pose is based on
#     the actual robot encoder readings.
#     Return Value
#     The current actual TCP vector [X, Y, Z, Rx, Ry, Rz]

# set_payload_mass(m)    # m: mass in kilograms

# sleep(t) #t:times(s)

# textmsg(s1, s2='')     # Send text message to log, e.g.textmsg("value=", 3)
