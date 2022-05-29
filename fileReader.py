""" This file gathers the data from route_data.txt and places it in the All_Routes Route_Container(). """

from Route_Container import Route_Container
from Route import Route

All_Routes = Route_Container()

# Open the text file.
file = open("route_data.txt","r")

unparsed_lines = []


for line in file.readlines(): # Read the file line by line.
	if line != "\n": # Only read the line if isn't just a linebreak.
		parsed_line = line.rstrip()
		print(parsed_line)
		All_Routes.addRoute(Route(parsed_line))
