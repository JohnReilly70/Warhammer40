import re

String_Input = "1d10 + 2"

#regex = r"(?P<Num_Of_Die>\d+)d(?P<Sides_Of_Die>\d+)\s+\s(?P<Damage_Constant>\d+)"
regex = r"(?P<Num_Of_Die>\d+)d(?P<Sides_Of_Die>\d+)\s*[+]\s*(?P<Damage_Constant>\d+)"

matches = re.search(regex, String_Input)

print(matches)
print(matches.group("Num_Of_Die"))
print(matches.group("Sides_Of_Die"))
print(matches.group("Damage_Constant"))