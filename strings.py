# -*- coding: utf-8 -*-

hello = "hello"
world = "world"
hello_world = hello + " " + world + ""
print(hello_world)

length = len(hello_world)
print(length)

# will print each element in hello_world
for i in hello_world:
	print(i)

# will print from first position to fourth
print(hello_world[0:4])
print(hello_world.upper())
print(hello_world.lower())
print(hello_world.strip()) # remove special characters from string end

neutral_string = "lorem ipsum dolor sit amet"
split_string = neutral_string.split(" ")
print(split_string)

search = neutral_string.find("dolor")
print(search)
print(neutral_string[search:])
print(neutral_string[-search:])

new_string = neutral_string.replace("dolor", "dor")
print(new_string)
