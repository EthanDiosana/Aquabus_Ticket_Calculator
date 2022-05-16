

from turtle import update
from Route import Route

def main(fileName):
    """ Gathers console input and saves a parsable Route string to a .txt file. """

    print("\nThis file saves routes to a .txt file using console input.")

    message = "Enter route start.\n"
    x = str(input(message)).upper()
    start = x

    message = "Enter route end.\n"
    x = str(input(message)).upper()
    end = x

    message = "Enter cost adults one way.\n"
    x = str(input(message))
    Adults_OW = x

    message = "Enter cost adults return trip.\n"
    x = str(input(message))
    Adults_RT = x

    message = "Enter adults one way ticket amount.\n"
    x = str(input(message))
    Adults_Tickets = x

    message = "Enter cost child / senior one way.\n"
    x = str(input(message))
    CS_OW = x

    message = "Enter cost child / senior return trip.\n"
    x = str(input(message))
    CS_RT = x

    message = "Enter child / senior one way ticket amount.\n"
    x = str(input(message))
    CS_Tickets = x

    parsable_string = createParsableString(start, end, Adults_OW, Adults_RT, Adults_Tickets, CS_OW, CS_RT, CS_Tickets)
    saveToFile(fileName, start, end, parsable_string)

    main(fileName)



def createParsableString(start, end, adults_OW, adults_RT, adults_tickets, CS_OW, CS_RT, CS_tickets):
    """ Returns a parsable string of Route information. """
    output = ""
    output += start + "|"
    output += end + "|"
    output += adults_OW + "|"
    output += adults_RT + "|"
    output += adults_tickets + "|"
    output += CS_OW + "|"
    output += CS_RT + "|"
    output += CS_tickets + "\n"
    return output

def routeIsInFile(fileName, start, end):
    """ Returns True if the given Route is already in the file. Returns False if it is not. """
    output = False
    try:
        with open(fileName, "r") as file:
            lines = file.readlines()
            for line in lines:
                parsed_line = line.split("|")
                if(parsed_line[0] == start and parsed_line[1] == end):
                    print("Route already in file.")
                    output = True
            file.close()
    except FileNotFoundError:
        print(fileName + " not found.")
    
    return output

def updateRouteInFile(fileName, start, end, parsable_string):
    """ Updates a given Route in a .txt file. """
    try:
        lines = []
        with open(fileName, "r") as file:
            lines = file.readlines()
            for x in range (0, len(lines)):
                parsed_line = lines[x].split("|")
                if(parsed_line[0] == start and parsed_line[1] == end):
                    lines[x] = parsable_string
                    print(lines[x])
            file.close()
        with open(fileName, "w") as file:
            file.writelines(lines)
            print(start + " to " + end + " updated! \n")
            file.close()
    except FileNotFoundError:
        print(fileName + " not found.")


def saveToFile(fileName, start, end, parsable_string):
    """ Appends a new parsable Route string to a file if it is not already in the file. """
    try:
        if(routeIsInFile(fileName, start, end)):
            msg = "Route is already in file. Update? y/n\n"
            x = str(input(msg))
            if(x == "y"):
                updateRouteInFile(fileName, start, end, parsable_string)
            else:
                print("Exiting...")
                exit()
        else: 
            with open(fileName, "a") as file:
                file.write(parsable_string)
                file.close()
            print(start + " to " + end + " saved!")
    except FileNotFoundError:
        print(fileName + " not found.")



main("route_data.txt")