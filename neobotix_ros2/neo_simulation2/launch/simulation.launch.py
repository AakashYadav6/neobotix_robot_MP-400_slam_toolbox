# Neobotix GmbH

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

MY_NEO_ROBOT = 'mp_400'
MY_NEO_ENVIRONMENT = 'neo_track1'

def generate_launch_description():
    default_world_path = os.path.join(get_package_share_directory('neo_simulation2'), 'worlds', MY_NEO_ENVIRONMENT + '.world')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    robot_dir = LaunchConfiguration(
        'robot_dir',
        default=os.path.join(get_package_share_directory('neo_simulation2'),
            'robots/'+MY_NEO_ROBOT,
            MY_NEO_ROBOT+'.urdf'))

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true')
    use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
    urdf = os.path.join(get_package_share_directory('neo_simulation2'), 'robots/'+MY_NEO_ROBOT+'/', MY_NEO_ROBOT+'.urdf')

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',arguments=['-entity', MY_NEO_ROBOT, '-file', urdf, '-spawn_service_timeout', '30.0'], output='screen')

    #rviz_config_dir = os.path.join(
    #    get_package_share_directory('nav2_bringup'),
    #    'rviz',
    #    'nav2_default_view.rviz')

    start_robot_state_publisher_cmd = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=[urdf])

    # teleop =  Node(package='teleop_twist_keyboard',executable="teleop_twist_keyboard",
    # output='screen',
    # prefix = 'xterm -e',
    # name='teleop')

    gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={
                'world': default_world_path,
                'verbose': 'true'
            }.items()
        )

    #rviz =   Node(
    #        package='rviz2',
    #        executable='rviz2',
    #        name='rviz2',
    #        arguments=['-d', rviz_config_dir],
    #        parameters=[{'use_sim_time': use_sim_time}],
    #        output='screen')


    #return LaunchDescription([spawn_entity, start_robot_state_publisher_cmd, teleop, gazebo])
    return LaunchDescription([gazebo, spawn_entity, start_robot_state_publisher_cmd])
