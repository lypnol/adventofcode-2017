import subprocess, os
from .wrapper import SubmissionWrapper
import tempfile

class CompilationError(Exception): pass

class SubmissionCpp(SubmissionWrapper):

	def __init__(self, file):
		SubmissionWrapper.__init__(self)
		tmp = tempfile.NamedTemporaryFile(prefix="aoc")
		tmp.close()
		compile_output = subprocess.check_output(["g++", "-std=c++11", "-o", tmp.name, file]).decode()
		if compile_output:
			raise CompilationError(compile_output)
		self.executable = tmp.name

	def language(self):
		return 'cpp'

	def exec(self, input):
		try:
			return subprocess.check_output([self.executable, input]).decode()
		except OSError as e:
			if e.errno == os.errno.ENOENT:
				# executable not found
				return None
			else:
				# subprocess exited with another error
				return None
