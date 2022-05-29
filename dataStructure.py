

class Route():

	def __init__(self, string: str):
		parsedString = string.split("|")
		self.start = parsedString[0]
		self.end = parsedString[1]
		self.name = self.start + " to " + self.end

		self.adults_OW = parsedString[2]
		self.adults_RT = parsedString[3]
		self.adults_tickets = parsedString[4]

		self.CS_OW = parsedString[5]
		self.CS_RT = parsedString[6]
		self.CS_tickets = parsedString[7]

	def returnAsDictionary(self):
		""" Returns the Route and its values as a dictionary. """
		asDictionary = {
		 "Name": self.name,
		 "Start": self.start,
		 "End": self.end,
		 "Adults_OW": self.adults_OW,
		 "Adults_RT": self.adults_RT,
		 "Adults_Tickets": self.adults_tickets,
		 "CS_OW": self.adults_OW,
		 "CS_RT": self.adults_RT,
		 "CS_Tickets": self.adults_tickets
		 }
		return asDictionary


	def toString(self):
		return ("Route Name: %s\n" % self.name
			+ "Start: %s\n" % self.start
			+ "End: %s\n" % self.end
			+ "Adults OW: $%s\n" % self.adults_OW
			+ "Adults RT: $%s\n" %self.adults_RT
			+ "Adults Tickets: %s\n" %self.adults_tickets
			+ "Children/Seniors OW: $%s\n" %self.CS_OW
			+ "Children/Seniors RT: $%s\n" %self.CS_RT
			+ "Children/Seniors Tickets: %s\n" % self.CS_tickets
			) 


class Route_Container():
	""" Holds all of the Routes and contains useful search functions. """

	Routes = {}

	def addRoute(self, routeToAdd: Route):
		""" Adds a Route to the Routes dictionary. """
		self.Routes[routeToAdd.name] = routeToAdd

	def getAllRoutesStartingAt(self, startLocation: str):
		""" Returns a dictionary of all Routes starting at the given startLocation. """
		outputDictionary = {}
		for key, value in self.Routes.items():
			if value.start.upper() == startLocation.upper():
				outputDictionary[key] = value
		return outputDictionary

	def getRouteThatStartsAndEndsWith(self, start: str, end: str):
		""" Returns a Route that starts at and ends with the given strings. """
		route_name = start.upper() + " to " + end.upper()
		if route_name in self.Routes:
			return self.Routes[route_name]
		else:
			raise Exception("Route not found.")

	def getStartLocations(self):
		""" Returns a string array of all the start locations in the Routes dictionary. """
		startLocations = []
		for value in self.Routes.values():
			if value.start not in startLocations:
				startLocations.append(value.start)
		return startLocations

	def printAllRoutes(self):
		""" Prints all of the Routes in the Routes dictionary. """
		for key, value in self.Routes.items():
			print(key)

