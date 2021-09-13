from q1 import paths_info
import argparse
# This is a test script to find all 4 and m-paths between p-(3,0) and q-(1,4) in the image given in Q1
# Zero-indexing has been used here

def conv_list(list1,rows, columns):     # List into a 2-D matrix
        result=[]               
        start = 0
        end = columns
        for i in range(rows): 
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--m",default=5,type=int,help='Rows in 2-D Image')
    parser.add_argument("--n",default=5,type=int,help='Columns in 2-D Image')
    parser.add_argument("--I",nargs='+',type=int,help='2-D matrix')
    parser.add_argument("--x1",default=3,type=int,help='x-coordinate of first point')
    parser.add_argument("--y1",default=0,type=int,help='y-coordinate of first point')
    parser.add_argument("--x2",default=1,type=int,help='x-coordinate of second point')
    parser.add_argument("--y2",default=4,type=int,help='y-coordinate of second point')
    parser.add_argument("--V",nargs='+',type=int,help='Array of pixel values within V')
    parser.add_argument("--pt",nargs='+',type=int,help='Path Type')
    args= parser.parse_args()

    if args.I!=None:
        M=conv_list(args.I,args.m,args.n)
    else:
        M=[[1,0,3,2,4],[4,3,4,0,2],[2,2,1,3,0],[2,4,0,2,3],[3,2,4,1,0]]


    if args.V!=None:
        V=args.V
    else:
        V=[4,2]

    if args.pt!=None:
        path_type=args.pt   # all 4-paths and m-paths as asked in the sample test case of Q1
    else:
        path_type=[4,10]
   

    # Finding 4-paths
    if 4 in path_type:
        ans,Lengths,shortest_paths=paths_info(M,args.x1,args.y1,args.x2,args.y2,V,4)
        if len(ans) != 0:
            print()
            print('All 4-paths from ({},{}) to ({},{}) and their lengths are given below'.format(args.x1,args.y1,args.x2,args.y2))   
            print()
            for i in range(len(ans)):
                print('Path - ',ans[i],end=' ')
                print('Length - ',Lengths[i])

            print()
            print('The shortest path(s) is/are :')
            print()
            for i in range(len(shortest_paths)):
                print('Path - ',shortest_paths[i],end=' ')
                print('Length - ',Lengths[i])
        else:
            print()
            print("No 4-Path exists between ({},{}) and ({},{})".format(args.x1,args.y1,args.x2,args.y2))



    #Finding 8-paths
    if 8 in path_type:
        ans,Lengths,shortest_paths=paths_info(M,args.x1,args.y1,args.x2,args.y2,V,8)
        if len(ans) != 0:
            print()
            print('All 8-paths from ({},{}) to ({},{}) and their lengths are given below'.format(args.x1,args.y1,args.x2,args.y2))   
            print()
            for i in range(len(ans)):
                print('Path - ',ans[i],end=' ')
                print('Length - ',Lengths[i])

            print()
            print('The shortest path(s) is/are :')
            print()
            for i in range(len(shortest_paths)):
                print('Path - ',shortest_paths[i],end=' ')
                print('Length - ',Lengths[i])
        else:
            print()
            print("No 8-Path exists between ({},{}) and ({},{})".format(args.x1,args.y1,args.x2,args.y2))

    # Finding m-paths
    if 10 in path_type:

        ans,Lengths,shortest_paths=paths_info(M,args.x1,args.y1,args.x2,args.y2,V,10)

        if len(ans)!=0:
            print()
            print('All m-paths from ({},{}) to ({},{}) and their lengths are given below'.format(args.x1,args.y1,args.x2,args.y2))   
            print()
            for i in range(len(ans)):
                print('Path - ',ans[i],end=' ')
                print('Length - ',Lengths[i])

            print()
            print('The shortest path(s) is/are :')
            print()
            for i in range(len(shortest_paths)):
                print('Path - ',shortest_paths[i],end=' ')
                print('Length - ',Lengths[i])

        else:
            print()
            print("No m-Path exists between ({},{}) and ({},{})".format(args.x1,args.y1,args.x2,args.y2))
