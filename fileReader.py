""" This file gathers the data from the text files and places them in the data containers. """



from Route_Container import Route_Container
from Pass_Container import Pass_Container
from Classes.Route import Route
from Classes.Pass import Pass

All_Routes = Route_Container()
All_Passes = Pass_Container()

# Open the text file.
file = open("Text_Files/route_data.txt","r")

unparsed_lines = []


for line in file.readlines(): # Read the file line by line.
	if line != "\n": # Only read the line if isn't just a linebreak.
		parsed_line = line.rstrip()
		All_Routes.addRoute(Route(parsed_line))

passes_file = "Text_Files/passes_data.txt"

with open(passes_file, "r") as file_object:
	for line in file_object:
		if line != "\n":
			parsed_line = line.rstrip().split("|")
			new_pass = Pass(parsed_line[0], parsed_line[1], parsed_line[2])
			All_Passes.addPass(new_pass)


All_Passes.printAllPasses()