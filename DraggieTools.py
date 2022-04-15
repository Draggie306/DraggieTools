import random
from requests import get
from datetime import datetime
from os import path, startfile
from subprocess import Popen
from time import monotonic

build = 6
version = "0.1.1"
build_date = 1650037833

current_directory = path.dirname(path.realpath(__file__))
print(f"running CLI from {current_directory}")

print(f"SUSSY AMOGUS build {build}")

current_build_version = int((get("https://raw.githubusercontent.com/Draggie306/DraggieTools/main/build.txt")).content)

def download_update():
	r = get('https://github.com/Draggie306/DraggieTools/blob/main/dist/draggietools.exe?raw=true', stream=True)
	file_size = int(r.headers['content-length'])
	downloaded = 0
	start = last_print = monotonic()
	with open(f'{current_directory}\\DraggieTools-{current_build_version}.exe', 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			downloaded += f.write(chunk)
			now = monotonic()
			if now - last_print > 1:
				pct_done = round(downloaded / file_size * 100)
				speed = round(downloaded / (now - start) / 1024)
				print(f'Downloading. {pct_done}% done, avg speed {speed} kbps')
				last_print = now

def check_for_update():
	print("Checking for update...")
	if build < current_build_version:
		update_choice = input(f"Update available! You are on version {version} which is build {build}. The new version is build {current_build_version}\n\nType 1 to download update, else not\n\n>>> ")
		if update_choice == "1":
			print("Downloading update...")
			download_update()
			print("Update downloaded. Launching new version...")
			startfile(f'{current_directory}\\DraggieTools-{current_build_version}.exe')
		else:
			print("Skipping update.")
			return
	else:
		print(f"Your tools are up to date. Running version {version} - build {build} - built at {datetime.fromtimestamp(1650035010).strftime('%Y-%m-%d %H:%M:%S')}. The server says the newest build is {current_build_version}")


check_for_update()


def main():
	the_funny = ['Transfering sensitive files to The Criminal Network...', 'Your Computer Has Been FUCKED by the Trojan!', r'Your computer is hacked by IP: 5.172.193.104 like OS: LINUX UBUNTO and location: RUSSIAN FEDERATION', r'Problem opening the application running at executable "C:\PROGRAM FILES\RIOT CLIENT\RIOT VANGUARD\vgcsrv.exe". Would you like to scan this PC?']
	print(random.choice(the_funny))
	print("\n\n\nWhat would you like to do, mon frère?")
	x = input("")
	print(x)
	shrek_casino()

def shrek_casino():

	version_number = "v0.17.3"
	dev_mode = False

	import random, time, base64, os, sys, itertools
	from colorama import Fore, Style

	def slowprint(s, egg: int):
		for c in s + '\n':
			sys.stdout.flush()
			time.sleep(1. / egg)

	def slowprintlist(s: list, egg: int):
		for c in s:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(1. / egg)            

	def dev_tools():  #	Call this when you want details for debugging
		print(
			f"\n--------- DevTools subroutine --------- \nMoney (variable) = {money}"
		)
		with open(f"{credit_balance_file_directory}", "r") as f:
			money_64 = f.read()
			call_credit_balance_noPrint(credit_card)
			print(f"Money from file = {money}")
			print(f"Credit card number = {credit_card}")
			path, dirs, files = next(os.walk("cards/encrypted"))
			cards = len(files)
			print(f"Money accounts = {cards}")
			print(f"Base64 Encryption Data: Card Number is {credit_card_encrypted}, Card Balance is {money_64}")

			print(f"--------- End of DevTools --------- \n\n")

	def spinning_cursor():
		while True:
			for cursor in '|/-\\':
				yield cursor

	# Emoji List:
	# https://unicode.org/emoji/charts/full-emoji-list.html
	# To use an emoji, write its Unicode value, but replace the "U+" with "\U000"    

	print(Fore.BLUE + f"{version_number}")
			
	shrek = (
		" ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆\n ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿\n ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀\n ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀ \n ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉\n\n"
	)

	rock_eyebrow = (
		"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
	)

	talking_ben = ( "⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⢿⢯⣛⣺⣯⣿⣿⣿⣿⣿⣿⣿⢱⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⡿⣿⣿⢡⣿⣉⣿⡿⠿⠿⠿⡿⠿⠻⣿⡇⠸⣻⠾⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⡿⠛⠉⠁⠹⡰⣹⣟⣧⣤⡤⠄⠄⠠⣡⣼⣷⠄⢉⢻⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⠟⠄⠄⠄⡀⢸⣾⣿⣯⣯⡃⠄⠄⠄⠄⠐⠙⣿⣧⡀⠩⣧⠙⣿⣿⣿⣿⣿⣿\n⣿⠄⠄⠄⠈⠈⣾⣿⣿⣿⣿⣆⡀⠄⠄⠄⠄⠄⣸⣿⣿⣿⣧⠄⣼⣿⣿⣿⣿⣿\n⣿⠇⠄⠄⠄⠄⠙⠛⠛⠿⠿⢿⣿⣶⣀⣶⣾⣿⣿⣿⣿⢾⣷⣇⣤⣿⣿⣿⣿⣿\n⣿⣻⠄⠄⠄⠄⠄⠄⠄⠄⠠⠤⣤⣤⣌⠉⠉⠉⠁⢈⠁⠤⠛⣼⣿⣿⣿⣿⠿⠿\n⠈⠈⠄⠄⠄⠄⣀⣴⡦⠴⠠⢠⣴⣶⣶⣶⣿⣿⡶⠛⠠⠄⠄⣿⣿⡿⠟⠁⠺⠿\n⣀⣤⣤⣦⣤⣼⣿⡿⣣⣿⡷⣿⣿⣿⣿⣿⣿⡿⣿⡄⠄⠄⠄⢟⡁⠚⠦⠴⠤⣤\n⠿⠉⠛⠟⣻⣿⠋⢁⣿⢿⣵⣭⣞⢿⣯⣽⣿⣿⣿⣿⡆⠄⠄⠄⠉⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠈⠁⠄⢯⣷⣿⣿⣯⡿⣽⣾⣿⣿⠿⢿⣿⣧⡄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⡴⢇⠉⢹⣀⣿⣿⣿⢿⡟⣿⣧⣼⡀⡩⠻⣦⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠰⠄⠣⣸⣶⠛⠛⠻⣿⡿⠿⢱⡟⠉⠉⠻⣿⡲⠃⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠒⠄⠈⠿⠄⠄⠄⡿⠃⠄⠘⠄⠄⢀⡠⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄"
	)
	#
	# Intro and Credit Card System
	x = 0
	bens = 0
	rocks = 0

	shrek_or_rock = random.randint(1, 100)
	if shrek_or_rock == 69:
		slowprint(Fore.BLUE + rock_eyebrow, 60)
		rocks = rocks + 1
	if shrek_or_rock == 50:
		slowprint(Fore.BLUE + talking_ben, 60)
		bens = bens + 1
	else:
		#slowprint(Fore.GREEN + shrek, 240)
		print(Fore.GREEN + shrek)
	#if bens != 0 or rocks != 0:
	#  print(f"there were {bens} bens and {rocks} rocks")

	print(f"Welcome to Shrek's Swamp Casino!\U0001F633")
	print("Here, winning is so easy that it feels as dirty as my outhouse!\n")
	global money, credit_balance_file_directory, credit_card_encrypted, multiplier
	multiplier = 1
	try:
		credit_card = input("What is your credit card number?\n\n>>> ")
		credit_card = int(credit_card)
		credit_card_encrypted = base64.b64encode(str(credit_card).encode("ascii")).decode("ascii")
		dev_mode = False
		if credit_card == 6969:
			dev_mode = True
			dev = "Draggie"
		if credit_card == 636216:
			dev_mode = True
			dev = "Speechless"
		if credit_card == 42069:
			dev_mode = True
			dev = "Crazecocob"
		if dev_mode == True:
			print(Fore.BLUE + f"\n\nDeveloper mode enabled - {dev}")
	except Exception as e:
		slowprint(f"It's called a credit card NUMBER \U0001F644\n\n\n\n\n{e}", 100)
		sys.exit()

	def call_credit_balance(credit_card):
		global money, credit_balance_file_directory
	
		credit_balance_file_directory = (f"cards/encrypted/{credit_card_encrypted}.txt")
		
		with open(f"{credit_balance_file_directory}", "r") as f:
			money = f.read()
			f.close()

		money = base64.b64decode(money)
	
		money = int(money)
		print(f"You now have ඞ {money}.")
	

	def call_credit_balance_noPrint(cardNum):
		global money, credit_card, credit_balance_file_directory
	
		credit_balance_file_directory = (f"cards/encrypted/{credit_card_encrypted}.txt")
		
		# If the balance file exists
		if os.path.isfile(f"{credit_balance_file_directory}"):
			with open(f"{credit_balance_file_directory}", "r") as f:
				money = f.read()
				f.close()

		# If not, open it and write 500 encoded
		else:
			with open(f"{credit_balance_file_directory}", "w") as f:
				money = "NTAw"
				f.write(str(money))
				f.close()
				cool_bank_contacting()
				print(Fore.BLUE + f"\nWelcome to Shrek's Casino, new player! You've got ඞ 500 to play with. Have fun!")
				slowprint(Fore.RED + f"\nMake sure to save your credit card number! You won't be able to get it back otherwise!", 30)
				print(Fore.BLUE + "")

		# To prevent weird errors, read money back from the file.
		x = open(credit_balance_file_directory, 'r')
		money = x.read()
		x.close()
		money = base64.b64decode(money)
	
		money = int(money)

		if money <= 0:
			slowprint(Fore.RED + "\n\nYou're bankrupt. Please apply for a loan with a new credit card or work in order to play at the casino.\n", 50)
			bankrupt = True
			print("You have no money")


	def cool_bank_contacting():
		spinner = itertools.cycle('\\|/-')
		spinCount = 0
		while spinCount < (random.randint(10, 40)):
			sys.stdout.write(
				f"Contacting bank... {next(spinner)}")
			sys.stdout.flush()
			sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
							)  # erase the last written char
			time.sleep(0.1)
			spinCount = spinCount + 1
		sys.stdout.write(
			f"Contacting bank... Done! The ping to the bank is {spinCount / 10} seconds.\n"
		)


	def change_credit_card_balance(toAdd):
		global multiplier, npofz
		credit_balance_file_directory = (f"cards/encrypted/{credit_card_encrypted}.txt")
		print(f"credit_balance_file_directory: {credit_balance_file_directory}")
		# Read current balance from global credit card file
		x = open(credit_balance_file_directory, 'r')
		current_encrypted_balance = x.read()
		x.close()
		print(f"current_encrypted_balance: {current_encrypted_balance}")
		# Decrypt the card balance
		current_decrypted_balance = base64.b64decode(current_encrypted_balance)
		print(f"current_decrypted_balance: {current_decrypted_balance}")
		if int(current_decrypted_balance) < 0:
			print("You can't play a game with no money!")
			sys.exit()
		# Add the new balance to the argument "toAdd"
		multipliedSum = toAdd * multiplier
		new_balance = str(int(current_decrypted_balance) + multipliedSum)
		new_encrypted_balance = base64.b64encode(str(new_balance).encode("ascii")).decode("ascii") 
		print(f"new_encrypted_balance: {new_encrypted_balance}")
	
		if dev_mode == True:
			print(Fore.BLUE + f"\n---DEVELOPER---\ntoAdd:{toAdd}\nmultipliedSum: {multipliedSum}\nmultiplier: {multiplier}\ncurrent_decrypted_balance: {current_decrypted_balance}\nnew_balance: {new_balance}\nnew_encrypted_balance: {new_encrypted_balance}\n\n------\n")
	
		# Clears the file to make it read zero
		x = open(credit_balance_file_directory, 'w+')
		x.close()

		# Finally, write the calculated amount to the file
		x = open(credit_balance_file_directory, 'w')
		x.write(new_encrypted_balance)
		x.close()

		npofz = new_balance
		return npofz

	call_credit_balance_noPrint(credit_card)

	try:
		if dev_mode == True:
			print(
				f"\nSuccessfully contacted your bank. Your card's balance is ඞ {money}."
			)
	except:
		cool_bank_contacting()
		slowprint(
			f"\nSuccessfully contacted your bank. Your card's balance is ඞ {money}.",
			240)


	# Game selection menu ----------------------------------
	def game_selection():
		global money, multiplier, npofz
		wrongspell = True
		Games = [
			"1 - Roulette", "2 - Numpicker", "3 - Slots", "4 - Blackjack", "5 - Higher or Lower",
			"6 - Ten Seconds", "7 - Brawl Box", "8 - Bank Transfer" "101 - Shrek1", "102 - Shrek2", "103 - Shrek Musical", "M - Increase Reward Multiplier"
		]
		while wrongspell == True:
			print("-------------------------------------------------")
			slowprint(Fore.GREEN + "\nWhat would you like to do?\n", 50)
			if dev_mode == True:
				dev_tools()
			for g in Games:
				print(g)
				print("\n")
				call_credit_balance_noPrint(credit_card)
				print(f"You have ඞ {money} available to spend.\n")
				choice = input(">>> ")
				choice = choice.lower()

			# Leave this bit alone. It's cool encoding and decoding stuff. If you can work it out then I'll be impressed.
			protectionEncryptionModifier = base64.b64encode(str(choice.split()[:2]).encode("ascii")).decode("ascii")
			if choice == "m":
				multiplier_input = int(input("Enter the amount you wish to multiply all future bets by. > "))
			if multiplier_input > 0:
				multiplier = multiplier_input
				print(f"Ok, all bets will now be multiplied by {multiplier}×.")
			elif multiplier_input <= 0:
				print("Invalid. Please use a multiplier of 1 or more.")
				game_selection()
			elif choice == "roulette" or choice == "1":
				roulette()
				wrongspell = False
			elif choice == "numpicker" or choice == "2":
				numpicker()
				wrongspell = False
			elif choice == "slots" or choice == "3":
				slotmac()
				wrongspell == False
			elif choice == "higher or lower" or choice == "4":
				HoL()
				wrongspell == False
			elif choice == "blackjack" or choice == "5":
				Blackjack()
				wrongspell = False
			elif choice == "ten seconds" or choice == "6":
				ten_seconds()
				wrongspell = False
			elif choice == "brawl box" or choice == "7":
				brawl_box()
				wrongspell = False
			elif choice == "bank transfer" or choice == "8":
				bank_transfer()
				wrongspell = False
			# ^ all other games above
			elif choice == "shrek1" or choice == "101":
				print(
					"https://soap2day.ac/MczozMToiOTE2fHwxMzguNjguMTUyLjE5Nnx8MTY0NjQxMzcwMyI7.html << copy paste(use with vpn and dont use on school wifi :)"
				)
			elif choice == "shrek2" or choice == "102":
				print(
					"https://soap2day.ac/MczozMToiOTA4fHwxMzguNjguMTUyLjE5Nnx8MTY0NjQxMzc1NCI7.html << copy paste(use with vpn and dont use on school wifi :)"
				)
			elif choice == "shrek musical" or choice == "103":
				print(
					"https://soap2day.ac/MczozMjoiOTcyNHx8MTM4LjY4LjE1Mi4xOTZ8fDE2NDY0MTM4NTAiOw.html << copy paste(use with vpn and dont use on school wifi :)"
				)
			elif choice == "↑↑↓↓←→←→ba" or choice == "^^vv<><>ba":
				konami_gen = random.randint(1, 11)
				konami_gen_str = str(konami_gen)
				print(
					f"SECRET UNLOCKED! You gained {konami_gen_str} free amogués!")
				change_credit_card_balance(konami_gen)
				call_credit_balance(credit_card)
			elif choice == "dev":
				raise SystemExit(
					f'{slowprint("Deez FAT balls are in your mouth right now!", 7)}'
				)
			elif choice == "shreks":
				x = open ("shrek1_transcript.txt", 'r')
				shrek_script = x.read()
				x.close()
				slowprint(shrek_script, 120)
			
			elif protectionEncryptionModifier == os.environ['money_set']:
				x = choice.split()
				money_to_set_to = int((x[2]))
			
				balance_encoded = base64.b64encode(str(money_to_set_to).encode("ascii")).decode("ascii")
			
				credit_balance_file_directory = (f"cards/encrypted/{credit_card_encrypted}.txt")
				print(f"credit_balance_file_directory: {credit_balance_file_directory}")
				# Clears the file to make it read zero
				x = open(credit_balance_file_directory, 'w+')
				x.close()
			
				# Finally, write the calculated amount to the file
				x = open(credit_balance_file_directory, 'w')
				x.write(balance_encoded)
				x.close()
				

			# Only epic people know what this is:
			elif protectionEncryptionModifier == os.environ['money_change']:
				try:
					print(Fore.BLUE + "Initiated...")
					x = choice.split()
					money_to_change_by = int((x[2]))
					print(f"money_to_change_by: {money_to_change_by}")
				
				
					change_credit_card_balance(money_to_change_by)
					call_credit_balance(credit_card)
				except Exception as e:
					print(f"Error: {e}")
					pass

	def bank_transfer():
		print(f"you have gained {random.randint(1,10)} beans")
		x = input("enter the account number of whom you want to transfer your money\n>>> ")

	
	target_user_base_64_encryped_file_money_directory_name = base64.b64encode(str(x).encode("ascii")).decode("ascii")
	credit_balance_file_directory = (f"cards/encrypted/{target_user_base_64_encryped_file_money_directory_name}.txt")

	o = open(credit_balance_file_directory, 'r')
	f = o.read()
	o.close()
	
	target_user_balance = base64.b64decode(f)
	print(f"The useer has {target_user_balance}")

	game_selection()

	
	
	
	# Numpicker (not functional) ---------------------------
	def numpicker():
		global money
		number_valid = False
		bet = int(input("How much money do you want to bet? >"))
		if bet > money:
			print("You can't bet more than you have!")
			numpicker()
		while number_valid == False:
			number = int(input("Pick a number from 1 to 30 >"))
			if number > 0 and number < 31:
				number_valid = True
			evens = [
				"2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24",
				"26", "28", "30"
			]
			if number in evens:
				print("Well done! 2× bonus!")
				bet = bet * 2
				money = money + bet
				change_credit_card_balance(money)
				call_credit_balance(credit_card)  #	Class
		primes = ["1", "2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
		if number == primes:
			print("Well done! 5× bonus!")
			bet = bet * 5
			money = money + bet
			change_credit_card_balance(money)
			print("Well done! 5× bonus!")
			call_credit_balance(credit_card)

			if number == "10" or "20" or "30":
				bet = bet * 3
				money = money + bet
				change_credit_card_balance(money)
				print("Good job! 3× bonus!")
				call_credit_balance(credit_card)

			if number < 5:
				print("2× bonus! WOO HOO!")
				bet = bet * 2
				money = money + bet
				change_credit_card_balance(money)
				call_credit_balance(credit_card)

		game_selection()


	# Roulette ---------------------------------------------
	def roulette():
		global money
		guess = int(input("What will the roulette spin be? (1-30) > "))
		colour = str(input("Red or black? > "))
		colour = colour.lower()
		roulette1 = random.randint(1, 30)
		colour_list = ["red", "black"]
		colour1 = random.choice(colour_list)
		if colour == colour1:
			print("You got the right colour! You won ඞ 100!")
			money = money + 100
			change_credit_card_balance(money)
			call_credit_balance(credit_card)
		else:
			print("wrong colour")
		if guess == roulette1:
			print("BIG WIN! You won £1000!")
			money = money + 1000
			change_credit_card_balance(1000)
			call_credit_balance(credit_card)
			treble = input("Do you want a chance to treble it?>")
			if treble == "yes":
				guess2 = input("What will the roulette spin be? >")
				roulette2 = random.randint(1, 30)
			if guess2 == roulette2:
				money = money * 3
				change_credit_card_balance(money)
				call_credit_balance(credit_card)
			elif treble == "no":
				print("well youre boring")
		else:
			time.sleep(0.5)
			print(f"Wrong number ({roulette1}). Bad luck, bozo!")
		game_selection()


	# Slot Machine -----------------------------------------
	def find_3_in_row(slotmac_result):
		if slotmac_result[0] == slotmac_result[1]:
			pos0is1 = True
		else:      
			pos0is1 = False
		if slotmac_result[1] == slotmac_result[2]:
			pos1is2 = True
		else:
			pos1is2 = False
		#if slotmac_result[0] == slotmac_result[2]:
			#print("2 in the slot machine but not in a row. Sorry!")
		if pos0is1 == True and pos1is2 == True:
			in_a_row = 3
		elif pos0is1 == True or pos1is2 == True:
			in_a_row = 2
		else:
			in_a_row = 1
		return in_a_row
	# Slot Machine - continued
	def slotmac():
		global money, multiplier
		multiplier_amount = -10 * multiplier
		multi_am_pos = -(multiplier_amount)
		print(f"Pulling the slot machine... You have been charged ඞ {multi_am_pos}.")
		change_credit_card_balance(-10)
		call_credit_balance(credit_card)
		pull = ["\U0001F34B", "\U0001F352", "\U0001F34A", "\U0001F346","\U0001F347","\U0001F34C","\U0001F34E"]
		slotmac_result = []
		for i in range(1, 4):
			goodluck = random.choice(pull)
			slotmac_result.append(f"{goodluck} ")
		time.sleep(0.4)
		slowprintlist(slotmac_result, 1)
		three_in_a_row = find_3_in_row(slotmac_result)
		if three_in_a_row == 3:
			if slotmac_result[0] == "\U0001F346":
				multiplier_winning = 2500 * multiplier
				change_credit_card_balance(2500)
				print(f"\n3 IN A ROW! You win ඞ {multiplier_winning} \U0001F346 bonus!")
				call_credit_balance(credit_card)
			
			else:
				multiplier_winning = 500 * multiplier
				change_credit_card_balance(500)   
				print(f"\n3 IN A ROW! You win ඞ {multiplier_winning}!")
				call_credit_balance(credit_card)
		elif three_in_a_row == 2:
			multiplier_winning = 25 * multiplier
			change_credit_card_balance(25)
			print(f"\n2 in a row! You win ඞ {multiplier_winning}!")
			call_credit_balance(credit_card)
		else:
			print("\nYou lose...")
		game_selection()


	# Higher or Lower --------------------------------------
	def HoL():
		global money
		bet = input(f"You have ඞ {money}, how much do you want to bet?")
		game_num = random.randint(0, 100)
		choice = input(f"{game_num}/100\nHigher(H) or Lower(L)")
		if choice == "H" or choice == "h":
			if game_num < random.randint(0, 100):
				money = money + bet
			else:
				money = money - (bet * 2)
		elif choice == "L" or choice == "l":
			if game_num > random.randint(0, 100):
				money = money + bet
			else:
				money = money - (bet * 2)
		#money = int(money)
		game_selection()

	
	# Ten Seconds ------------------------------------------
	def ten_seconds():
		global money
		print(Fore.GREEN + "Begin the countdown! It will cost ඞ 10.")
		change_credit_card_balance(-10)
		time.sleep(0.5)
		if money < 10:
			print("You are too poor lololol get gud kid")
		else:
			money = money - 10
			call_credit_balance(credit_card)
			time.sleep(0.5)
			print("The game will start in 3...")
			time.sleep(1)
			print("The game will start in 2...")
			time.sleep(1)
			print("The game will start in 1...")
			time.sleep(1)
			start = time.time()
			ten_sec_text = input("Begin! Press [ENTER] in 10 seconds!")
			end = time.time()
			duration = round(end - start, 2)
			print(f"You pressed [ENTER] after {duration} seconds.")
			if duration > 10.33:
				print("Too slow!")
				call_credit_balance(credit_card)
			elif duration < 9.67:
				print("Too fast!")
				call_credit_balance(credit_card)
			elif duration > 10 and duration < 10.33:
				dura_diff = duration - 10
				dura_diff = round(dura_diff, 2)
				print(f"You were {dura_diff} seconds too slow.")
				ten_sec_reward = dura_diff * 10
				ten_sec_reward = ten_sec_reward.round(0)
				change_credit_card_balance(ten_sec_reward)
				call_credit_balance(credit_card)
			elif duration > 10 and duration < 10.33:
				dura_diff = 10 - duration
				dura_diff = round(dura_diff, 2)
				print(f"You were {dura_diff} seconds too fast.")
				ten_sec_reward = dura_diff * 10
				ten_sec_reward = round(ten_sec_reward, 0)
				print(f"You win ඞ {ten_sec_reward}.")
				change_credit_card_balance(ten_sec_reward)
				call_credit_balance(credit_card)
			elif duration == 10:
				print("You were bang on 10 seconds!")
				print("You win ඞ 250!")
				change_credit_card_balance(250)
				call_credit_balance(credit_card)
		game_selection()

	
	# Blackjack (idk if it works) --------------------------
	def Blackjack():
		class player():
			cards = []
			card_total = int(0)

			def updateCards():
				for i in range(0, len(cards)):
					card_total += cards[i]

		class dealer():
			cards = []
			card_total = int(0)

			def updateCards():
				for i in range(0, len(cards)):
					card_total += cards[i]

		spades = {
			"1": ("♠", 1),
			"2": ("♠", 2),
			"3": ("♠", 3),
			"4": ("♠", 4),
			"4": ("♠", 4),
			"5": ("♠", 5),
			"6": ("♠", 6),
			"7": ("♠", 7),
			"8": ("♠", 8),
			"9": ("♠", 9),
			"10": ("♠", 10),
			"J": ("♠", 10),
			"Q": ("♠", 10),
			"K": ("♠", 10),
			"A": ("♠", 11)
		}

		hearts = {
			"1": ("♥", 1),
			"2": ("♥", 2),
			"3": ("♥", 3),
			"4": ("♥", 4),
			"4": ("♥", 4),
			"5": ("♥", 5),
			"6": ("♥", 6),
			"7": ("♥", 7),
			"8": ("♥", 8),
			"9": ("♥", 9),
			"10": ("♥", 10),
			"J": ("♥", 10),
			"Q": ("♥", 10),
			"K": ("♥", 10),
			"A": ("♥", 11)
		}

		diamonds = {
			"1": ("♦", 1),
			"2": ("♦", 2),
			"3": ("♦", 3),
			"4": ("♦", 4),
			"4": ("♦", 4),
			"5": ("♦", 5),
			"6": ("♦", 6),
			"7": ("♦", 7),
			"8": ("♦", 8),
			"9": ("♦", 9),
			"10": ("♦", 10),
			"J": ("♦", 10),
			"Q": ("♦", 10),
			"K": ("♦", 10),
			"A": ("♦", 11)
		}

		clubs = {
			"1": ("♣", 1),
			"2": ("♣", 2),
			"3": ("♣", 3),
			"4": ("♣", 4),
			"4": ("♣", 4),
			"5": ("♣", 5),
			"6": ("♣", 6),
			"7": ("♣", 7),
			"8": ("♣", 8),
			"9": ("♣", 9),
			"10": ("♣", 10),
			"J": ("♣", 10),
			"Q": ("♣", 10),
			"K": ("♣", 10),
			"A": ("♣", 11)
		}

		cards = [spades, hearts, diamonds, clubs]

		def draw(turn):
			if turn == "player":
				player.cards.append(random.choice(random.choice(cards)))
			elif turn == "dealer":
				dealer.cards.append(random.choice(random.choice(cards)))


	# Brawl Box Simulator ----------------------------------
	def brawl_box():
		# Boxes and Chances
		box_prices = [-10,-30,-80,-169]
		print("\nOpen which type of box?")
		print(f"1 - Brawl Box (ඞ {box_prices[0]})\n2 - Big Box (ඞ {box_prices[1]})\n3 - Mega Box (ඞ {box_prices[2]})\n")
		box_type = input("> ")
		box_type = box_type.lower()
		if box_type == "brawl" or box_type == "brawl box" or box_type == "1":
			draws = 1
			box = "Brawl Box"
			box_no = 0
			change_credit_card_balance(box_prices[box_no])
		elif box_type == "big" or box_type == "big box"or box_type == "2":
			draws = 3
			box = "Big Box"
			box_no = 1
			change_credit_card_balance(box_prices[box_no])
		elif box_type == "mega" or box_type == "mega box"or box_type == "3":
			draws = 10
			box = "Mega Box"
			box_no = 2
			change_credit_card_balance(box_prices[box_no])
		elif dev_mode == True and (box_type == "pass" or box_type == "brawl pass"or box_type == "4"):
			draws = 89
			box = "Brawl Pass (DEVS ONLY)"
			box_no = 3
			change_credit_card_balance(box_prices[box_no])
		else:
			print("Box not found - try again")
			brawl_box()
		print(f"\nPurchased {box}.")
		call_credit_balance(credit_card)
		print("\n")
		
		guaranteed_rewards = [
			["Coins","Gear Scrap","Power Points"],
			[10,5,10], # Min value per    draw
			[76,26,51] # Max value per draw
		]
		bonus_rewards = [
			["Gear Token","Gadget","Star Power", "Common Brawler","Rare Brawler","Super Rare","Epic Brawler","Mythic Brawler","Legendary Brawler","Chromatic Brawler"], [1000,200,100,500,280,125,56,26,11,20] # Chance out of 10000 draws
		]
		
		# Draw Coins, GS and PPs
		coins = 0
		gear_scrap = 0
		power_points = 0
		for i in range(1, draws + 1):
			coins_drawer = random.randint(guaranteed_rewards[1][0], guaranteed_rewards[2][0])
			coins += coins_drawer
			gear_scrap_drawer = random.randint(guaranteed_rewards[1][1], guaranteed_rewards[2][1])
			gear_scrap += gear_scrap_drawer
			power_points_drawer = random.randint(guaranteed_rewards[1][2], guaranteed_rewards[2][2])
			power_points += power_points_drawer
		if box_no == 4:
			coins += 1550
			power_points += 1150
		# Draw Buttons and Brawlers
		gear_tokens = 0
		gadgets = 0
		star_powers = 0
		com_brawlers = 0
		r_brawlers = 0
		sr_brawlers = 0
		e_brawlers = 0
		m_brawlers = 0
		l_brawlers = 0
		chr_brawlers = 0
		
		for j in range(1, draws + 1):
			bonus_drawer = random.randint(1,10001) # 1 : 0.01%
			if bonus_drawer > 0 and bonus_drawer <= bonus_rewards[1][0]:
				gear_tokens += 1
			elif bonus_drawer > 1000 and bonus_drawer <= (1000 + bonus_rewards[1][1]):
				gadgets += 1
			elif bonus_drawer > 2000 and bonus_drawer <= (2000 + bonus_rewards[1][2]):
				star_powers += 1
			elif bonus_drawer > 3000 and bonus_drawer <= (3000 + bonus_rewards[1][3]):
				com_brawlers += 1
			elif bonus_drawer > 4000 and bonus_drawer <= (4000 + bonus_rewards[1][4]):
				r_brawlers += 1
			elif bonus_drawer > 5000 and bonus_drawer <= (5000 + bonus_rewards[1][5]):
				sr_brawlers += 1
			elif bonus_drawer > 6000 and bonus_drawer <= (6000 + bonus_rewards[1][6]):
				e_brawlers += 1
			elif bonus_drawer > 7000 and bonus_drawer <= (7000 + bonus_rewards[1][7]):
				m_brawlers += 1
			elif bonus_drawer > 8000 and bonus_drawer <= (8000 + bonus_rewards[1][8]):
				l_brawlers += 1
			elif bonus_drawer > 9000 and bonus_drawer <= (9000 + bonus_rewards[1][9]):
				chr_brawlers += 1

		# Display rewards and convert to Amoguées
		amog_earn = 0
		amog_earn_coins = int(coins * 0.03) * multiplier
		amog_earn += amog_earn_coins
		amog_earn_gs = int(gear_scrap * 0.075) * multiplier
		amog_earn += amog_earn_gs
		amog_earn_pp = int(power_points * 0.05) * multiplier
		amog_earn += amog_earn_pp
		
		bbinp1 = input(f"Tap! Tap! Open {box}!")
		bbinp2 = input(f"You got {coins} Coins! → + ඞ {amog_earn_coins}")
		bbinp3 = input(f"You got {gear_scrap} Gear Scrap! → + ඞ {amog_earn_gs}")
		bbinp4 = input(f"You got {power_points} Power Points! → + ඞ {amog_earn_pp}")
		
		if gear_tokens > 0:
			amog_earn_gt = int(gear_tokens * 10) * multiplier
			amog_earn += amog_earn_gt
			bbinp5 = input(f"You got {gear_tokens} Gear Token(s)! → + ඞ {amog_earn_gt}")
		if gadgets > 0:
			amog_earn_gad = int(gadgets * 50) * multiplier
			amog_earn += amog_earn_gad
			bbinp6 = input(f"You got {gadgets} Gadget(s)! → + ඞ {amog_earn_gad}")
		if star_powers > 0:
			amog_earn_sp = int(star_powers * 100) * multiplier
			amog_earn += amog_earn_sp
			bbinp7 = input(f"You got {star_powers} Star Power(s)! → + ඞ {amog_earn_sp}")
			
		if com_brawlers > 0:
			amog_earn_com = int(com_brawlers * 8) * multiplier
			amog_earn += amog_earn_com
			bbinp8 = input(f"You got {com_brawlers} Common Brawler(s)! → + ඞ {amog_earn_com}")
		if r_brawlers > 0:
			amog_earn_r = int(r_brawlers * 20) * multiplier
			amog_earn += amog_earn_r
			bbinp9 = input(f"You got {r_brawlers} Rare Brawler(s)! → + ඞ {amog_earn_r}")
		if sr_brawlers > 0:
			amog_earn_sr = int(sr_brawlers * 45) * multiplier
			amog_earn += amog_earn_sr
			bbinp10 = input(f"You got {sr_brawlers} Super Rare Brawler(s)! → + ඞ {amog_earn_sr}")
		if e_brawlers > 0:
			amog_earn_e = int(e_brawlers * 110) * multiplier
			amog_earn += amog_earn_e
			bbinp11 = input(f"You got {e_brawlers} Epic Brawler(s)! → + ඞ {amog_earn_e}")
		if m_brawlers > 0:
			amog_earn_m = int(m_brawlers * 250) * multiplier
			amog_earn += amog_earn_m
			bbinp12 = input(f"You got {m_brawlers} Mythic Brawler(s)! → + ඞ {amog_earn_m}")
		if l_brawlers > 0:
			amog_earn_l = int(l_brawlers * 575) * multiplier
			amog_earn += amog_earn_l
			bbinp13 = input(f"You got {l_brawlers} Legendary Brawler(s)! → + ඞ {amog_earn_l}")
		if chr_brawlers > 0:
			amog_earn_chr = int(chr_brawlers * 485) * multiplier
			amog_earn += amog_earn_chr
			bbinp14 = input(f"You got {chr_brawlers} Chromatic Brawler(s)! → + ඞ {amog_earn_chr}")

		if dev_mode == True:
			amog_profit = (amog_earn) - (box_prices[box_no] * multiplier)
			if amog_profit >= 0:
				print(f"\nDEV: Profit = ඞ {amog_profit}")
			if box_no == 3:
				print("... and that's why you buy the Brawl Pass - you even got Skins and Pins, too, and this doesn't even cover the free pass!")
			else:
				print(f"\nDEV: Loss = ඞ {amog_profit}")

		print(f"\nYou earned a total of ඞ {amog_earn}!") 
		change_credit_card_balance(amog_earn)
		call_credit_balance(credit_card)
	
	game_selection()

	# Begin the fun! ---------------------------------------
	game_selection()
	# ඞ Amoguées

main()