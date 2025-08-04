#尝试进行不同数据类型之间的转换。
print(f"数据类型转换示例")
#定义一个字符串变量 num_str = "123"。
num_str = "123"
#将 num_str 转换为整数类型，并将其存储在新变量 num_int 中。
num_int= int(num_str)
print(f"转换前的字符串: '{num_str}', 类型: {type(num_str)}")#注意这里字符串里只能用’‘，不能用“”
print(f"转换后的整数: {num_int}, 类型: {type(num_int)}")    
#定义一个浮点数变量 float_val = 98.76。
float_val= 98.76
#将 float_val 转换为整数类型，并将其存储在新变量 int_val 中。
int_val = int(float_val)
#打印转换前后的变量值和类型，观察变化。
print(f"转换前的浮点数: {float_val}, 类型: {type(float_val)}")
print(f"转换后的整数: {int_val}, 类型: {type(int_val)}")