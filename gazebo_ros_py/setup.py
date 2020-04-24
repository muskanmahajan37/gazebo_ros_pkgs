from setuptools import setup

package_name = 'gazebo_ros_py'

setup(
    name=package_name,
    version='0.8.4',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Jacob Perron',
    author_email='jacob@openrobotics.org',
    maintainer='Jacob Perron',
    maintainer_email='jacob@openrobotics.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Python action tutorials code.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_entity = gazebo_ros_py.spawn_entity:main',
        ],
    },
)
