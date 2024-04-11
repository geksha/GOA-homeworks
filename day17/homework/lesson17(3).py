#3) შექმენით ფუნქცია რომელიც გამოითვლის კენტების და ლუწების ჯამს ცალცალკე, დააბრუნეთ სია სადაც იქნება ეს ჯამები ჩასმული, შესატანი მონაცემები [1,2,3,4,5] ---- გამოსატანი მონაცემები [6, 9] (edited)
#[8:49 PM]
# num % 2 == 0
# num % 2 != 0
even_list = []
odd_list = []

def summ(listn):
    for i in listn:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    sum_even = sum(even_list)
    sum_odd = sum(odd_list)
    return [sum_even, sum_odd]
          


print(summ([1,2,3,4,5]))
print(summ([1,2,3,4,5,6,7,8,9,10]))
