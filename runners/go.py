import subprocess, os
from .wrapper import SubmissionWrapper

class SubmissionGo(SubmissionWrapper):

	def __init__(self, file):
		SubmissionWrapper.__init__(self)
		self.file = file

	def language(self):
		return 'go'

	def exec(self, input):
		try:
			return subprocess.check_output(["go", "run", self.file, input]).decode()
		except OSError as e:
			if e.errno == os.errno.ENOENT:
				# executable not found
				return None
			else:
				# subprocess exited with another error
				return None

	def __call__(self):
		return SubmissionGo(self.file)
