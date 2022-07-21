"""
	def Create_DropDown_Menu(self, main_button_text, button_font_size, data, handler):
		Creates the FROM dropdown menu using the given array.
		dropDown = DropDown()
		for item in data:
			button = Button(text=item, size_hint_y=None, height=80)
			button.font_size = button_font_size
			button.bind(on_release=lambda button: dropDown.select(button.text))
			button.bind(on_release=handler)
			dropDown.add_widget(button)
			if(button.text=="x"):
				button.opacity = 0
				button.disabled = True
		mainButton = Button(text=main_button_text, font_size = button_font_size)
		mainButton.bind(on_release = dropDown.open)
		dropDown.bind(on_select=lambda instance, x: setattr(mainButton, 'text', x))
		return mainButton
		"""

class Route_Dropdown_Menu(DropDown()):
	"A dropdown menu that contains the routes given in the array."

	def __init__(self, item_array):
		super(Route_Dropdown_Menu, self).__init__()

		self.main_button = Button(text=main_button_text, font_size=button_font_size)