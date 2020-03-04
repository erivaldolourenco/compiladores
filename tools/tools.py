
class Tools(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

	def print_f(msg, filename):
		# sample = open(str(filename)+'.out', 'w') 
		with open(str(filename)+'.out', 'a') as f:

			f.write(msg+'\n')
			# sample.close() 