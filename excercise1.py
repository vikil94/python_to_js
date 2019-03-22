apples = 14
print(apples)

print("I have {} apples.".format(apples))


materials = ['wood', 'metal', 'stone']
words = {
    'elephant': "The world's largest land mammal.",
    'school': 'A place of learning.',
    'ice cream': 'A delicious milk-based dessert.',
}


num = 16
if num > 10:
  print("{} is greater than 10.".format(num))
elif num == 10:
  print("{} is exactly 10.".format(num))
else:
  print("{} must be less than 10.".format(num))


for x in range(0, 10):
  print("Doing the same thing over and over.")


base = 5
for num in range(0, 20):
  print(num + base)

total = 0
for num in range(0, 100):
  total += num

print(total)

for height in range(3, 15):
  if height > 9:
    print("You can get on the rollercoaster!")
  else:
    print("You are too short to ride this rollercoaster.")


containers = ['purse', 'wallet', 'backpack']
for container in containers:
  print(container)


def hello_world():
  return "Hello world!"


hello_world()


def add(first_num, second_num):
  return first_num + second_num


amount = add(5, 7)
print(amount)
