from PIL import Image
import random


def is_rectangle_overlap(R1, R2):
    """check whether R1 and R2 overlapping

    Args:
        R1 ([tuple]): [(x1,y1,x2,y2) (x1,y1) is the coordinates of its bottom-left corner, 
                        and (x2, y2) is the coordinates of its top-right corner.]
        R2 ([tuple]): [same as R1]

    Returns:
        [boolean]: [whether R1 and R2 overlapping]
    """
    if (R1[0] >= R2[2]) or (R1[2] <= R2[0]) or (R1[3] <= R2[1]) or (R1[1] >= R2[3]):
        return False
    return True


def is_overlapping(width, height, x, y, ractangle_list):
    """check if the ractangle is non-overlapping with the other ractangles

    Args:
        width ([int]): [The width of the ractangle]
        height ([int]): [The height of the ractangle]
        x ([int]): [The x-coordinate of the bottom left corner of the ractangle]
        y ([int]): [The y-coordinate of the bottom left corner of the ractangle]
        ractangle_list ([list]): [The list of tuples]
    """
    # check if the ractangle is non-overlapping with the other ractangles
    tuple_R = (x, y, x+width, y+height)
    for (x0, y0, w0, h0) in ractangle_list:
        R0 = (x0, y0, x0+w0, y0+h0)
        if is_rectangle_overlap(tuple_R, R0):
            return True
    return False


def create_ractangle(M, N, border, n, w1, w2, alpha, orientation, vf=0, vb=255):
    """create a 8-bit grayscale image with n ractangles

    Args:
        M ([int]): [The intial height of the image]
        N ([int]): [The intial width of the image]
        border ([int]): [The border of the image]
        n ([int]): [The number of ractangles]
        w1 ([int]): [Starting range of the width of the ractangles]
        w2 ([int]): [Ending range of the width of the ractangles]
        alpha ([int]): [The ratio of height and weight]
        orientation ([int]): [The orientation of the ractangles]
        vf ([int]): [The value of the foreground color]
        vb ([int]): [The value of the background color]
    """

    # create a list of tuples that contains three quantities of the ractangles,
    # (x,y,w, h) bottom left corner and width
    ractangle_list = []

    # putting n ractangles in the ractangle_list
    while(True):
        # trying for 2*n iterations
        for _ in range(2*n):
            if(len(ractangle_list) == n):
                break
            # randomly uniformly generate the width of the ractangle in range [w1,w2]
            width = int(random.uniform(w1, w2+1))
            height = int(width * alpha)
            # randomly uniformly generate the x-coordinate of the bottom left corner of the ractangle
            x = int(random.uniform(0, N-width))
            # randomly uniformly generate the y-coordinate of the bottom left corner of the ractangle
            y = int(random.uniform(height, M))

            if(is_overlapping(width, height, x, y, ractangle_list) == False):
                ractangle_list.append((x, y, width, height))
                
        if(len(ractangle_list) == n):
            break
        
        # if the non-overlapping ractangles are not enough, then increase the canvas size
        M = 2*M
        N = 2*N
    
    # creating the image
    ractangle_image = Image.new('L', (N+2*border, M+2*border), vb)
    
    # Extracting pixel map:
    pixel_map = ractangle_image.load()
    
    # adding the boarder in the image
    for i in range(border):
        for j in range(N+2*border):
            pixel_map[i,j] = vf
            pixel_map[(M+2*border)-1-i,j] = vf
    for j in range(border):
        for i in range(M+2*border):
            pixel_map[i,j] = vf
            pixel_map[i,(N+2*border)-1-j] = vf
    
    # filling rectangles in the image
    for (x0, y0, w0, h0) in ractangle_list:
        for i in range(x0, x0+w0):
            for j in range(y0, y0-h0,-1):
                pixel_map[i,j] = vf
                
    
    ractangle_image.show()
   
   
   
   
    
if __name__ == "__main__":
    create_ractangle(M=500, N=500, border=10, n=15, w1=10, w2=100, alpha=4, orientation=0)