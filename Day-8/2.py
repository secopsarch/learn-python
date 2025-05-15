# Functions Demo and practice
# Key Word Arguments

# def colors_in(basket, rainbow):
#   print(f"is it {basket}, or {rainbow}")

# colors_in(rainbow = "white",basket = "orange")



# def calculate_love_score(name1, name2):
#   for name in name1 and name2:
#     if name2 in name1():
#       name += True
    
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Arun Bharathwaj", "Pavithra")    
