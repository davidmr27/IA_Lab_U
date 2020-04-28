#!/usr/bin/env python
import rospy, random
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    while not rospy.is_shutdown():
        random_str = "Numero aleatorio {" + str(random.randint(0,1000) +"}")
        rospy.loginfo(random_str)
        pub.publish(random:_str)
        rospy.sleep(5.)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
