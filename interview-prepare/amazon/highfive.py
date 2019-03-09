#Author:YZW
'''
Description
There are two properties in the node student id and scores, to ensure that each student
will have at least 5 points, find the average of 5 highest scores for each person.
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
'''
def highfive(nums):
    import heapq
    dictnum={}
    for num in nums:
        if num[0] not in dictnum:
            stack=[]
            heapq.heappush(stack,num[1])
            dictnum[num[0]]=stack
        else:
            heapq.heappush(dictnum[num[0]],num[1])
            if len(dictnum[num[0]])>5:
                heapq.heappop(dictnum[num[0]])
    rep=[]
    print(dictnum)
    for key in dictnum:
        average=sum(dictnum[key])/5
        rep.append([key,average])
    return rep


print(highfive([[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61],[1,100]]))
