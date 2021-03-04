import os
from glob import glob
from setuptools import find_packages
from setuptools import setup

package_name = 'omo_r1mini_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=[]),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'param'), glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    author='Bishop Pearson',
    author_email='bishopearson@gmail.com',
    maintainer='Bishop Pearson',
    maintainer_email='bishopearson@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'OMORobot R1 Mini driver node that include iff drive controller, odometry and tf node'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'omo_r1mini_mcu_node = omo_r1mini_bringup.scripts.omo_r1mini_mcu_node:main',
            'omo_r1mini_motor_setting_node = omo_r1mini_bringup.scripts.omo_r1mini_motor_setting_node:main'
        ],
    },
)
