import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.config import Config

from Route import Route
from Route_Container import Route_Container
from fileReader import All_Routes

Start_Route_Names = All_Routes.getStartLocations()
End_Route_Names = All_Routes.getEndLocations()

for x in range(0, 3):
	Start_Route_Names.append("x")

for x in range(0, 3):
	End_Route_Names.append("x")
print(Start_Route_Names)

fontSize_Labels = 14
fontSize_Buttons = 35

def keep_above_zero(number):
	""" Returns 0 if the number is below 0. Otherwise, returns the number. """
	if (number < 0):
		return 0
	else:
		return number

class MyGrid(GridLayout):
	
	Adults_RT = 0
	Adults_OW = 0
	CS_RT = 0
	CS_OW = 0
	current_start = ""
	current_end = ""

	def preventBelowZero(self, numberToProtect, integer):
		if(numberToProtect + integer < 0):
			return 0

	def Create_DropDown_Menu(self, main_button_text, data, handler):
		""" Creates the FROM dropdown menu using the given array."""
		dropDown = DropDown()
		fontSize = 15
		for item in data:
			button = Button(text=item, size_hint_y=None, font_size = fontSize, height = 45)
			button.bind(on_release=lambda button: dropDown.select(button.text))
			button.bind(on_release=handler)
			dropDown.add_widget(button)
		mainButton = Button(text=main_button_text, width=100, font_size = fontSize)
		mainButton.bind(on_release = dropDown.open)
		dropDown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))
		return mainButton

	def Create_Adults_RT_Grid(self, mainGrid):
		mainGrid.add_widget(Label(text="Adults RT: ", font_size=fontSize_Labels)) # Add a text label

		self.Adults_RT_input = TextInput(text = "0", multiline = False, font_size=fontSize_Buttons) # Create a text input box
		self.Adults_RT_input.bind(on_text_validate=self.Adults_RT_Button_Inputs)
		self.Adults_RT_minus = Button(text="-", font_size=fontSize_Buttons) # Create a button
		self.Adults_RT_minus.bind(on_press=self.Adults_RT_Button_Inputs) # Bind the button
		self.Adults_RT_add = Button(text="+", font_size=fontSize_Buttons) # Create a button
		self.Adults_RT_add.bind(on_press=self.Adults_RT_Button_Inputs) # Bind the button

		mainGrid.add_widget(self.Adults_RT_minus) # Add the button to the grid
		mainGrid.add_widget(self.Adults_RT_input) # Add the text input box to the grid
		mainGrid.add_widget(self.Adults_RT_add)

	def Create_Adults_OW_Grid(self, mainGrid):
		mainGrid.add_widget(Label(text="Adults OW: ", font_size=fontSize_Labels)) # Add a text label

		self.Adults_OW_input = TextInput(text = "0", multiline = False, font_size=fontSize_Buttons) # Create a text input box
		self.Adults_OW_minus = Button(text="-", font_size=fontSize_Buttons) # Create a button
		self.Adults_OW_minus.bind(on_press=self.Adults_OW_Button_Inputs) # Bind the button
		self.Adults_OW_add = Button(text="+", font_size=fontSize_Buttons) # Create a button
		self.Adults_OW_add.bind(on_press=self.Adults_OW_Button_Inputs) # Bind the button

		mainGrid.add_widget(self.Adults_OW_minus) # Add the button to the grid
		mainGrid.add_widget(self.Adults_OW_input) # Add the text input box to the grid
		mainGrid.add_widget(self.Adults_OW_add)

	def Create_CS_RT_Grid(self, mainGrid):
		mainGrid.add_widget(Label(text="C / S RT: ", font_size=fontSize_Labels))

		self.CS_RT_input = TextInput(text = "0", multiline = False, font_size = fontSize_Buttons)
		self.CS_RT_minus = Button(text="-", font_size=fontSize_Buttons)
		self.CS_RT_minus.bind(on_press=self.CS_RT_Inputs)
		self.CS_RT_add = Button(text="+", font_size=fontSize_Buttons)
		self.CS_RT_add.bind(on_press=self.CS_RT_Inputs)

		mainGrid.add_widget(self.CS_RT_minus)
		mainGrid.add_widget(self.CS_RT_input)
		mainGrid.add_widget(self.CS_RT_add)

	def Create_CS_OW_Grid(self, mainGrid):
		mainGrid.add_widget(Label(text="C / S OW: ", font_size=fontSize_Labels))

		self.CS_OW_input = TextInput(text = "0", multiline = False, font_size = fontSize_Buttons)
		self.CS_OW_minus = Button(text="-", font_size=fontSize_Buttons)
		self.CS_OW_minus.bind(on_press=self.CS_OW_Inputs)
		self.CS_OW_add = Button(text="+", font_size=fontSize_Buttons)
		self.CS_OW_add.bind(on_press=self.CS_OW_Inputs)

		mainGrid.add_widget(self.CS_OW_minus)
		mainGrid.add_widget(self.CS_OW_input)
		mainGrid.add_widget(self.CS_OW_add)

	def Create_Results_Grid(self, mainGrid):

		mainGrid.add_widget(Label(text="Total: "))

		self.totalPrice = Label(text="$0.00", font_size=45)

		mainGrid.add_widget(self.totalPrice)
		
		mainGrid.add_widget(Label(text="Tickets: "))

		self.totalTickets = Label(text="0", font_size=45)

		mainGrid.add_widget(self.totalTickets)

	def Create_Reset_Button(self, mainGrid):
		reset_button_text = "Reset"
		self.Reset_Button = Button(text=reset_button_text)
		self.Reset_Button.bind(on_press=self.Reset_Button_Input)
		mainGrid.add_widget(self.Reset_Button)


	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)

		self.cols = 1 # Set the number of columns.

		self.ticketCounter = GridLayout(cols=4)

		""" Top Bar """
		self.ticketCounter.add_widget(Label(text="From: ", height=44))
		self.From_Menu = self.Create_DropDown_Menu("Start", Start_Route_Names, self.Start_DropDown_Menu_Inputs)
		self.ticketCounter.add_widget(self.From_Menu)
		self.ticketCounter.add_widget(Label(text="To: ", height=44))
		self.To_Menu = self.Create_DropDown_Menu("End", End_Route_Names, self.End_DropDown_Menu_Inputs)
		self.ticketCounter.add_widget(self.To_Menu)

		""" Calculator parts """
		self.Create_Adults_OW_Grid(self.ticketCounter)
		self.Create_Adults_RT_Grid(self.ticketCounter)
		self.Create_CS_RT_Grid(self.ticketCounter)
		self.Create_CS_OW_Grid(self.ticketCounter)
		self.Create_Results_Grid(self.ticketCounter)

		""" Reset Button """
		self.Create_Reset_Button(self.ticketCounter)

		self.add_widget(self.ticketCounter)

	def print_stats(self):
		print("Adults RT", self.Adults_RT)
		print("Adults OW", self.Adults_OW)
		print("Children Seniors RT", self.Children_Seniors_RT)
		print("Children Seniors OW", self.Children_Seniors_OW)

	def update_stats(self):
		current_route = All_Routes.getRouteThatStartsAndEndsWith(self.current_start, self.current_end)
		total_price = current_route.getTotalPrice(self.Adults_OW, self.Adults_RT, self.CS_OW, self.CS_RT)
		total_tickets = str(current_route.getTotalTickets(self.Adults_OW, self.Adults_RT, self.CS_OW, self.CS_RT))
		formatted_price = str("{:.2f}".format(total_price))
		self.totalPrice.text = "$" + formatted_price
		self.totalTickets.text = total_tickets

	def Adults_RT_Button_Inputs(self, instance):
		if(instance == self.Adults_RT_minus):
			self.Adults_RT_input.text = str(keep_above_zero(int(self.Adults_RT_input.text) - 1))

		elif(instance == self.Adults_RT_add):
			self.Adults_RT_input.text = str(keep_above_zero(int(self.Adults_RT_input.text) + 1))

		self.Adults_RT = int(self.Adults_RT_input.text)
		self.Adults_RT_input.text = str(self.Adults_RT)
		self.Null_Route_Popup()
		self.update_stats()

	def Adults_OW_Button_Inputs(self, instance):
		if(instance == self.Adults_OW_minus):
			self.Adults_OW_input.text = str(keep_above_zero(int(self.Adults_OW_input.text) - 1))

		elif(instance == self.Adults_OW_add):
			self.Adults_OW_input.text = str(keep_above_zero(int(self.Adults_OW_input.text) + 1))

		self.Adults_OW = int(self.Adults_OW_input.text)
		self.Adults_OW_input.text = str(self.Adults_OW)
		self.Null_Route_Popup()
		self.update_stats()

	def CS_RT_Inputs(self, instance):
		if(instance == self.CS_RT_minus):
			self.CS_RT_input.text = str(keep_above_zero(int(self.CS_RT_input.text) - 1))

		elif(instance == self.CS_RT_add):
			self.CS_RT_input.text = str(keep_above_zero(int(self.CS_RT_input.text) + 1))

		self.CS_RT = int(self.CS_RT_input.text)
		self.CS_RT_input.text = str(self.CS_RT)
		self.Null_Route_Popup()
		self.update_stats()

	def CS_OW_Inputs(self, instance):
		if(instance == self.CS_OW_minus):
			self.CS_OW_input.text = str(keep_above_zero(int(self.CS_OW_input.text) - 1))

		elif(instance == self.CS_OW_add):
			self.CS_OW_input.text = str(keep_above_zero(int(self.CS_OW_input.text) + 1))

		self.CS_OW = int(self.CS_OW_input.text)
		self.CS_OW_input.text = str(self.CS_OW)
		self.Null_Route_Popup()
		self.update_stats()

	def Null_Route_Popup(self):
		if(All_Routes.getRouteThatStartsAndEndsWith(self.current_start, self.current_end).start == "NULL"):
			popup = Popup(title="Route does not exist.", content=Label(text="Please double-check the START and END locations.", font_size=fontSize_Labels), size_hint_y=None, size=(100, 100))
			popup.auto_dismiss = True
			popup.open()

	def Start_DropDown_Menu_Inputs(self, instance):
		self.current_start = instance.text
		print(All_Routes.getAllRoutesEndingAt(instance.text))
		self.To_Menu = self.Create_DropDown_Menu("End", All_Routes.getAllRoutesEndingAt(instance.text), self.End_DropDown_Menu_Inputs)
		self.Null_Route_Popup()
		self.update_stats()

	def End_DropDown_Menu_Inputs(self, instance):
		self.current_end = instance.text
		self.Null_Route_Popup()
		self.update_stats()

	def Reset_Button_Input(self, instance):
		print("Reset")
		self.Adults_OW_input.text = "0"
		self.Adults_RT_input.text = "0"
		self.CS_OW_input.text = "0"
		self.CS_RT_input.text = "0"
		self.Adults_RT = 0
		self.Adults_OW = 0
		self.CS_RT = 0
		self.CS_OW = 0
		self.update_stats()



class MyApp(App):
	def build(self):
		return MyGrid()


if __name__ == "__main__" :
	MyApp().run()