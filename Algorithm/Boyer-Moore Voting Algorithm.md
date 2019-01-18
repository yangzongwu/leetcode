#  Boyer-Moore majority vote algorithm(摩尔投票算法)  

##  简介  
Boyer-Moore majority vote algorithm(摩尔投票算法)是一种在线性时间O(n)和空间复杂度的情况下，
在一个元素序列中查找包含最多的元素。它是以Robert S.Boyer和J Strother Moore命名的，1981年发
明的，是一种典型的流算法(streaming algorithm)。  

在它最简单的形式就是，查找最多的元素，也就是在输入中重复出现超过一半以上(n/2)的元素。如果序列
中没有最多的元素，算法不能检测到正确结果，将输出其中的一个元素之一。  

当元素重复的次数比较小的时候，对于流算法不能在小于线性空间的情况下查找频率最高的元素。  

##  算法描述  
算法在局部变量中定义一个序列元素(m)和一个计数器(i)，初始化的情况下计数器为0. 算法依次扫描序列
中的元素，当处理元素x的时候，如果计数器为0，那么将x赋值给m，然后将计数器(i)设置为1，如果计数器
不为0，那么将序列元素m和x比较，如果相等，那么计数器加1，如果不等，那么计数器减1。处理之后，最后
存储的序列元素(m)，就是这个序列中最多的元素。  

如果不确定是否存储的元素m是最多的元素，还可以进行第二遍扫描判断是否为最多的元素。  

##  perudocode  
Initialize an element m and a counter i with i = 0  
For each element x of the input sequence:  
  if i = 0, then assign m = x and i = 1  
  else if m = x, then assign i = i + 1  
  else assign i = i − 1  
Return m

##  题目：    
Leetcode 169（Majority Element）  
LeetCode 229 [Majority Element II]   
