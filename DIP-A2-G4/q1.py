from PIL import Image


class huffmanNode:
    """The huffmanNode class is used to create a node for the huffman tree.
    """

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


class huffmanCoding:
    """Class to compress the file based on the huffman coding
    """

    def __init__(self, probability_matrix):
        """Constructor for the huffman coding class

        Args:
            probability_matrix (list): list of tuples containing the character and
                                  the probability of the character
        """
        self.probability_matrix = probability_matrix
        if(self.validate_probability_matrix()):
            self.huffman_codes = self.huffman_coding()
        else:
            raise ValueError("Invalid symbol matrix")

    def validate_probability_matrix(self):
        """check if the symbol matrix is valid  

        Returns:
            bool: True if the symbol matrix is valid, False otherwise
        """
        total_probability = 0
        for symbol in self.probability_matrix:
            total_probability += symbol[1]
        return total_probability == 1

    def huffman_code_helper(self, huffman_node, code, huffman_code):
        """The huffman_code_helper function is used to create the huffman
        code for each character.

        Args:
            huffman_node (huffmanNode): the huffman node
            code (str): the huffman code
            huffman_code (dict): the dictionary to store the huffman code
        """
        if huffman_node.char is not None:
            huffman_code[huffman_node.char] = code
        else:
            self.huffman_code_helper(huffman_node.left, code + "0",
                                     huffman_code)
            self.huffman_code_helper(huffman_node.right, code + "1",
                                     huffman_code)

    def huffman_coding(self):
        """The huffman_coding function is used to create the huffman tree
        and the huffman code for each character.
        """
        # Create a list of huffman nodes
        huffman_nodes = []
        for i in range(len(self.probability_matrix)):
            huffman_nodes.append(huffmanNode(self.probability_matrix[i][0],
                                             self.probability_matrix[i][1]))

        # Create a list of huffman nodes
        while len(huffman_nodes) > 1:
            # Sort the huffman nodes based on the frequency
            huffman_nodes.sort(key=lambda x: x.freq)

            # Create a new huffman node with the two lowest frequency nodes
            new_huffman_node = huffmanNode(None, huffman_nodes[0].freq +
                                           huffman_nodes[1].freq)
            new_huffman_node.left = huffman_nodes[0]
            new_huffman_node.right = huffman_nodes[1]

            # Remove the two lowest frequency nodes
            huffman_nodes.pop(0)
            huffman_nodes.pop(0)

            # Add the new huffman node to the list
            huffman_nodes.append(new_huffman_node)

        # Create a dictionary to store the huffman code for each character
        huffman_code = {}
        self.huffman_code_helper(huffman_nodes[0], "", huffman_code)

        return huffman_code

    def encode(self, message):
        """encode the message on the huffman codes

        Args:
            message (list): the message to be encoded
        """

        encoded_message = ""
        for symbol in message:
            encoded_message += self.huffman_codes[symbol]
        return encoded_message

    def decode(self, encoded_message):
        """decode the encoded message

        Args:
            encoded_message (str): the encoded message
        """
        reverse_lookup = {v: k for k, v in self.huffman_codes.items()}
        decoded_message = []
        current_code = ""
        for bit in encoded_message:
            current_code += bit
            if(current_code in reverse_lookup):
                decoded_message.append(reverse_lookup[current_code])
                current_code = ""
        return decoded_message


def main_encode(probability_matrix=None, message=None, image_path=None):
    """main encoder for the q1 mentioned in the assigment

    Args:
        probability_matrix (list, optional): contains 2 column one for symbol and other one for probability. Defaults to None.
        message (list, optional): 1-d array of symbols. Defaults to None.
        image_path (r string, optional): contains the path of the image. Defaults to None.

    Returns:
        encoded image or message, probability table
    """
    if(probability_matrix == None or message == None):
        im = Image.open(image_path)
        pixel_map = im.load()
        width, height = im.size
        flatten_image = []
        freq_table = {}
        for i in range(height):
            for j in range(width):
                value = pixel_map[i, j]
                flatten_image.append(value)
                if(value not in freq_table):
                    freq_table[value] = 1
                else:
                    freq_table[value] += 1
        total_pixel = width*height
        probability_matrix = [[k, v/total_pixel]
                              for k, v in freq_table.items()]
    huffman_coder = huffmanCoding(probability_matrix)
    return huffman_coder.encode(flatten_image), probability_matrix


def main_decode(probability_matrix, data_addr, image_dimention=None):
    with open(data_addr, 'r') as f:
        message = f.read()
    decoded_message = huffmanCoding(probability_matrix).decode(message)
    
    if(image_dimention == None):
        print(decoded_message)
    else:
        print(len(decoded_message))
        im = Image.new('L', image_dimention)
        pixel_map = im.load()
        for i in range(image_dimention[0]):
            for j in range(image_dimention[1]):
                pixel_map[i, j] = decoded_message[(image_dimention[1]*i)+j]
        im.show()
        im.save("decoded.png")


if __name__ == "__main__":
    # probability_matrix = [(1, 0.25), (2, 0.30), (3, 0.12), (4, 0.15), (5, 0.18)]
    # huffman_coder = huffmanCoding(probability_matrix)
    # huffman_coding_symbols = huffman_coder.huffman_codes
    # print(huffman_coding_symbols)
    # message = [1, 2, 3, 4, 5]

    # huffman_encoded = huffman_coder.encode(message)
    # print(huffman_encoded)

    # huffman_decoded = huffman_coder.decode(huffman_encoded)
    # print(huffman_decoded)
    image_path = r"8-bit-256-x-256-Grayscale-Image.png"
    encoded_image, probability_matrix = main_encode(image_path=image_path)
    with open(f"compressed.bin", "w") as f:
        f.write(encoded_image)
    main_decode(probability_matrix, f"compressed.bin", (256, 256))
