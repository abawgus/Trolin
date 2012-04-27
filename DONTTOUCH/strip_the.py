def strip_the(stuff):
	if stuff[0]=='the':
		return stuff[1:]
	else:
		return stuff

print strip_the('the','house')
