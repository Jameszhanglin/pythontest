from sys import  argv

script, input_file = argv  #参数

def print_all(f):    #函数打印读到的文件内容
    print(f.read())

def rewind(f):     #函数回到文件起点
    f.seek(0)

def print_a_line(line_count,f):   #函数行号计算 并读行
    print(line_count,f.readline())

current_file = open(input_file)  #打开 文件

print("First let's print the whole file:\n")

print_all(current_file)  #打印打开的文件 内容

print("Now,let's rewind, kind of like a tape.")

rewind(current_file) #通过函数回到文件起点

print("Let's print three liness:")

current_line = 1  #行号赋值
print_a_line(current_line,current_file)  #读行号和指定行内容

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)


