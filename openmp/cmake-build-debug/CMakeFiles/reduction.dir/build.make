# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/Users/ARTEM/CLionProjects/openmp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/reduction.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/reduction.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/reduction.dir/flags.make

CMakeFiles/reduction.dir/reduction.cpp.o: CMakeFiles/reduction.dir/flags.make
CMakeFiles/reduction.dir/reduction.cpp.o: ../reduction.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/reduction.dir/reduction.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/reduction.dir/reduction.cpp.o -c /mnt/c/Users/ARTEM/CLionProjects/openmp/reduction.cpp

CMakeFiles/reduction.dir/reduction.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/reduction.dir/reduction.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/ARTEM/CLionProjects/openmp/reduction.cpp > CMakeFiles/reduction.dir/reduction.cpp.i

CMakeFiles/reduction.dir/reduction.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/reduction.dir/reduction.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/ARTEM/CLionProjects/openmp/reduction.cpp -o CMakeFiles/reduction.dir/reduction.cpp.s

CMakeFiles/reduction.dir/reduction.cpp.o.requires:

.PHONY : CMakeFiles/reduction.dir/reduction.cpp.o.requires

CMakeFiles/reduction.dir/reduction.cpp.o.provides: CMakeFiles/reduction.dir/reduction.cpp.o.requires
	$(MAKE) -f CMakeFiles/reduction.dir/build.make CMakeFiles/reduction.dir/reduction.cpp.o.provides.build
.PHONY : CMakeFiles/reduction.dir/reduction.cpp.o.provides

CMakeFiles/reduction.dir/reduction.cpp.o.provides.build: CMakeFiles/reduction.dir/reduction.cpp.o


# Object files for target reduction
reduction_OBJECTS = \
"CMakeFiles/reduction.dir/reduction.cpp.o"

# External object files for target reduction
reduction_EXTERNAL_OBJECTS =

reduction: CMakeFiles/reduction.dir/reduction.cpp.o
reduction: CMakeFiles/reduction.dir/build.make
reduction: CMakeFiles/reduction.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable reduction"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/reduction.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/reduction.dir/build: reduction

.PHONY : CMakeFiles/reduction.dir/build

CMakeFiles/reduction.dir/requires: CMakeFiles/reduction.dir/reduction.cpp.o.requires

.PHONY : CMakeFiles/reduction.dir/requires

CMakeFiles/reduction.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/reduction.dir/cmake_clean.cmake
.PHONY : CMakeFiles/reduction.dir/clean

CMakeFiles/reduction.dir/depend:
	cd /mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/ARTEM/CLionProjects/openmp /mnt/c/Users/ARTEM/CLionProjects/openmp /mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug /mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug /mnt/c/Users/ARTEM/CLionProjects/openmp/cmake-build-debug/CMakeFiles/reduction.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/reduction.dir/depend
