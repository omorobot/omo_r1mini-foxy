from setuptools import find_packages
from setuptools import setup

package_name = 'omo_r1mini_teleop'

setup(
    name=package_name,
    version='2.1.1',
    packages=find_packages(exclude=[]),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        'Teleoperation node using keyboard for the OMORobot R1 Mini'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_keyboard = omo_r1mini_teleop.script.teleop_keyboard:main'
        ],
    },
)
