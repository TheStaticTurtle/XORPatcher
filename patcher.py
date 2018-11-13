import random,sys,os
fname = os.path.abspath(sys.argv[1])
def applyXOR(file):
	try:
		print("Applying XOR to  "+file)
		reload(random)
		random.seed(fname)
		b = bytearray(open(fname, 'rb').read())
		for i in range(len(b)):
			b[i] ^= random.randint(0,254)
		open(fname, 'wb').write(b)
	except IOError:
		print("IOError while applying XOR to  "+file)
if os.path.isfile(fname):
	applyXOR(fname)
else:
	files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(fname) for f in filenames]
	for fname in files:
		applyXOR(fname)