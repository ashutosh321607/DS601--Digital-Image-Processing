from q1 import paths_info

# This is a test script to find all 4 and m-paths between p-(3,0) and q-(1,4) in the image given in Q1
# Zero-indexing has been used here

M=[[1,0,3,2,4],[4,3,4,0,2],[2,2,1,3,0],[2,4,0,2,3],[3,2,4,1,0]] # Given 2-D image 
x1 = 3 # row of p
y1 = 0 # column of p
x2 = 1 # row of q
y2 = 4 # column of q
V=[4,2]

# Finding 4-paths
ans,Lengths,shortest_paths=paths_info(M,x1,y1,x2,y2,V,4)
if len(ans) != 0:
    print()
    print('All 4-paths from ({},{}) to ({},{}) and their lengths are given below'.format(x1,y1,x2,y2))   
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
    print("No 4-Path exists between ({},{}) and ({},{})".format(x1,y1,x2,y2))

# Finding m-paths
ans,Lengths,shortest_paths=paths_info(M,x1,y1,x2,y2,V,10)

if len(ans)!=0:
    print()
    print('All m-paths from ({},{}) to ({},{}) and their lengths are given below'.format(x1,y1,x2,y2))   
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
    print("No m-Path exists between ({},{}) and ({},{})".format(x1,y1,x2,y2))
