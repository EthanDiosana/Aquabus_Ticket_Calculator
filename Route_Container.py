from Classes.Route import Route

class Route_Container():
	""" Holds all of the Routes and contains useful search functions. """

	Routes = {}

	def addRoute(self, routeToAdd: Route):
		""" Adds a Route to the Routes dictionary. """
		self.Routes[routeToAdd.name] = routeToAdd

	def routeIsInContainer(self, start, end):
		"""Returns True if the given route is in Routes{}. Returns False otherwise."""
		if(self.getRouteThatStartsAndEndsWith(start, end).start == "NULL"):
			return False
		else:
			return True

	def getAllRoutesStartingAt(self, startLocation: str):
		""" Returns a dictionary of all Routes starting at the given startLocation. """
		outputDictionary = {}
		for key, value in self.Routes.items():
			if value.start.upper() == startLocation.upper():
				outputDictionary[key] = value
		return outputDictionary

	def getAllRoutesEndingAt(self, endLocation: str):
		""" Returns a dictionary of all Routes ending at the given startLocation. """
		outputDictionary = {}
		for key, value in self.Routes.items():
			if value.start.upper() == endLocation.upper():
				outputDictionary[key] = value
		return outputDictionary

	def getRouteThatStartsAndEndsWith(self, start: str, end: str):
		""" Returns a Route that starts at and ends with the given strings. """
		route_name = start.upper() + " to " + end.upper()
		if route_name in self.Routes:
			return self.Routes[route_name]
		#else:
			#raise Exception("Route not found.")
		else:
			return Route("NULL|NULL|0|0|0|0|0|0")

	def getStartLocations(self):
		""" Returns a string array of all the start locations in the Routes dictionary. """
		startLocations = []
		for value in self.Routes.values():
			if value.start not in startLocations:
				startLocations.append(value.start)
		return startLocations

	def getEndLocations(self):
		""" Returns a string array of all the end locations in the Routes dictionary. """
		endLocations = []
		for value in self.Routes.values():
			if value.start not in endLocations:
				endLocations.append(value.start)
		return endLocations

	def printAllRoutes(self):
		""" Prints all of the Routes in the Routes dictionary. """
		for key, value in self.Routes.items():
			print(key)

