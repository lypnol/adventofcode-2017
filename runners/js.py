# 3p
import execjs
# project
from runners.python import Submission


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
		answer, stdout = self.compiled.call('console.run', s)
		if stdout:
			print(stdout)
		return answer

class SubmissionJsGenerator:
	def __init__(self, source):
		console = """
var console = {
	lines: [],
	log: function() {
		var parts = [];
		for (var i = 0; i < arguments.length; i++) {
			parts.push(arguments[i].toString());
		}
		var line = parts.join(' ');
		console.lines.push(line);
		return line;
	},
	flush: function() {
		if (console.lines.length) {
			return console.lines.join('\\n');
		}
		return null;
	},
	run: function(input) {
		return [run(input), console.flush()];
	}
};
"""
		self.compiled = execjs.compile(console + source)

	def __call__(self):
		return SubmissionJs(self.compiled)