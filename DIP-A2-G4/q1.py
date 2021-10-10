from PIL import Image, ImageOps
import heapq


class huffmanNode:
    """The huffmanNode class is used to create a node for the huffman tree.
    """

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq <= other.freq


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
        # delta for minor error in decimals
        delta = 0.000001
        return total_probability >= 1 - delta

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
        # Create a heap of huffman nodes
        huffman_nodes = []
        for i in range(len(self.probability_matrix)):
            heapq.heappush(
                huffman_nodes,
                huffmanNode(
                    self.probability_matrix[i][0], self.probability_matrix[i][1])
            )

        # Create a list of huffman nodes
        while len(huffman_nodes) > 1:
            # Remove the two lowest frequency nodes
            first = heapq.heappop(huffman_nodes)
            second = heapq.heappop(huffman_nodes)

            # Create a new huffman node with the two lowest frequency nodes
            new_huffman_node = huffmanNode(None, first.freq +
                                           second.freq)
            new_huffman_node.left = first
            new_huffman_node.right = second

            # Add the new huffman node to the list
            heapq.heappush(huffman_nodes, new_huffman_node)

        # Create a dictionary to store the huffman code for each character
        huffman_code = {}
        huffman_node = heapq.heappop(huffman_nodes)
        self.huffman_code_helper(huffman_node, "", huffman_code)

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
    if(message != None and probability_matrix != None):
        huffman_coder = huffmanCoding(probability_matrix)
        return huffman_coder.encode(message), probability_matrix

    og_image = Image.open(image_path)
    # applying grayscale method
    im = ImageOps.grayscale(og_image)
    pixel_map = im.load()
    width, height = im.size
    print(width, height)
    flatten_image = []
    freq_table = {}

    for i in range(width):
        for j in range(height):
            value = pixel_map[i, j]
            flatten_image.append(value)
            if(value not in freq_table):
                freq_table[value] = 1
            else:
                freq_table[value] += 1
    total_pixel = width*height
    probability_matrix = [(k, v/total_pixel)
                          for k, v in freq_table.items()]

    huffman_coder = huffmanCoding(probability_matrix)
    return huffman_coder.encode(flatten_image), probability_matrix


def main_decode(probability_matrix, data_addr, image_dimention=None):
    """main decoder function for the q1 mentioned in the assignment 

    Args:
        probability_matrix (list): list of tuples containing the character and
                                  the probability of the character
        data_addr (string): address of the compressed file
        image_dimention (tuple, optional): tuple of the height and width. Defaults to None.
    """
    with open(data_addr, 'r') as f:
        message = f.read()
    decoded_message = huffmanCoding(probability_matrix).decode(message)
    print("\nMessage after decoding")
    if(image_dimention == None):
        print(decoded_message)
    else:
        im = Image.new('L', image_dimention)
        pixel_map = im.load()
        for i in range(image_dimention[0]):
            for j in range(image_dimention[1]):
                pixel_map[i, j] = decoded_message[(image_dimention[1]*i)+j]
        im.show()
        im.save("decoded.png", "PNG")
