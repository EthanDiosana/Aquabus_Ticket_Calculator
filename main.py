

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

from fileReader import All_Routes

Start_Route_Names = All_Routes.getStartLocations()
End_Route_Names = All_Routes.getEndLocations()

for x in range(0, 3):
	Start_Route_Names.append("x")

for x in range(0, 3):
	End_Route_Names.append("x")


# The size for the labels.
fontSize_Labels = 20

# The size for the buttons on the dropdown menu.
fontSize_Buttons = 40

# The size for the input buttons.
fontSize_Dropdown = 30

class MyGrid(GridLayout):

	current_start = ""
	current_end = ""

	Special_Costs = {
		"Adults DP": 1,
		"Adults MP": 1,
		"CS DP": 1,
		"CS MP": 1
	}

	Tickets = {
		"Adults RT" : 0,
		"Adults OW" : 0,
		"CS RT" : 0,
		"CS OW" : 0,
		"Adults DP": 0,
		"Adults MP": 0,
		"CS DP": 0,
		"CS MP": 0,
	}

	def Create_DropDown_Menu(self, main_button_text, button_font_size, data, handler):
		""" Creates the FROM dropdown menu using the given array."""
		dropDown = DropDown()
		for item in data:
			button = Button(text=item, size_hint_y=None, height = 80)
			button.font_size = button_font_size
			button.bind(on_release=lambda button: dropDown.select(button.text))
			button.bind(on_release=handler)
			dropDown.add_widget(button)
		mainButton = Button(text=main_button_text, width=100, font_size = button_font_size)
		mainButton.bind(on_release = dropDown.open)
		dropDown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))
		return mainButton

	def Create_Start_End_Grid(self, label_font_size, dropdown_font_size, start_data, end_data, start_handler, end_handler):
		"""Creates a grid for selecting the TO and FROM of the route."""

		# Create the grid to be returned.
		newGrid = GridLayout(rows=1, cols=4)

		# Create all of the labels and buttons.
		start_label = Label(text="Start: ", font_size=label_font_size)
		end_label = Label(text="End: ", font_size=label_font_size)
		start_menu = self.Create_DropDown_Menu("Start", dropdown_font_size, start_data, start_handler)
		end_menu = self.Create_DropDown_Menu("End", dropdown_font_size, end_data, end_handler)

		# Add the widgets to the grid.
		newGrid.add_widget(start_label)
		newGrid.add_widget(start_menu)
		newGrid.add_widget(end_label)
		newGrid.add_widget(end_menu)

		return newGrid

	def Create_Ticket_Grid(self, label_text, label_font_size, button_font_size, text_input_font_size, input_handler):
		"""Creates a grid for adding and removing tickets."""

		# Create the grid to be returned.
		ticketGrid = GridLayout(rows=1, cols=4)
	
		# Create the label, buttons, and text input box.
		label = Label(text=label_text, font_size=label_font_size)
		minus_button = Button(text="-", font_size=button_font_size)
		plus_button = Button(text="+", font_size=button_font_size)
		text_input = TextInput(text="0", multiline=False, font_size=text_input_font_size)

		# Bind the buttons to the input handler.
		minus_button.bind(on_press=input_handler)
		plus_button.bind(on_press=input_handler)
		text_input.bind(on_text_validate=input_handler)

		# Add all of the widgets to the grid.
		ticketGrid.add_widget(label)
		ticketGrid.add_widget(minus_button)
		ticketGrid.add_widget(text_input)
		ticketGrid.add_widget(plus_button)

		return ticketGrid
	
	def Create_Results_Grid(self):

		newGrid = GridLayout(rows=1, cols=4)

		newGrid.add_widget(Label(text="Total: ", font_size=fontSize_Labels))

		self.totalPrice = Label(text="$0.00", font_size=45)

		newGrid.add_widget(self.totalPrice)
		
		newGrid.add_widget(Label(text="Tickets: ", font_size=fontSize_Labels))

		self.totalTickets = Label(text="0", font_size=45)

		newGrid.add_widget(self.totalTickets)

		return newGrid

	def Create_Button(self, button_text, text_size, handler):
		newButton = Button(text=button_text, font_size=text_size)
		newButton.bind(on_press=handler)
		return newButton

	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)

		self.cols = 1 # Set the number of columns.

		self.ticketCounter = GridLayout(cols=1)
		
		Start_End_Grid = self.Create_Start_End_Grid(fontSize_Labels, fontSize_Dropdown, Start_Route_Names, End_Route_Names, self.Start_DropDown_Menu_Inputs, self.End_DropDown_Menu_Inputs)

		Results_Grid = self.Create_Results_Grid()

		Reset_Button = self.Create_Button("Reset", fontSize_Buttons, self.Reset_Button_Input)

		self.ticketCounter.add_widget(Start_End_Grid)

		"""Create and add the ticket grids to the main grid."""
		for ticket_name in self.Tickets.keys():
			new_grid = self.Create_Ticket_Grid(ticket_name, fontSize_Labels, fontSize_Buttons, fontSize_Buttons, self.change_ticket_number)
			self.ticketCounter.add_widget(new_grid)


		self.ticketCounter.add_widget(Results_Grid)
		self.ticketCounter.add_widget(Reset_Button)


		self.add_widget(self.ticketCounter)

	def print_stats(self):
		print("Adults RT", self.Adults_RT)
		print("Adults OW", self.Adults_OW)
		print("Children Seniors RT", self.Children_Seniors_RT)
		print("Children Seniors OW", self.Children_Seniors_OW)

	def update_stats(self):
		current_route = All_Routes.getRouteThatStartsAndEndsWith(self.current_start, self.current_end)
		total_price = current_route.getTotalPrice(self.Tickets["Adults OW"], self.Tickets["Adults RT"], self.Tickets["CS OW"], self.Tickets["CS RT"])

		for item in self.Special_Costs:
			print(item)
			total_price += self.Tickets[item] * self.Special_Costs[item]

		total_tickets = str(current_route.getTotalTickets(self.Tickets["Adults OW"], self.Tickets["Adults RT"], self.Tickets["CS OW"], self.Tickets["CS RT"]))
		formatted_price = str("{:.2f}".format(total_price))
		self.totalPrice.text = "$" + formatted_price
		self.totalTickets.text = total_tickets

		self.Null_Route_Popup()

	def change_ticket_number(self, instance):
		grid = instance.parent
		label = instance.parent.children[3]
		minus_button = instance.parent.children[2]
		text_input = instance.parent.children[1]
		plus_button = instance.parent.children[0]

		tag = label.text # This is used to identify the ticket.
	
		# Check which button was pressed.
		if(instance==plus_button):
			self.Tickets[tag] += 1
		elif(instance==minus_button):
			self.Tickets[label.text] -= 1
		elif(instance==text_input):
			if(instance.text.isnumeric()):
				print(instance.text + " is numeric.")
				self.Tickets[label.text] = int(instance.text)
			else:
				print(instance.text + " is not numeric.")
				instance.text = str(0)

		# Prevent the number of tickets from going below zero.
		self.Tickets[tag] = self.prevent_below_zero(self.Tickets[tag])

		text_input.text = str(self.Tickets[tag])

		print(tag + ": " + str(self.Tickets[tag]))

		self.update_stats()
	
	def prevent_below_zero(self, number):
		if(number<0):
			return 0
		else:
			return number

	def Null_Route_Popup(self):
		if(All_Routes.getRouteThatStartsAndEndsWith(self.current_start, self.current_end).start == "NULL"):
			popup = Popup(title="Route does not exist.", content=Label(text="Please double-check the START and END locations.", font_size=fontSize_Labels), size_hint_y=None, size=(100, 100))
			popup.auto_dismiss = True
			popup.open()

	def Start_DropDown_Menu_Inputs(self, instance):
		self.current_start = instance.text
		print(All_Routes.getAllRoutesEndingAt(instance.text))
		self.Null_Route_Popup()
		self.update_stats()

	def End_DropDown_Menu_Inputs(self, instance):
		self.current_end = instance.text
		self.Null_Route_Popup()
		self.update_stats()

	def Reset_Button_Input(self, instance):
		for ticket in self.Tickets:
			self.Tickets[ticket] = 0

		for x in range(len(self.Tickets)+1, 1, -1):
			print(self.children[0].children[x].children[3].text)
			self.children[0].children[x].children[1].text = str(0)
		self.update_stats()



class MyApp(App):
	def build(self):
		return MyGrid()


if __name__ == "__main__" :
	MyApp().run()