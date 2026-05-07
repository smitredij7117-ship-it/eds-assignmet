from datetime import date

#write your code here...
d1_str = input().strip()
d2_str = input().strip()


y1, m1, d1 = map(int, d1_str.split('-'))
y2, m2, d2 = map(int, d2_str.split('-'))


date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)


diff = (date2 - date1).days
print(diff)