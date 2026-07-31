#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import numpy as np

def image_publisher():
    rospy.init_node('image_publisher', anonymous=True)
    pub = rospy.Publisher('/demo_image', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz 发布频率

    while not rospy.is_shutdown():
        # 生成 480x640 模拟纯色图像
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        img[:, :] = [100, 200, 150]  # BGR 格式填充

        # 构建 Image 消息
        msg = Image()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "camera"
        msg.height = 480
        msg.width = 640
        msg.encoding = "bgr8"
        msg.step = 640 * 3
        msg.data = img.tobytes()

        pub.publish(msg)
        rospy.loginfo("发布图像：宽%d 高%d 编码%s", msg.width, msg.height, msg.encoding)
        rate.sleep()

if __name__ == '__main__':
    try:
        image_publisher()
    except rospy.ROSInterruptException:
        pass