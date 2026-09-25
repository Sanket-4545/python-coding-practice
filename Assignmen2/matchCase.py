color = input("Enter your favorite color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look!!")
    case "Red":
        print("stop..")
    case _:
        print("Invalid color")