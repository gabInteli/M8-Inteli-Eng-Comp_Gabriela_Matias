from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess

map_saver_params_file = 'map_saver_params.yaml'


def generate_launch_description():
    map_saver = ExecuteProcess(
            cmd=['ros2', 'run', 'nav2_map_server', 'map_saver_cli', '-f', 'my-map', '--ros-args', '-p', 'save_map_timeout:=10000.00'],
            output='screen'
        )

    return LaunchDescription([
        map_saver,
        ])

if __name__ == "__main__":
   generate_launch_description()