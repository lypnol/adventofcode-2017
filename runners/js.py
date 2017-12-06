import subprocess, os
from runners.python import Submission

class SubmissionJs(Submission):

	def __init__(self, file):
		Submission.__init__(self)
		self.file = file
		self.script = """{script}
result = run(process.argv[1]);
console.log(result);
""".format(script=open(file).read())

	def language(self):
		return 'js'

	def run(self, s):
		try:
			output = subprocess.check_output(["node", "-e", self.script, s]).decode()
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
