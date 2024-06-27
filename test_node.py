import rclpy
##import python
from geometry_msgs.msg import Quaternion
##Import message type 

rclpy.init()
##innitiate ros2 python

##defines callback function
def callback(data):
    x = data.x
    y = data.y
    z = data.z
    w = data.w
    print('X = ',x,'Y = ', y, 'Z = ', z, 'W = ' ,w)
    pass

#defines a node with the name my_first_node
node=rclpy.create_node('my_first_node')

#publishes the data in the form of a quaternion
publisher = node.create_publisher(Quaternion,'my_first_publisher_topic',10)

# recieves and callsback the data of the quaternion

subscriber = node.create_subscription(Quaternion, 'my_first_subscription', callback,10)

#defines the data values for the quaternion
D = Quaternion()

D.x = 9.0
D.y = 7.0
D.z = 5.0
D.w = 1.0

#publishes the quaternion

publisher.publish(D)

#print (x,y,z,w)

#runs the node continuously. 
rclpy.spin(node)