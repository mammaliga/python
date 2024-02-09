# def return_day(num):
#     days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#     if num < 1 or num > 7:
#         return None
#     return days[num - 1] 




def return_day(num):
    days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
    if num < 1 or num > 7:
        return None
    return days[num] 

print(return_day(1)) 
print(return_day(2))
print(return_day(3)) 
print(return_day(4)) 
print(return_day(5)) 
print(return_day(6)) 
print(return_day(7)) 
print(return_day(0))
print(return_day(-12))
print(return_day(8)) 
