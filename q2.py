from PIL import Image
import random
import argparse


def is_rectangle_overlap(R1, R2):
    """check whether R1 and R2 are overlapping

    Args:
        R1 ([tuple]): [(x1,y1,x2,y2) (x1,y1) is the coordinates of its bottom-left corner, 
                        and (x2, y2) is the coordinates of its top-right corner.]
        R2 ([tuple]): [same as R1]

    Returns:
        [boolean]: [whether R1 and R2 overlapping]
    """

    # If one rectangle is on left side of other
    if R1[0] > R2[2]+1 or R2[0] > R1[2]+1:
        return False

    # If one rectangle is above other
    if R1[1] > R2[3]+1 or R2[1] > R1[3]+1:
        return False

    return True


def is_overlapping(width, height, x, y, rectangle_list):
    """check if the rectangle is non-overlapping with the other ractangles

    Args:
        width ([int]): [The width of the rectangle]
        height ([int]): [The height of the rectangle]
        x ([int]): [The x-coordinate of the bottom left corner of the rectangle]
        y ([int]): [The y-coordinate of the bottom left corner of the rectangle]
        rectangle_list ([list]): [The list of tuples]

    Returns:
        [boolean]: [whether the rectangle is non-overlapping with the other rectangles]
    """
    # check if the rectangle is non-overlapping with the other ractangles
    tuple_R = (x, y, x+width, y+height)
    for (x0, y0, w0, h0) in rectangle_list:
        R0 = (x0, y0, x0+w0, y0+h0)
        if is_rectangle_overlap(tuple_R, R0):
            return True
    return False


def create_rectangles(M, N, border, n, w1, w2, alpha, orientation, vf=[0], vb=[255]):
    """create a 8-bit grayscale image with n non-overlapping rectangles, display the image and save it after that

    Args:
        M ([int]): [The intial height of the image]
        N ([int]): [The intial width of the image]
        border ([int]): [The border of the image]
        n ([int]): [The number of rectangles]
        w1 ([int]): [Starting range of the width of the rectangles]
        w2 ([int]): [Ending range of the width of the rectangles]
        alpha ([int]): [The ratio of height and weight]
        orientation ([list]): [The possible oriintation of the ractangles, 1 denotes the height and width ratio is alpha 
                                2 denotes the width and height ratio is alpha]
        vf ([list]): [The possible values of the foreground color]
        vb ([list]): [The possible value of the background color]
    """

    # create a list of tuples that contains three quantities of the rectangles,
    # (x,y,w,h) bottom left corner coordinates, width, height
    rectangle_list = []

    # putting n rectangles in the rectangle_list
    while(True):
        # trying for 2*n iterations
        for _ in range(2*n):
            if(len(rectangle_list) == n):
                break
            # randomly uniformly generate the width of the rectangle in range [w1,w2]
            width = int(random.uniform(w1, w2+1))
            height = int(width * alpha)

            # choose the orientation of the ractangle
            orientation_of_rectangle = random.choice(orientation)
            # flip the ractangle if the orientation is 2
            if(orientation_of_rectangle == 2):
                width, height = height, width

            # randomly uniformly generate the x-coordinate of the bottom left corner of the rectangle
            x = int(random.uniform(1, N-width-1))
            # randomly uniformly generate the y-coordinate of the bottom left corner of the ractangle
            y = int(random.uniform(1, M-height-1))

            if(is_overlapping(width, height, x, y, rectangle_list) == False):
                rectangle_list.append((x, y, width, height))

        if(len(rectangle_list) == n):
            break

        # if the non-overlapping rectangles are not enough, then increase the canvas size
        M = 2*M
        N = 2*N

    # choosing the forground and background color
    cf = random.choice(vf)
    cb = random.choice(vb)

    # creating the image
    rectangle_image = Image.new('L', (N+2*border, M+2*border), cb)

    # Extracting pixel map:
    pixel_map = rectangle_image.load()

    # adding the border in the image
    for i in range(border):
        for j in range(N+2*border):
            pixel_map[i, j] = cf
            pixel_map[(M+2*border)-1-i, j] = cf
    for j in range(border):
        for i in range(M+2*border):
            pixel_map[i, j] = cf
            pixel_map[i, (N+2*border)-1-j] = cf

    # filling rectangles in the image
    for (x0, y0, w0, h0) in rectangle_list:
        for i in range(x0, x0+w0):
            for j in range(y0, y0+h0):
                pixel_map[i+border, j+border] = cf

    # displaying the image
    rectangle_image.show()

    # saving the image after displaying
    rectangle_image.save("rectangle.jpg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--M",default=500,type=int,help='height of Image/Canvas')
    parser.add_argument("--N",default=500,type=int,help='width of Image/Canvas')
    parser.add_argument("--border",default=10,type=int,help='Border of Image')
    parser.add_argument("--n",default=25,type=int,help='Number of Rectangles')
    parser.add_argument("--w1",default=10,type=int,help='Range of width for rectangles (w1,w2)')
    parser.add_argument("--w2",default=100,type=int,help='Range of width for rectangles (w1,w2)')
    parser.add_argument("--alpha",default=2,type=int,help='height to width ratio')
    parser.add_argument('--vf', nargs='+', type=int)
    parser.add_argument('--vb', nargs='+', type=int)
    args= parser.parse_args()
    # create_rectangles(M=500, N=500, border=10, n=25, w1=10,
    #                  w2=100, alpha=2, orientation=[1, 2], vf=range(0, 128, 1), vb=range(128, 256, 1))
    if args.vf != None:
        vf=args.vf
    else:
        vf=range(0,128,1)
    if args.vb != None:
        vb=args.vb
    else:
        vb=range(128,256,1)
    create_rectangles(M=args.M, N=args.N, border=args.border, n=args.n, w1=args.w1,
                     w2=args.w2, alpha=args.alpha, orientation=[1, 2], vf=vf, vb=vb)

