num = [1,2,3,4,5]
even_num = list(filter(lambda x: x%2==0,num))
cube_num = list(map(lambda x: x**3,even_num))
print("Even_num\n",even_num)
print("Cubed_num\n",cube_num)