#Школярі та яблука
num_p = int(input("Enter number of pupils: "))
num_a = int(input("Enter number of apples: "))

res_of_div =  num_a // num_p
result = num_a % num_p

print(f"Number of apples for each pupil: {res_of_div}")

print(f"Number of remainder: {result}")
