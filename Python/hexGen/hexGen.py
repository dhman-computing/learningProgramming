### This programme takes a name of a file as command line argument and generates a hex code file

## File input

#TODO

# TEST
in_file = input("Input file:")

## Main computations

fin = open(in_file, "rb")

byte_list = []

byte = fin.read(1)
while byte:
	byte_list.append(byte)
	byte = fin.read(1)

byte_list_str = []
for i in byte_list:
	byte_list_str.append(i.hex())

# print(byte_list_str)
# print(len(byte_list_str))

out_file = in_file[:in_file.index('.')]

# print(out_file)

out_file += '.hex'

# print(out_file)

fout = open(out_file, "x")

for i in byte_list_str:
	fout.write(i)
	fout.write(' ')

## Closing all opened files

fin.close()
fout.close()