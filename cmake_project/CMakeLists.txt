# 1. 设置 CMake 最低版本要求
cmake_minimum_required(VERSION 3.10)

# 2. 设置项目名称，比如叫 "MyProject"
project(MyProject)

# 3. 告诉 CMake，我们的项目需要 C++ 17 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 4. 找到所有的源文件 (main.cpp, math.cpp)
#    并把它们添加到一个叫 "SOURCES" 的变量里
aux_source_directory(. SOURCES) 
# 注意: aux_source_directory 是个偷懒的办法，在大型项目中不推荐
# 但在入门时，它非常好用。它会把当前目录下所有 .cpp 文件都加进来。

# 5. 添加一个可执行文件
#    名称叫 "MyExecutable" (你可以随便起)
#    源文件就是我们刚刚找到的 "SOURCES" 变量
add_executable(MyExecutable ${SOURCES})

# 就这么简单！