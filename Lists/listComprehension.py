people_you_know = ["Rolf", " John", "anna", "GREG"]

normalized_people = [person.strip(" ").lower() for person in people_you_know]
capFirst_people = [(person[:1].upper()+person[1:]) for person in normalized_people]
print(normalized_people)
print(capFirst_people)
