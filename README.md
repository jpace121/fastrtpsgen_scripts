# fastrtpsgen_scripts

## Problem
When [fastrtpsgen]( https://github.com/eProsima/Fast-RTPS-Gen) is compiled
with [colcon](https://github.com/colcon), the script provided with the source
is not added to the user's path when they source the relevant `local_setup.bash`
file.

## Solution
This package contains a python script which is added to the user's path.

This package assumes that the `fasrtpsgen` class is in the user's
`$CLASSPATH`.

This can be done using `colcon-gradle` from the following branch
https://github.com/colcon/colcon-gradle/tree/jacob/classpath_hook.
