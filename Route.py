class Route():
	""" Contains all of the information of a Route."""

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
		 "CS_OW": self.CS_OW,
		 "CS_RT": self.CS_RT,
		 "CS_Tickets": self.CS_tickets
		 }
		return asDictionary

	def returnRouteAsParsableString(self):
		""" Returns the Route as a parsable string. """
		output = ""
		output += self.name + "|"
		output += self.start + "|"
		output += self.end + "|"
		output += self.adults_OW + "|"
		output += self.adults_RT + "|"
		output += self.adults_tickets + "|"
		output += self.CS_OW + "|"
		output += self.CS_RT + "|"
		output += self.CS_tickets + "\n"
		return output;

	def getTotalPrice(self, number_adults_OW: int, number_adults_RT: int, number_CS_OW: int, number_CS_RT: int):
		""" Returns a float calculated from the number of tickets and their prices. """
		final_price = float(0.00)

		for x in range(0, number_adults_OW):
			final_price += float(self.adults_OW)

		for x in range(0, number_adults_RT):
			final_price += float(self.adults_RT)

		for x in range(0, number_CS_OW):
			final_price += float(self.CS_OW)

		for x in range(0, number_CS_RT):
			final_price += float(self.CS_RT)

		return final_price

	def getTotalTickets(self, number_adults_OW: int, number_adults_RT: int, number_CS_OW: int, number_CS_RT: int):
		""" Returns an int calculated from the number of tickets"""
		final_tickets = 0

		for x in range(0, number_adults_OW):
			final_tickets += int(self.adults_tickets)

		for x in range(0, number_adults_RT):
			final_tickets += int(self.adults_tickets) * 2

		for x in range(0, number_CS_OW):
			final_tickets += int(self.CS_tickets)

		for x in range(0, number_CS_RT):
			final_tickets += int(self.CS_tickets) * 2
		return final_tickets

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
