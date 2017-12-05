from submission import Submission


class LizzarocSubmission(Submission):

	def run(self, s):
		return(sum([int(e) if s[idx] == s[(idx+1) % len(s)] else 0 for idx, e in enumerate(s)]))

