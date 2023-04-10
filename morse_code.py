from datetime import date
from optparse import OptionParser
from colorama import Fore, Back, Style
from time import strftime, localtime, time

status_color = {
	'+': Fore.GREEN,
	'-': Fore.RED,
	'*': Fore.YELLOW,
	':': Fore.CYAN,
	' ': Fore.WHITE,
}

raw_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',']
encode_list = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", "/", "_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", "._._._", "__..__"]

def get_time():
	return strftime("%H:%M:%S", localtime())
def display(status, data):
	print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {get_time()}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

def get_arguments(*args):
	parser = OptionParser()
	for arg in args:
		parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
	return parser.parse_args()[0]

def encode(data, error=True):
	encoded_result, error_list = "", {}
	data = data.upper()
	for index, item in enumerate(data):
		try:
			encoded_result += f"{encode_list[raw_list.index(item)]} "
		except:
			if error:
				return -1
			else:
				error_list[index] = item
	return encoded_result, error_list
def decode(data, error=True):
	decoded_result, error_list = "", {}
	sentences = data.split('/')
	for index, sentence in enumerate(sentences):
		words = sentence.split(' ')
		words = [word for word in words if word != '']
		for word in words:
			try:
				decoded_result += f"{raw_list[encode_list.index(word)]}"
			except:
				if error:
					return -1
				else:
					error_list[index] = word
		decoded_result += ' '
	return decoded_result, error_list

if __name__ == "__main__":
	data = get_arguments(('-e', "--encode", "encode", "File to load data from to encode"),
		                 ('-d', "--decode", "decode", "File to load data from to decode"))
	if data.encode:
		try:
			with open(data.encode, 'r') as file:
				data = file.read().split('\n')
		except FileNotFoundError:
			display('-', f"File {Back.MAGENTA}{data.encode}{Back.RESET} Not Found")
		except:
			display('-', "Some Error Occured")
		for sentence in data:
			print(encode(sentence, error=False)[0])
		exit(0)
	if data.decode:
		try:
			with open(data.decode, 'r') as file:
				data = file.read().split('\n')
		except FileNotFoundError:
			display('-', f"File {Back.MAGENTA}{data.decode}{Back.RESET} Not Found")
		except:
			display('-', "Some Error Occured")
		for sentence in data:
			print(decode(sentence, error=False)[0])
		exit(0)
	print("(1) Encode\n(2) Decode")
	choice = int(input("Enter your Choice : "))
	if choice == 1:
		data = input("Enter the String to Encode : ")
		print(encode(data, error=False)[0])
	else:
		data = input("Enter the String to Decode : ")
		print(decode(data, error=False)[0])