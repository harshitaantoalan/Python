# 02-flip-name.py[cite: 1]
# Topic: Reversing a String with Recursion[cite: 1]

def flip_name(s):[cite: 1]
    if len(s) == 1:[cite: 1]
        return s[cite: 1]
    return flip_name(s[1:]) + s[0][cite: 1]

input("flip_name recurses on s[1:] then attaches s[0] at the end.  Press Enter ")[cite: 1]
print("  flip_name('Maya') =", flip_name('Maya'))[cite: 1]
print("  flip_name('Code') =", flip_name('Code'))[cite: 1]

name = input("Enter a name (try 'Riya' or 'Dev'): ")[cite: 1]
guess = input("What is flip_name(" + name + ")? ")[cite: 1]
input("flip_name(s) = flip_name(s[1:]) + s[0]  first character lands last. Press Enter ")[cite: 1]
print("  flip_name('" + name + "') =", flip_name(name), " your guess:", guess)[cite: 1]