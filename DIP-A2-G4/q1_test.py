from q1 import *

# testing with probability matrix and 1-d array

print("Case1:\n")
# encoding

# input
probability_matrix = [(1, 0.25), (2, 0.30), (3, 0.12), (4, 0.15), (5, 0.18)]
message = [1, 2, 3, 4, 5]

print("Given Inputs:")
print(f"Probability Matrix: {probability_matrix}")
print(f"Message: {message}\n")

# huffman codes based on the table
print("huffman codes based on the probability table")
huffman_coding_symbols = huffmanCoding(probability_matrix).huffman_codes
for k,v in huffman_coding_symbols.items():
    print(f"{str(k).ljust(2)}: {v}")

encoded_message, probability_matrix = main_encode(probability_matrix=probability_matrix, message=message)
print("\nMessage After Encoded based on the above symbol table")
print(encoded_message)

# saving message in a binary file
with open("q1_compressed_message.bin", "w") as f:
    f.write(encoded_message)

# decoding
main_decode(probability_matrix, r"q1_compressed_message.bin")


print("\nCase2:\n")
# testing with a 8-bit grayscale image

print("Input")
print("A 8-bit grayscale image\n")
image_path = r"q1_image.jpg"
Image.open(image_path).show()

#encoding
encoded_image, probability_matrix = main_encode(image_path=image_path)
print("After Encoding,")
# print(f"Encoded_image: {encoded_image}")
print(f"Probability Matrix: {probability_matrix}")

print("\nhuffman codes based on the probability table")
huffman_coding_symbols = huffmanCoding(probability_matrix).huffman_codes
for k,v in huffman_coding_symbols.items():
    print(f"{str(k).ljust(3)}: {v}")

with open(f"q1_compressed_image.bin", "w") as f:
    f.write(encoded_image)
    
main_decode(probability_matrix, f"q1_compressed_image.bin", (332, 300))