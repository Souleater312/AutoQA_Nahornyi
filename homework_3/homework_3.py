print("Rules for using notes:")
print("add - add a note.")
print("earliest - display saved notes in chronological order - from the oldest to the newest.")
print("latest - display saved notes in chronological order - from the newest to the oldest.")
print("longest - display saved notes in order of their length - from the longest to the shortest.")
print("shortest - display saved notes in order of their length - from the shortest to the longest.")
print("Exit - exit")

notes = []
while True:
    command = input("Enter your command: ").lower()

    if command.title() == "Exit":
        print("Notes:")
        for note in notes:
            print("•", note)
        break
    elif command == "add":
        new_note = input("Add new note: ")
        notes.append(new_note)
    elif command == "earliest":
        print("Notes:")
        for note in notes:
            print("•", note)
    elif command == "latest":
        print("Latest notes:")
        for note in reversed(notes):
            print("•", note)
    elif command == "longest":
        sorted_notes = sorted(notes, key=len, reverse=True)
        print("Longest notes:")
        for note in sorted_notes:
            print("•", note)
    elif command == "shortest":
        sorted_notes = sorted(notes, key=len)
        print("Shortest notes:")
        for note in sorted_notes:
            print("•", note)
    else:
        print("Wrong command, try again.")