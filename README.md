
# SLAM TOOLBOX with Neobotix Mobile Robot MP-400

```bash
source simulation2_ws/install/setup.bash
~/simulation2_ws/src/neobotix_ros2/start_basic_neobotix_sim.sh
```
This sets up our environment and launches the simulation. Run the following command on a shell.

```bash
ros2 launch ros2_mapping online_async_launch.py
```
Now launch the node.

Run Rviz2 and visualize the map that's being created.
```bash
rviz2
```
Move the robot around and generate a full map of the environment. To move the robot around you can use the following command:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

In order to save the map you have created, you need to ran an executable map_saver which runs a map_saver node from nav2_map_server.
```bash
ros2 run nav2_map_server map_saver_cli -f my_map
```

This command will generate two files:

my_map.pgm image file. Is the map as an occupancy grid image.
my_map.yaml file which contains details about the resolution of the map.

YAML File of the Map.
```bash
image: my_map.pgm
mode: trinary
resolution: 0.05
origin: [-5.9, -5.22, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.25
```

The map you created needs to be provided to other navigation applications like the localization system or the path planner. In order to do that, we need to launch the map_server.

We will launch the following nodes to load the map & visualize on Rviz:

map_server
nav2_lifecycle_manager
rviz2

launch the node 
```bash
source install/setup.bash
ros2 launch ros2_mapping provide_map.launch.py

```


Different Mapping modes
```bash
Offline: Mapping is done without real-time data. For instance using bag files.
Synchronous: It makes sure it processes all the incoming laser measurements. It can lag over time.
Asynchronous: It processes incoming laser measurements in real time.
Lifelong: It allows to build a map partially over time. For instance, get a 1st version of a map and update it.
```


lifelong 
launch 
```bash
ros2 service call /slam_toolbox/serialize_map slam_toolbox/srv/SerializePoseGraph "filename: 'half_map'"
```













