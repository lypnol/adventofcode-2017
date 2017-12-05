import subprocess, os
from runners.python import Submission

class SubmissionJs(Submission):

	def __init__(self, file):
		Submission.__init__(self)
		self.file = file

	def language(self):
		return 'js'

	def run(self, s):
		try:
			output = subprocess.check_output(["node", "-e", "{script}\nconsole.log(run(process.argv[1]));".format(script=open(self.file).read()), s]).decode()
			return output.split('\n')[-2]
		except OSError as e:
			if e.errno == os.errno.ENOENT:
				# executable not found
				return None
			else:
				# subprocess exited with another error
				return None

	def __call__(self):
		return SubmissionJs(self.file)
