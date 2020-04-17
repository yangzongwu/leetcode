'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

'''
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        tmp1=int(date1.replace('-',''))
        tmp2=int(date2.replace('-',''))
        if tmp1>tmp2:
            date1,date2=date2,date1
        month=[31,28,31,30,31,30,31,31,30,31,30,31]
        [y1,m1,d1]=[int(x) for x in date1.split('-')]
        [y2,m2,d2]=[int(x) for x in date2.split('-')]
        if y1==y2:
            if m1==m2:
                return d2-d1
            else:
                cur=0
                for i in range(m1,m2-1):
                    cur+=month[i]
                cur+=d2+month[m1-1]-d1
                if m1<=2 and m2>2:
                    if y1%400==0 or (y1%100!=0 and y1%4==0):
                        cnt+=1
                return cur
        else:
            end_of_date=self.calculatFromDToEnd(y1,m1,d1,month)
            mid_of_date=self.calculatFromYToY(y1,y2,month)
            from_to_date=self.calculatFrontToD(y2,m2,d2,month)
            return end_of_date+mid_of_date+from_to_date

    def calculatFromYToY(self,y1,y2,month):
        cnt=0
        years=sum(month)
        for year in range(y1+1,y2):
            if year%400==0 or (year%100!=0 and year%4==0):
                cnt+=1
            cnt+=years
        return cnt
    
    def calculatFrontToD(self,y,m,d,month):
        if m==1:return d
        if m==2:return month[0]+d
        cnt=d
        for i in range(m-1):
            cnt+=month[i]
        if y%400==0 or (y%100!=0 and y%4==0):
            cnt+=1
        return cnt

    def calculatFromDToEnd(self,y,m,d,month):
        cnt=sum(month)-self.calculatFrontToD(y,m,d,month)
        if y%400==0 or (y%100!=0 and y%4==0):
            cnt+=1
        return cnt
