class Solution:
    def dayOfYear(self, date: str) -> int:
        date_list=date.split('-')
        year,month,day=date_list[0],date_list[1],date_list[2]
        days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
        rep=int(day)
        for k in range(int(month)-1):
            rep+=days_list[k]
        if ((int(year)%100!=0 and int(year)%4==0) or ((int(year)%100==0 and int(year)%400==0))) and int(month)>2:
            rep+=1
        return rep
