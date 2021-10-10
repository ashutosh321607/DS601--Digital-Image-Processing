
from PIL import Image
from decimal import Decimal, getcontext

getcontext().prec = 50    # Setting Decimal precision upto 50 places





def arithmetic(prob_matrix=None,N=10,message=None,image_path=None):    # Function to perform arithmetic coding
    cumul_matrix={}
    if (prob_matrix == None or message == None):   # If probability table or 1-D array to encode are not given
        im = Image.open(image_path).convert('L')
        pixel_map = im.load()
        width, height = im.size
        freq_matrix={}    
        img_array=[]    # Flattened 1-D list of pixel values of image
        for i in range(width):
            for j in range(height):
                value=pixel_map[i,j]
                img_array.append(value)
                if (value not in freq_matrix):
                    freq_matrix[value]=1
                else:
                    freq_matrix[value]+=1
        total_pixels= width*height
        prob_matrix=[]
        for i in sorted(freq_matrix):
            prob_matrix.append([i,freq_matrix[i]/total_pixels])     # Probability values of intensities stored in a 2-D matrix format where 1st column is intensity value and second column is probability       
        if message==None:         # If no message to encode is given, encode the image
            message=img_array
        
    

    sum=0
    for i in range(len(prob_matrix)):
        cumul_matrix[prob_matrix[i][0]]=[Decimal(sum),Decimal(sum+prob_matrix[i][1])]  # Generating a cumulative probabilty table with each symbol assigned a cumulative range (min - max)
        sum=sum+prob_matrix[i][1]
    msglen=len(message)
    encoded=[]
    for i in range(0,msglen,N):
        initial=i
        final=min(msglen,i+N)
        start=Decimal(0.0) # Current range beginning    # Cumulative Probability ranges
        end=Decimal(1.0) # Current range ending
        for j in range(initial,final):       # Reading one sub-message 
            char=message[j]
            prev_start=start
            length=end-start
            start=prev_start+ length*cumul_matrix[char][0]     # Updating the range with each symbol
            end=prev_start + length*cumul_matrix[char][1]
        diff= end-start
        decimal_places = abs(int(f'{diff:e}'.split('e')[-1]))   # Minimum decimal_places to represent the decimal
        ans=round((start+end)/2,decimal_places)      # Taking average of range_start and range_ending to minimise chances of error
        encoded.append(ans)

    return encoded,prob_matrix




