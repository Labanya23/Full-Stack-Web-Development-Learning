people = [
    {"name": "Harry", "house": "Gryff"},
    {"name": "Cho","house":"rqven"},
    {"name": "Dracer", "house": "style"}
]
#people.sort()

#print(people)
"""

def f(person):
    return person["house"]


people.sort(key=f)
"""

people.sort(key=lambda person: person["name"])

print(people)