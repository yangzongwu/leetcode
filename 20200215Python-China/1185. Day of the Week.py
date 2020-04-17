'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        today_y=2020
        today_m=4
        today_d=17
        value="Friday"
        cur=['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
        if today_y<year or (today_y==year and today_m<month) or (today_y==year and today_m==month and today_d<day):
            gap=self.caldaysbetween(today_d,today_m,today_y,day,month,year)
            gap=gap%7
            return cur[gap]
        else:
            gap=self.caldaysbetween(day,month,year,today_d,today_m,today_y)
            gap=gap%7
            return cur[-gap]

    def caldaysbetween(self,d1,m1,y1,d2,m2,y2):
        month=[31,28,31,30,31,30,31,31,30,31,30,31]
        if y1==y2:
            if m1==m2:
                return d2-d1
            else:
                cnt=0
                if m2>2 and m1<=2:
                    if y1%400==0 or (y1%100!=0 and y1%4==0):
                        cnt+=1
                cnt+=d2+month[m1-1]-d1
                for k in range(m1,m2-1):
                    cnt+=month[k]
                return cnt
        else:
            rest_day=self.getFromDToEnd(d1,m1,y1,month)
            mid_day=self.getBetweenYToY(y1,y2,month)
            end_day=self.getFromBeginToD(d2,m2,y2,month)
            return rest_day+mid_day+end_day

    def getBetweenYToY(self,y1,y2,month):
        tmp=sum(month)
        days=0
        for y in range(y1+1,y2):
            days+=tmp
            if y%400==0 or (y%100!=0 and y%4==0):
                days+=1
        return days

    def getFromBeginToD(self,d,m,y,month):
        if m==1:
            return d
        if m==2:
            return 31+d
        cnt=d
        if y%400==0 or (y%100!=0 and y%4==0):
            cnt+=1
        for k in range(m-1):
            cnt+=month[k]
        return cnt
    
    def getFromDToEnd(self,d,m,y,month):
        cnt=sum(month)
        if y%400==0 or (y%100!=0 and y%4==0):
            cnt+=1
        return cnt-self.getFromBeginToD(d,m,y,month)

