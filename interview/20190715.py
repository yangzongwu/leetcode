'''
( )
1:" " invalid
2:"()()" valid
3:"((()(" invalid
'''

def isValid(self,s):
    if len(s)==0:
        return False
    
    rep=[]
    for ss in s:
       if ss=='(':
           rep.append(ss) 
       else:
           if len(rep)==0:
               return False
           elif rep[-1]!='(':# change '(' to ')'
               return False
           rep.pop()
     
    return len(rep)==0
    
    
 def isValidString(self,s):
     if len(s)==0:
        return False
     cnt=0
     for ss in s:
        if ss=='(':
            cnt+=1
        else:
            if cnt==0:
                return False
            cnt-=1
     return cnt==0
     
     
     
