import subprocess, os
from .wrapper import SubmissionWrapper

class SubmissionGo(SubmissionWrapper):

	def __init__(self, file):
		SubmissionWrapper.__init__(self)
		self.file = file

	def language(self):
		return 'go'

	def run(self, s):
		try:
			output_raw = subprocess.check_output(["go", "run", self.file, s]).decode()
			output_rows = output_raw.split('\n')[:-1]
			if len(output_rows) > 1:
				print('\n'.join(output_rows[:-1]))
			return output_rows[-1]
		except OSError as e:
			if e.errno == os.errno.ENOENT:
				# executable not found
				return None
			else:
				# subprocess exited with another error
				return None

	def __call__(self):
		return SubmissionGo(self.file)
