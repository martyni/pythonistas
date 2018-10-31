Information = dict()

Fields = ["Name", "DOB", "Age"]

for field in Fields:
    question = "What is your " + field + "?"
    Information[field] = raw_input(question)


for field, value in Information.items():
    print "Your", field, "is", value
