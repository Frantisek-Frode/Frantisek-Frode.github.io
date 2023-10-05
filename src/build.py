import os

contentIdentificator = "<!--[page]-->"
head = ""
tail = ""

with open("./src/template.html", "r") as template:
    content = template.read()
    index = content.find(contentIdentificator)
    head = content[:index]
    tail = content[index + len(contentIdentificator):]

for file in os.listdir("./src/content"):
    with open("./" + file, "w") as target:
        target.write(head)
        with open("./src/content/" + file, "r") as source:
            target.write(source.read())
        target.write(tail)