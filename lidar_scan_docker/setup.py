from setuptools import setup
import os
from glob import glob

package_name = 'lidar_scan'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name,['ekf_node.yaml']),
        ('share/' + package_name,['wamv.urdf']),
        ('share/' + package_name,['tahseen.rviz']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thussain',
    maintainer_email='tahseenreza101@gmail.com',
    description='Creates lidar frame and occupancy grid',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'lidar_pub = lidar_scan.lidar_pub:main',
                             'pointcloud_to_laserscan_node = lidar_scan.pointcloud_to_laserscan_node:main',
                             'colorMappingNode = lidar_scan.colorMappingNode:main',
                             'fixed_math=lidar_scan.fixed_math:main'
                             
        ],
    },
)

# Figure out how to include 'share/config and share/description' so you can move ekf_node and wamv.urdf into respective files 