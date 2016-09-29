import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', type = float, required = True)
	parser.add_argument('-y', type = float, required = True)
	args = parser.parse_args()
	return args.x, args.y

x, y = get_args()
print x, y

