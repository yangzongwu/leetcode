'''
Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a 
simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever 
the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)
#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

'''
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        while '/./' in path:
            path=path.replace('/./','//')
        while '//' in path:
            path=path.replace('//','/')
        pathlist=path.split('/')
        i=0
        len_pathlist=len(pathlist)
        while i<len_pathlist:
            if pathlist[i]=='..' and i>0:
                pathlist.pop(i)
                pathlist.pop(i-1)
                len_pathlist-=2
                i-=1
            elif pathlist[i]=='..' and i==0:
                pathlist.pop(i)
                len_pathlist-=1
            else:
                i+=1
        rep=''
        for ss in pathlist:
            if ss and ss!='.':
                rep=rep+'/'+ss
        if not rep:
            return '/'
        else:
            return rep
