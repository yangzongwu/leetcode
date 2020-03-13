'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder=='#':
            return True
            
        preorder_list=preorder.split(',')
        preorder_stack=[]
        
        k=0
        while k<len(preorder_list):
            if preorder_list[k]!="#":
                preorder_stack.append(preorder_list[k])
                k+=1
            else:
                if not preorder_stack:
                    return False
                if preorder_stack[-1]=='#':
                    if len(preorder_stack)<2:
                        return False
                    preorder_stack.pop()
                    preorder_stack.pop()
                    if not preorder_stack and k==len(preorder_list)-1:
                        return True
                else:
                    preorder_stack.append('#')
                    k+=1
        return len(preorder_list)==0

                    
