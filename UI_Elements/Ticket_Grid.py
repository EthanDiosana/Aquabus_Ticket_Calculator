"""def Create_Ticket_Grid(self, label_text, label_font_size, button_font_size, text_input_font_size, input_handler):
		Creates a grid for adding and removing tickets.

		# Create the grid to be returned.
		ticketGrid = BoxLayout(orientation="horizontal")
	
		# Create the label, buttons, and text input box.
		label = Label(text=label_text, font_size=label_font_size, size_hint=(2, 0))
		minus_button = Button(text="-", font_size=button_font_size)
		plus_button = Button(text="+", font_size=button_font_size)
		text_input = TextInput(text="0", multiline=False, font_size=text_input_font_size, input_filter='int')

		# Bind the buttons to the input handler.
		minus_button.bind(on_press=input_handler)
		plus_button.bind(on_press=input_handler)
		text_input.bind(on_text_validate=input_handler)

		# Add all of the widgets to the grid.
		ticketGrid.add_widget(label)
		ticketGrid.add_widget(minus_button)
		ticketGrid.add_widget(text_input)
		ticketGrid.add_widget(plus_button)

		return ticketGrid"""

class Ticket_Grid(BoxLayout):

	def __init__(self):
		super(Ticket_Grid, self).__init__()

		self.orientation = horizontal
		
		# The label, text input, and buttons.
		self.label = Label(text=label_text, font_size=label_font_size, size_hint=(2,0))
		self.minus_button = Button(text="-", font_size=button_font_size)
		self.plus_button = Button(text="+", font_size=button_font_size)
		self.text_input = TextInput(text="0", multiline=False, font_size=text_input_font_size, input_filter='int')

		self.minus_button.bind(on_press=minus_handler)
		self.plus_button.bind(on_press=plus_hander)
		self.text_input.bind(on_text_validate=text_input_handler)

	def minus_handler(self, instance):
		pass

	def plus_handler(self, instance):
		pass

	def text_input_handler(self, instance):
		pass
