people = {
"Carter": "+1-617-495-1000",
"Martian": "+1-512-277-9958",
"Bob": "+1-512-565-1325",
"Bradley": "+1-818-123-4567"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")
