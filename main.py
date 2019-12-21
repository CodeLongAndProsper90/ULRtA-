from colorama import Fore, Style
fname = input("LOAD: ")

source = open(fname, 'r')
source_raw = source.read().rstrip()
source.close()
source = source_raw.split('\n')

try:
	source.remove('')
except:
	source = source
i = []


def reg(var):
	if var.startswith('$'):
		if var not in regs:
			throw("RegisterError", "Register {} does not exist or has not been initialized in the current context! {}".format(var.replace('$','',1),p+1))
		else:
			return (regs[var])
	elif var.startswith("\""):
		Str = ''
		for item in i:
			Str = Str + ' ' + item
		Str = Str.split("\"")
		Str.remove(Str[0])
		String = Str[0].replace('_',' ')
		return String
		pass

	else:
		return int(var)


def throw(error, msg=''):
	print("\n\033[1m{}{}{} :: {} @{}! {}{}\n".format(Fore.GREEN,p+1,Fore.RESET,Fore.RED,error,msg,Style.RESET_ALL))
	exit()


def warn(warning, msg=''):
    print("\n\033[1m{}{} {}:: {}{}! {}{}\n".format(Fore.GREEN,p+1,Fore.RESET,Fore.LIGHTYELLOW_EX,warning,msg,Style.RESET_ALL))


def confirm(foo, bar, ret=False, error='HaltError', msg='Unsure if arguments are the same!'):

	if not foo == bar:
		if not ret:
			throw(error, msg)
		else:
			return 0
	else:
		if ret:
			return 1


def math(a, b, o):
	a = int(a)
	b = int(b)
	if o == '+':
		return a + b
	elif o == '-':
		return a - b
	elif o == '*':
		return a * b
	elif 0 == '/':
		return a / b


regs = {}
p = 0
left_point = None
while p < len(source):
	item = source[p]

	i = item.split(' ')
	l = len(i) - 1

	if i[0].startswith('//'):
		p += 1
		continue
	for item in i:
		i[i.index(item)] = item.rstrip()

	if i[0] == 'mov':

		if i[1].startswith("\""):
			Str = ''
			for item in i:
				Str = Str + ' ' + item
			Str = Str.split("\"")
			Str.remove(Str[0])
			regs[Str[1].replace(' ','',1)] = Str[0].replace('_',' ')
		else:
			regs[i[2]] = int(reg(i[1]))

	elif i[0] == 'add':
		regs[i[3]] = int(reg(i[1])) + int(reg(i[2]))

	elif i[0] == 'out':
		print(reg(i[1]))

	elif i[0] == 'sub':
		confirm(l, 3)
		regs[i[3]] = int(reg(i[1])) - int(reg(i[2]))
	elif i[0] == 'times':
		regs[i[3]] = math(reg(i[1]), reg(i[2]), '*')
	elif i[0] == 'div':
		regs[i[3]] = math(reg[i[1]], reg(i[2]), '/')
	elif i[0] == 'goto':
		if not p == reg(i[1])-1:
			p = int(reg(i[1])) - 1
		else:
			throw('LoopWarning','Goto results in an endless loop!')
		continue

	elif i[0] == 'if':
		i1 = i
		try:
			i1.remove('is')
			i1.remove('goto')
		except:
			None
		if reg(i1[1]) == reg(i1[2]):
			p = int(reg(i1[3])) -1
			continue

	elif i[0] == 'join':
		regs[i[3]] = reg(i[1]) + reg(i[2])
	elif i[0] == 'in':
		regs[i[2]] = input(reg(i[1]))
	elif i[0] == 'end':
		break
	elif i[0] == 'int':
		try:
			regs[i[1]] = int(regs[i[1]])
		except ValueError:
			throw("ConversionError", 'Invalid conversion to int!')
	elif i[0] == 'str':
		regs[i[0]] = str(regs[i[1]])
	elif i[0] == 'type':
		if type(reg(i[1])) is int:
			regs[i[2]] = 1
		elif type(reg(i[1])) is str:
			regs[i[2]] = 2
	elif i[0] == 'dump':
		print("CORE MEMORY:\n",regs)
		warn('Stop_check', 'An application requsted a core dump')
	elif i[0] == 'call':
		left_point = p
		print(left_point)
		p=reg(i[1])
		continue
	elif i[0] == 'ret':
		try:
			type(left_point)
		except:
			throw('CallError','You have\'nt gone anywhere, so where can you?')
		
		p= left_point
	elif i[0] == 'inc':
		confirm(type(reg(i[1])),int, error='MathError', msg="Cannot increment type <String>")
		confirm(i[1].startswith('$'), True, error='RegisterError', msg='Attempting to write to a read-only register. Register=({})'.format(i[1]))
		regs[i[1]] = reg(i[1])+1
	elif i[0] == 'dec':
		confirm(type(reg(i[1])),int, error='MathError', msg="Cannot decrement type <String>")
		confirm(i[1].startswith('$'), True, error='RegisterError', msg='Attempting to write to a read-only register. Register=({})'.format(i[1]))
		regs[i[1]] = reg(i[1])+1
	
	p += 1
