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
			output_raw = subprocess.check_output(["node", "-e", self.script, s]).decode()
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
		return SubmissionJs(self.file)
