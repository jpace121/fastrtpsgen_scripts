# fastrtpsgen_scripts

## Problem
When [fastrtpsgen][source-link] is compiled with [colcon][colcon-link], the
script provided with the source is not added to the user's path when they source
the relevant `local_setup.bash` file.

## Solution
This package contains a python script which is added to the user's path.

This package assumes that the `fasrtpsgen` class is in the user's
`$CLASSPATH`.

This can be done using `colcon-gradle` from the following branch
https://github.com/colcon/colcon-gradle/tree/jacob/classpath_hook.

source-link: https://github.com/eProsima/Fast-RTPS-Gen
colcon-link: https://github.com/colcon
