from html.parser import HTMLParser

class LinkHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tags_src = ("img", "bgsound", "embed", "iframe", "script", "input")
		self.tags_href = ("a", "link", "area")
		self.tags_misc = {"body":("background"), "form":("action"), "object":("data"), 
							"blockquote":("cite")}
	def handle_starttag(self, tag, attrs):
		if tag in self.tags_src:
			print("Found tag", tag, "looking for attribute src")
			for attr, value in attrs:
				if(attr.lower() == "src"):
					# analyze the path given and rename accordingly
					break
		elif tag in self.tags_href:
			print("Found tag", tag, "looking for attribute href")
			for attr, value in attrs:
				if(attr.lower() == "href"):
					# analyze the path given and rename accordingly
					break
		elif tag in self.tags_misc.keys():
			wanted_attr = self.tags_misc[tag]
			print("Found tag", tag, "looking for attribute", wanted_attr)
			for attr, value in attrs:
				if(attr.lower() == wanted_attr.lower()):
					# analyze the path given adn rename accordingly
					break
