class DiaryEntry:
	def __init__(self, title, contents):
		self.title = title
		self.contents = contents
	#	self.position = 0
		
	def count_words(self):
		return len(self.contents.split())
	
	def reading_time(self, wpm):
		self.wpm = wpm
		averange = self.count_words() * 60 // self.wpm
		return f"Reading time: {averange} minuts" 
	
	def reading_chunk(self, wpm, minutes):
		qtd_word_this_time = wpm * minutes
		split_contents = self.contents.split()
		if self.position > len(self.contents.split()):
			self.position = 0
		read = " ".join(split_contents[self.position:self.position + qtd_word_this_time])
		self.position += qtd_word_this_time
		return read    