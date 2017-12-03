# 3p
import execjs
# project
from submission import Submission


class CompilerError(Exception): pass

class SubmissionJs(Submission):

	def __init__(self, compiled):
		Submission.__init__(self)
		self.compiled = compiled

	def language(self):
		return 'js'

	def run(self, s):
		if self.compiled is None:
			raise CompilerError("Js source not compiled")
		return self.compiled.call('run', s)

class SubmissionJsGenerator:
	def __init__(self, source):
		self.compiled = execjs.compile(source)

	def __call__(self):
		return SubmissionJs(self.compiled)