
from kivy.uix.screenmanager import ScreenManager, Screen

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
fontSize_Labels = 40

# The size for the buttons on the dropdown menu.
fontSize_Buttons = 40

# The size for the input buttons.
fontSize_Dropdown = 30

# The size for the top tabs.
fontSize_Tabs = 20

Passes = {
		"Adults DP": 0,
		"Adults MP": 0,
		"CS DP" : 0,
		"CS MP" : 0
	}

Passes_Costs = {
		"Adults DP": 0.00,
		"Adults MP": 0.00,
		"CS DP" : 0.00,
		"CS MP" : 0.00
	}

Tickets = {
		"Adults OW" : 0,
		"Adults RT" : 0,
		"CS OW" : 0,
		"CS RT" : 0,
	}

class MyGrid(GridLayout):

	current_start = ""
	current_end = ""
	current_tab = "Tickets"

	def Create_Switch_Tabs(self, tab_1_text, tab_2_text, tab_font_size, handler):
		newGrid = GridLayout(rows=1, cols=2)
		newGrid.size_hint = (1, 0.5)

		tab_1 = Button(text=tab_1_text, font_size=tab_font_size)
		tab_2 = Button(text=tab_2_text, font_size=tab_font_size)

		tab_1.bind(on_press=handler)
		tab_2.bind(on_press=handler)
		
		tab_1.disabled = True

		newGrid.add_widget(tab_1)
		newGrid.add_widget(tab_2)

		return newGrid

	def Create_Calculator_Grid(self):
		newGrid = GridLayout(cols=1)
		newGrid.size_hint = (1, 7)
		return newGrid


	def Create_DropDown_Menu(self, main_button_text, button_font_size, data, handler):
		""" Creates the FROM dropdown menu using the given array."""
		dropDown = DropDown()
		for item in data:
			button = Button(text=item, size_hint_y=None, height=80)
			button.font_size = button_font_size
			button.bind(on_release=lambda button: dropDown.select(button.text))
			button.bind(on_release=handler)
			dropDown.add_widget(button)
		mainButton = Button(text=main_button_text, font_size = button_font_size)
		mainButton.bind(on_release = dropDown.open)
		dropDown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))
		return mainButton

	def Create_Start_End_Grid(self, dropdown_font_size, start_data, end_data, start_handler, end_handler):
		"""Creates a grid for selecting the TO and FROM of the route."""

		# Create the grid to be returned.
		newGrid = GridLayout(rows=1, cols=4)

		# Create all of the labels and buttons.
		start_menu = self.Create_DropDown_Menu("Start", dropdown_font_size, start_data, start_handler)
		end_menu = self.Create_DropDown_Menu("End", dropdown_font_size, end_data, end_handler)

		# Add the widgets to the grid.
		newGrid.add_widget(start_menu)
		newGrid.add_widget(end_menu)

		return newGrid

	def Create_Ticket_Grid(self, label_text, label_font_size, button_font_size, text_input_font_size, input_handler):
		"""Creates a grid for adding and removing tickets."""

		# Create the grid to be returned.
		ticketGrid = GridLayout(rows=1, cols=4)
	
		# Create the label, buttons, and text input box.
		label = Label(text=label_text, font_size=label_font_size, size_hint=(2, 0))
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

		self.Calculator_Grid = self.Create_Calculator_Grid()
		self.Passes_Grid = self.Create_Calculator_Grid()
		self.hide_grid(self.Passes_Grid)

		Tabs_Grid = self.Create_Switch_Tabs("Tickets", "Passes", fontSize_Tabs, self.Tabs_Handler)
		Start_End_Grid = self.Create_Start_End_Grid( fontSize_Dropdown, Start_Route_Names, End_Route_Names, self.Start_DropDown_Menu_Inputs, self.End_DropDown_Menu_Inputs)
		Results_Grid = self.Create_Results_Grid()

		Reset_Button = self.Create_Button("Reset", fontSize_Buttons, self.Reset_Button_Input)

		self.notification_zone = Label(size_hint=(.5,.5), font_size=20, color="red")
		self.notification_zone_2 = Label(size_hint=(.5,.5), font_size=20, color="red", text="Coming soon!")

		self.ticketCounter.add_widget(Tabs_Grid)
		self.Calculator_Grid.add_widget(self.notification_zone)
		self.Calculator_Grid.add_widget(Start_End_Grid)
		self.Calculator_Grid.add_widget(Label(size_hint=(.5, .2)))

		self.Passes_Grid.add_widget(self.notification_zone_2)


		"""Create and add the ticket grids to the main grid."""
		for ticket_name in Tickets.keys():
			new_grid = self.Create_Ticket_Grid(ticket_name, fontSize_Labels, fontSize_Buttons, fontSize_Buttons, self.change_ticket_number)
			self.Calculator_Grid.add_widget(new_grid)

		for ticket_name in Passes.keys():
			new_grid = self.Create_Ticket_Grid(ticket_name, fontSize_Labels, fontSize_Buttons, fontSize_Buttons, self.change_ticket_number)
			self.Passes_Grid.add_widget(new_grid)


		self.Calculator_Grid.add_widget(Results_Grid)
		self.Calculator_Grid.add_widget(Reset_Button)

		self.ticketCounter.add_widget(self.Passes_Grid)
		self.ticketCounter.add_widget(self.Calculator_Grid)
		self.ticketCounter.add_widget(Label(text="danielrenendez@gmail.com", color="grey", font_size=15, size_hint=(0,0.1)))


		self.add_widget(self.ticketCounter)

	def print_stats(self):
		print("Adults RT", self.Adults_RT)
		print("Adults OW", self.Adults_OW)
		print("Children Seniors RT", self.Children_Seniors_RT)
		print("Children Seniors OW", self.Children_Seniors_OW)

	def update_stats(self):
		if(self.current_tab=="Tickets"):
			current_route = All_Routes.getRouteThatStartsAndEndsWith(self.current_start, self.current_end)
			total_price = current_route.getTotalPrice(Tickets["Adults OW"], Tickets["Adults RT"], Tickets["CS OW"], Tickets["CS RT"])
			total_tickets = str(current_route.getTotalTickets(Tickets["Adults OW"], Tickets["Adults RT"], Tickets["CS OW"], Tickets["CS RT"]))
			formatted_price = str("{:.2f}".format(total_price))
			self.totalPrice.text = "$" + formatted_price
			self.totalTickets.text = total_tickets
			self.notify_null_route()
		elif(self.current_tab=="Passes"):
			pass


	def change_ticket_number(self, instance):
		grid = instance.parent
		label = instance.parent.children[3]
		minus_button = instance.parent.children[2]
		text_input = instance.parent.children[1]
		plus_button = instance.parent.children[0]

		tag = label.text # This is used to identify the ticket.
		
		if(self.current_tab=="Tickets"):
			# Check which button was pressed.
			if(instance==plus_button):
				Tickets[tag] += 1
			elif(instance==minus_button):
				Tickets[label.text] -= 1
			elif(instance==text_input):
				if(instance.text.isnumeric()):
					print(instance.text + " is numeric.")
					Tickets[label.text] = int(instance.text)
				else:
					print(instance.text + " is not numeric.")
					instance.text = str(0)

			# Prevent the number of tickets from going below zero.
			Tickets[tag] = self.prevent_below_zero(Tickets[tag])
			text_input.text = str(Tickets[tag])
			print(tag + ": " + str(Tickets[tag]))
		elif(self.current_tab=="Passes"):
			# Check which button was pressed.
			if(instance==plus_button):
				Passes[tag] += 1
			elif(instance==minus_button):
				Passes[label.text] -= 1
			elif(instance==text_input):
				if(instance.text.isnumeric()):
					print(instance.text + " is numeric.")
					Passes[label.text] = int(instance.text)
				else:
					print(instance.text + " is not numeric.")
					instance.text = str(0)
			# Prevent the number of tickets from going below zero.
			Passes[tag] = self.prevent_below_zero(Passes[tag])
			text_input.text = str(Passes[tag])
			print(tag + ": " + str(Passes[tag]))

		self.update_stats()
	
	def prevent_below_zero(self, number):
		if(number<0):
			return 0
		else:
			return number

	def notify_null_route(self):
		if(All_Routes.getRouteThatStartsAndEndsWith(self.current_start, self.current_end).start == "NULL"):
			self.notification_zone.text = "Route does not exist."
			self.notification_zone.color = "red"
		else:
			self.notification_zone.text = self.current_start + " to " + self.current_end
			self.notification_zone.color = "green"

	def Start_DropDown_Menu_Inputs(self, instance):
		self.current_start = instance.text
		self.update_stats()

	def End_DropDown_Menu_Inputs(self, instance):
		self.current_end = instance.text
		self.update_stats()

	def Reset_Button_Input(self, instance):
		for ticket in Tickets:
			Tickets[ticket] = 0

		for x in range(len(Tickets)+1, 0, -1):
			print(self.children[0].children[1].children[x].children[1].text)
			print("AAAAAAAAAAAAAAAAAAAAAAA")
			self.children[0].children[1].children[x].children[1].text = str(0)
		self.update_stats()

	def Tabs_Handler(self, instance):
		if(instance.text=="Tickets"):
			instance.disabled = True
			instance.parent.children[0].disabled = False
			self.current_tab="Tickets"
			self.hide_grid(self.Passes_Grid)
			self.show_grid(self.Calculator_Grid)
		elif(instance.text=="Passes"):
			instance.disabled = True
			instance.parent.children[1].disabled = False
			self.current_tab="Passes"
			self.hide_grid(self.Calculator_Grid)
			self.show_grid(self.Passes_Grid)

	def hide_grid(self, grid):
		grid.size_hint=(0,0)
		grid.opacity = 0
		grid.disabled = True

	def show_grid(self, grid):
		grid.opacity = 1
		grid.disabled = False
		grid.size_hint=(1,7)

class MyApp(App):
	def build(self):
		self.icon = "Logo.png"
		return MyGrid()


if __name__ == "__main__" :
	MyApp().run()