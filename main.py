import os

class Digg3r():
	def __init__(self, urdir, word):
		self.urdir = urdir
		self.word = str(word)

	def digfind(self, locates, word):
		try:
			digread = open(locates, encoding="utf8").read()
			if word in digread:
				return True
			else:
				return False
		except:
			return False

	def core(self, urdirx=0):
		deepdir = []
		if urdirx==0:
			usedir = self.urdir
		else:
			usedir = urdirx
		for x in os.listdir(usedir):
			dirf = f'{usedir}\{x}'
			if os.path.isfile(dirf):
				if self.digfind(dirf, self.word):
					wordfind = "(Found)"
					with open("result.txt", "a") as digresult:
						digresult.write(f"[{dirf}] - Found word ({self.word})\n")
				else:
					wordfind = "(Not Found)"
				print("[File] - " + x + " - " + wordfind)
			elif os.path.isdir(dirf):
				print("[Folder] - " + x)
				deepdir.append(dirf)
		print("--- Deeper ---")
		for next in deepdir:
			self.core(next)


inp = input("Enter Directory Address : ")
word = input("Enter Word to Find : ")
go = Digg3r(inp, word).core()