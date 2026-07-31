#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image

def image_callback(msg):
    rospy.loginfo("收到图像消息")
    rospy.loginfo("宽度: %d", msg.width)
    rospy.loginfo("高度: %d", msg.height)
    rospy.loginfo("编码格式: %s", msg.encoding)
    rospy.loginfo("数据长度: %d 字节", len(msg.data))
    rospy.loginfo("------------------------")

def image_subscriber():
    rospy.init_node('image_subscriber', anonymous=True)
    rospy.Subscriber('/demo_image', Image, image_callback)
    rospy.spin()  # 循环等待消息

if __name__ == '__main__':
    image_subscriber()