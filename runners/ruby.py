import subprocess, os
from .wrapper import SubmissionWrapper

class SubmissionRb(SubmissionWrapper):

	def __init__(self, file):
		SubmissionWrapper.__init__(self)
		self.file = file

	def language(self):
		return 'rb'

	def run(self, s):
		try:
			output_raw = subprocess.check_output(["ruby", self.file, s]).decode()
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
		return SubmissionRb(self.file)
