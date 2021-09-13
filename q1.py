def dfs_4(I,s,d,visited,ans,path):     # Function for finding all 4-paths between s and d
    if(s==d):
        ans.append(path+[s])
        return 
    
    


    x=s[0]
    y=s[1]
    
    visited[x][y]=1
    
    if(x-1>=0 and not visited[x-1][y] and I[x-1][y]):
        dfs_4(I,(x-1,y),d,visited,ans,path+[s])
    if(y-1>=0 and not visited[x][y-1] and I[x][y-1]):
        dfs_4(I,(x,y-1),d,visited,ans,path+[s])
    if(x+1<len(I) and not visited[x+1][y] and I[x+1][y]):
        dfs_4(I,(x+1,y),d,visited,ans,path+[s])
    if(y+1<len(I[0]) and not visited[x][y+1] and I[x][y+1]):
        dfs_4(I,(x,y+1),d,visited,ans,path+[s])
    
    visited[x][y]=0  
    return 





def dfs_8(I,s,d,visited,ans,path):         # Function for finding all 8-paths between s and d
    if(s==d):
        ans.append(path+[s])
        return 
    
    


    x=s[0]
    y=s[1]
    
    visited[x][y]=1
    
    if(x-1>=0 and not visited[x-1][y] and I[x-1][y]):
        dfs_8(I,(x-1,y),d,visited,ans,path+[s])
    if(y-1>=0 and not visited[x][y-1] and I[x][y-1]):
        dfs_8(I,(x,y-1),d,visited,ans,path+[s])
    if(x+1<len(I) and not visited[x+1][y] and I[x+1][y]):
        dfs_8(I,(x+1,y),d,visited,ans,path+[s])
    if(y+1<len(I[0]) and not visited[x][y+1] and I[x][y+1]):
        dfs_8(I,(x,y+1),d,visited,ans,path+[s])
    if(x-1>=0 and y-1>=0 and not visited[x-1][y-1] and I[x-1][y-1]):
        dfs_8(I,(x-1,y-1),d,visited,ans,path+[s])
    if(x-1>=0 and y+1<len(I[0]) and not visited[x-1][y+1] and I[x-1][y+1]):
        dfs_8(I,(x-1,y+1),d,visited,ans,path+[s])
    if(x+1<len(I) and y-1>=0 and not visited[x+1][y-1] and I[x+1][y-1]):
        dfs_8(I,(x+1,y-1),d,visited,ans,path+[s])
    if(x+1<len(I) and y+1<len(I[0]) and not visited[x+1][y+1] and I[x+1][y+1]):
        dfs_8(I,(x+1,y+1),d,visited,ans,path+[s])
    
    visited[x][y]=0  
    return 
    


def dfs_m(I,s,d,visited,ans,path):                   # Function for finding all m-paths between s and d
    if(s==d):
        ans.append(path+[s])
        return 
    
    


    x=s[0]
    y=s[1]
    
    visited[x][y]=1
    
    if(x-1>=0 and not visited[x-1][y] and I[x-1][y]):
        dfs_m(I,(x-1,y),d,visited,ans,path+[s])
    if(y-1>=0 and not visited[x][y-1] and I[x][y-1]):
        dfs_m(I,(x,y-1),d,visited,ans,path+[s])
    if(x+1<len(I) and not visited[x+1][y] and I[x+1][y]):
        dfs_m(I,(x+1,y),d,visited,ans,path+[s])
    if(y+1<len(I[0]) and not visited[x][y+1] and I[x][y+1]):
        dfs_m(I,(x,y+1),d,visited,ans,path+[s])
    if(x-1>=0 and y-1>=0 and not visited[x-1][y-1] and I[x-1][y-1] and not I[x][y-1] and not I[x-1][y]):
        dfs_m(I,(x-1,y-1),d,visited,ans,path+[s])
    if(x-1>=0 and y+1<len(I[0]) and not visited[x-1][y+1] and I[x-1][y+1] and not I[x][y+1] and not I[x-1][y]):
        dfs_m(I,(x-1,y+1),d,visited,ans,path+[s])
    if(x+1<len(I) and y-1>=0 and not visited[x+1][y-1] and I[x+1][y-1] and not I[x][y-1] and not I[x+1][y]):
        dfs_m(I,(x+1,y-1),d,visited,ans,path+[s])
    if(x+1<len(I) and y+1<len(I[0]) and not visited[x+1][y+1] and I[x+1][y+1] and not I[x][y+1] and not I[x+1][y]):
        dfs_m(I,(x+1,y+1),d,visited,ans,path+[s])
    
    visited[x][y]=0  
    return 






def paths_info(I,x1,y1,x2,y2,V,path_type):
    
    #At first we create a binary matrix using V
    m=len(I)
    n=len(I[0])

    # We create a binary matrix I_bin having value 1 for all pixels with values from V and 0 otherwise. 

    I_bin=[[0 for j in range(n)] for i in range(m) ]
    visited = [[0 for j in range(n)] for i in range(m) ]
    for i in range(m):
        for j in range(n):
            if I[i][j] in V:
                I_bin[i][j]=1
    
    ans=[]

    # Depending upon the path needed, we call the appropriate dfs function
    if path_type==4:
        dfs_4(I_bin,(x1,y1),(x2,y2),visited,ans,[])   
    if path_type==8:
        dfs_8(I_bin,(x1,y1),(x2,y2),visited,ans,[])
    if path_type==10:
        dfs_m(I_bin,(x1,y1),(x2,y2),visited,ans,[])


    min=m*n+1
    shortest_paths=[]
    Lengths=[]
    for i in range(len(ans)):
        if len(ans[i]) < min:
            min=len(ans[i])
        Lengths.append(len(ans[i])-1)
    for i in range(len(ans)):
        if len(ans[i])==min:
            shortest_paths.append(ans[i])
    
    return (ans,Lengths,shortest_paths)




