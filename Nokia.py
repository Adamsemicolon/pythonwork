menu = """
       				MENU
           1-> Phone Book
           2-> Messages
           3-> Chat
           4-> Call Register
           5-> Tones
           6-> Settings
           7-> Call Divert
           8-> Games
           9-> Calculator
           10-> Reminders
           11-> Clock
           12-> Profiles
           13-> Sim Services
"""
print(menu)
userInput = int(input("Input a number to select "))
match userInput:
	case 1:
		phoneBook = """
			PHONEBOOK
		1-> Search
		2-> Service Nos
		3-> Add name
		4-> Erase
		5-> Edit
		6-> Assign tone
		7-> Send b'card
		8-> Options
		9-> Speed dials
		10-> Voice tags
		"""
		print(phoneBook)
		userInput = int(input("Input a number to select "))
		match userInput:
			case 1:print("Search")
			case 2:print("Service Nos")
			case 3:print("Add name")
			case 4:print("Erase")
			case 5:print("Edit")
			case 6:print("Assign tone")
			case 7:print("Send b'card")
			case 8:
				Options = """
				1-> Type of view
				2-> Memory status
				"""
				print(Options)
				userInput = int(input("Input a number to select"))
				match userInput:
					case 1:print("Type of view")
					case 2:print("Memory Status")
					case _:print("")
				
			case 9:print("Speed dials")
			case 10:print("Voice tags")
			case _:print("")
		
	case 2:
		Messages = """
				MESSAGES
		1-> Write messages
		2-> Inbox
		3-> Outbox
		4-> Picture messages
		5-> Templates
		6-> Smileys
		7-> Message settings
		8-> Info services
		9-> Voice Mailbox number
		10-> Service command editor
		"""
		print(Messages)
		userInput = int(input("Input number to select "))
		match userInput:
			case 1:print("Write messages")
			case 2:print("Inbox")
			case 3:print("Outbox")
			case 4:print("Picture messages")
			case 5:print("Templates")
			case 6:print("Smileys")
			case 7:
					Message_settings = """
					1-> Set1
					2-> Common
					"""
					print(Message_settings)
					userInput = int(input("Enter a number to select "))
					match userInput:
						case 1:
								Set1 = """
								1-> Message centre number
								2-> Messages sent as
								3-> Message validity
								"""
								print(Set1)
								userInput = int(input("Enter number to select"))
								match userInput:
									case 1:print("Message centre number")
									case 2:print("Messages sent as")
									case 3:print("Message validity")
									case _:print("")
						case 2:
									Common = """
									1->Delivery Reports
									2-> Reply same centre
									3-> Character support
									"""
									print(Common)
									userInput = int(input("Enter number to select")) 
									match userInput:
										case 1:print("Delivery reports")
										case 2:print("Reply same centre")
										case 3:print("Character support")
										case _:print("")
						case _:print("")
			case 8:print("Info services")
			case 9:print("Voice mailbox number")
			case 10:print("Service command editor")
	case 3:print("Chat")
	case 4:
				CallRegister = """
				1-> Missed calls
				2-> Received calls
				3-> Dialled numbers
				4-> Erase recent calls
				5-> Show call duration
				6-> Show call costs
				7-> Call cost settings
				8-> Prepaid credit
				"""
				print(CallRegister)
				userInput = int(input("Enter a number to select "))
				match userInput:
					case 1:print("Missed calls")
					case 2:print("Received calls")
					case 3:print("Dialled numbers")
					case 4:print("Erase recent calls")
					case 5:
						Show_call_duration = """
						1-> Last call duration 
						2-> All call's duration
						3-> Received call's duration
						4-> Dialled call's duration
						5-> Clear timers
						"""
						print(Show_call_duration)
						userInput = int(input("Input number to select "))
						match userInput:
							case 1:print("Last call duration")
							case 2:print("All call's duration")
							case 3:print("Received call's duration")
							case 4:print("Dialled call's duration")
							case 5:print("Clear timers")
							case _:print("")

					case 6:
								Show_call_cost = """
								1-> Last call cost
								2-> All call's cost
								3-> Clear counters
								"""
								print(Show_call_cost)
								userInput = int(input("Input number to select "))
								match userInput:
									case 1:print("Last call cost")
									case 2:print("All call's cost")
									case 3:print("Clear counters")
									case _:print("")
					case 7:
									Call_cost_settings = """
									1-> Call cost limit
									2-> Show costs in
									"""
									print(Call_cost_settings)
									userInput = int(input("Input number to select"))
									match userInput:
										case 1:print("Call cost limit")
										case 2:print("Show costs in")
										case _:print("")
					case 8:print("Prepaid credit")

	case 5:
			Tones = """
			1-> Ringing tone
			2-> Ringing volume
			3-> Incoming call alert
			4-> Composer
			5-> Message alert tone
			6-> Keypad tones
			7-> Warning and games tone
			8-> Vibrating alert
			9-> Screen saver
			"""
			print(Tones)
			userInput = int(input("Enter number to select"))
			match userInput:
				case 1:print("Ringing tone")
				case 2:print("Ringing volume")
				case 3:print("Incoming call alert")
				case 4:print("Composer")
				case 5:print("Message alert tone")
				case 6:print("Keypad tones")
				case 7:print("Warning and games tone")
				case 8:print("Vibrating alert")
				case 9:("Screen saver")
				case _:("")
	case 6:
					Settings = """
					1-> Call settings
					2-> Phone settings
					3-> Security settings
					4-> Restore factory settings
					"""
					print(Settings)
					userInput = int(input("Input a number to select "))
					match userInput:
						case 1:
							Call_settings = """
							1-> Automatic Redial
							2-> Speed dialling
							3-> Call waiting options
							4-> Own number Sending
							5-> Phone line in use
							6-> Automatic answer
							"""
							print(Call_settings)
							userInput = int(input("Input a number to select "))
							match userInput:
								case 1:print("Automatic Redial")
								case 2:print("Speed dialling")
								case 3:print("Call waiting options")
								case 4:print("Own number Sending")
								case 5:print("Phone line in use")
								case 6:print("Automatic answer")
						case 2:
								Phone_settings = """
								1-> Language
								2-> Cell info display
								3-> Welcome note
								4-> Network selection
								5-> Lights
								6-> Confirm SIM service actions
								"""
								print(Phone_settings)
								userInput = int(input("Input a number to select "))
								match userInput:
									case 1:print("Language")
									case 2:print("Cell info display")
									case 3:print("Welcome note")
									case 4:print("Network selection")
									case 5:print("Lights")
									case 6:print("Confirm SIM service actions")
						case 3:
									Security_settings = """
									1->Pin code request
									2-> Call barring service
									3-> Fixed dialling
									4-> Closed user group
									5-> Phone security
									6-> Change access codes
									"""
									print(Security_settings)
									userInput = int(input("Input number to select "))
									match userInput:
										case 1:print("Pin code request")
										case 2:print("Call barring service")
										case 3:print("Fixed dialling")
										case 4:print("Closed user group")
										case 5:print("Phone security")
										case 6:print("Change access codes")
						case 4:print("Restore factory settings")
	case 7:print("Call divert")
	case 8:print("Games")
	case 9:print("Calculator")
	case 10:print("Reminders")
	case 11:
					Clock = """
					1-> Alarm clock
					2-> Clock settings
					3-> Date settings
					4-> Stopwatch
					5-> Countdown timers
					6-> Auto-update of date and time
					"""
					print(Clock)
					userInput = int(input("Enter a number to select"))
					match userInput:
						case 1:print("Alarm clock")
						case 2:print("Clock settings")
						case 3:print("Date settings")
						case 4:print("Stopwatch")
						case 5:print("Countdown timers")
						case 6:print("Auto-update of date and time")
	case 12:print("Profiles")
	case 13:print("Sim services")
	case _:print("")











