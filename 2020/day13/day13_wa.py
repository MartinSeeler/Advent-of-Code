with open("input.txt", "r") as f:
	ids = list(f.read().split(","))
	print('https://www.wolframalpha.com/input/?i=0+%3D+' + '+%3D+'.join(['((n+%2B+{})+mod+{})'.format(i, n) for i, n in enumerate(ids) if n != 'x']))