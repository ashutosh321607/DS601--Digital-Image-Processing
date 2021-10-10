
import pickle
import argparse
from q2 import *

parser = argparse.ArgumentParser()
parser.add_argument("--prob", nargs='+', type=float,
                    help='Probability matrix with 2 columns')
parser.add_argument("--N", default=10, type=int,
                    help='Number of symbols to be coded together')
parser.add_argument("--msg", nargs='+', default=None,
                    type=int, help='Message to be encoded')
parser.add_argument("--image", default='q2_Image.jpg',
                    type=str, help='Path to the image file')
args = parser.parse_args()


if args.prob != None:
    prob_matrix = conv_list(args.prob, 2)
else:
    prob_matrix = None

if args.prob != None and args.msg != None:
    args.image = None


print("Parameters used are as follows:\n\n", "Probability matrix - ", prob_matrix,
      "\n", "N - ", args.N, "\n", "Message - ", args.msg, "\n", "Image Path - ", args.image)
Encoded, prob_matrix = arithmetic(
    prob_matrix=prob_matrix, N=args.N, message=args.msg, image_path=args.image)
print("\n")


with open('q2_Output.pickle', 'wb') as f:
    # Saving Arithmetic emcoding and Probability table in q2_Output.pickle
    pickle.dump((Encoded, prob_matrix), f)


with open('q2_Output.pickle', 'rb') as f:
    # Loading Arithmetic emcoding and Probability table from q2_Output.pickle
    Encoded, prob_matrix = pickle.load(f)


print('Encoding is as follows : \n')
for i in Encoded:
    print(i)

print('\n\n')
print('The Probability matrix used is : \n')
for i in prob_matrix:
    print('Symbol : {} , probability : {}'.format(i[0], i[1]))
