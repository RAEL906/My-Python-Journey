#算术运算符:
#计算两个数字（例如：15 和 7）的和、差、积、商（浮点数）、整除、取模和幂。
num1=15
num2=7
print(f"算术运算符")
sum_result=num1+num2
diff_result=num1-num2
product_result=num1*num2
quotient_result=num1/num2
integer_division_result=num1//num2
modulus_result=num1%num2
power_result=num1**num2
#打印每次计算的结果。
print(f"{num1}+{num2} = {sum_result}")
print(f"{num1}-{num2} = {diff_result}")
print(f"{num1}*{num2} = {product_result}")
print(f"{num1}/{num2} = {quotient_result}")
print(f"{num1}//{num2} = {integer_division_result}")    
print(f"{num1}%{num2} = {modulus_result}")
print(f"{num1}**{num2} = {power_result}")
#比较运算符:
#比较两个数字（例如：10 和 5），判断它们是否相等、不相等、大于、小于、大于等于、小于等于。
print(f"比较运算符")
num3=10
num4=5
equal_check=(num3==num4)
not_equal_check=(num3!=num4)
greater_than_check=(num3>num4)
less_than_check=(num3<num4)
greater_than_or_equal_check=(num3>=num4)
less_than_or_equal_check=(num3<=num4)
#打印每次比较的结果（这将是布尔值）。
print(f"{num3} == {num4} 的结果是: {equal_check}")
print(f"{num3} != {num4} 的结果是: {not_equal_check}")
print(f"{num3} > {num4} 的结果是: {greater_than_check}")
print(f"{num3} < {num4} 的结果是: {less_than_check}")
print(f"{num3} >= {num4} 的结果是: {greater_than_or_equal_check}")
print(f"{num3} <= {num4} 的结果是: {less_than_or_equal_check}")
#逻辑运算符:
print(f"逻辑运算符")
#定义两个布尔变量 has_license = True 和 has_car = False。
has_license = True
has_car = False
#使用 and、or、not 运算符组合这两个变量，并打印结果。
and_result = has_license and has_car
or_result = has_license or has_car
not_result = not has_license
#打印每次逻辑运算的结果。
print(f"拥有驾照（{has_license}） and 拥有车辆（{has_car}） 的结果是: {and_result}")
print(f"拥有驾照（{has_license}） or 拥有车辆（{has_car}） 的结果是: {or_result}")
print(f"not 拥有驾照（{has_license}） 的结果是: （{not_result}）")