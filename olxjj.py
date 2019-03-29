from bs4 import BeautifulSoup
import time
import itertools
import requests
import re

#progress indicator
class PROGRESS:
		def __init__(self):
				self.char=itertools.cycle('/-\|')
		def run(self):
				print(next(self.char), end = '\r')


class OLXJJ:
	def __init__(self,url):
		self.url=url
		#prepare data to parse (to discover links/pages)
		self.r  = requests.get(self.url)
		self.data = self.r.text
		self.soup = BeautifulSoup(self.data,features="html.parser")

		#get number of pages
		try:
			self.nr_of_pages = int(str(self.soup.find("a", {"data-cy": "page-link-last"})).split(";page=")[1].split('"')[0])
		except:
			print("Problem to determine number of pages or there is only 1 page (nr_of_pages)")
			self.nr_of_pages=1
		
		self.progress=PROGRESS()
		
	#returns direct links to offers from single page
	def _get_links_from_page(self,soup):
		self.soup=soup
		self.righttab = self.soup.find("table", {"class": "fixed offers breakword redesigned"}) 
		self.offers=[]
		for link in self.righttab('a'):
			if "promoted" in str(link): continue
			if "oferta" in str(link) and link.get('href') not in self.offers: self.offers.append(link.get('href'))
		return self.offers
		
	#returns offer links for all pages (combined)
	def _get_all_links(self):
		for self.page_nr in range(1,self.nr_of_pages+1):
			self.output=[]
			if self.url[-1:] is "/": self.r  = requests.get(self.url+"?page="+str(self.page_nr))  #because there are different versions of links
			else:                    self.r  = requests.get(self.url+"&page="+str(self.page_nr))
			self.data = self.r.text
			self.soup = BeautifulSoup(self.data,features="html.parser")
			for link in self._get_links_from_page(self.soup): self.output.append(link)
			self.progress.run()
		return self.output
		
	#returns dict with links, that include specific words in the page text, 
	#format: {link:[word1 with context, word2 with context....]}
	#if and_or equals "and", all words must be present in the link,
	#if it equals "or", any of words must be in the link
	#you can put many words as arguments or pass list with words
	def get_links_with_word(self,and_or,*words):	
		self.links=self._get_all_links()
		self.words=words
		if type(self.words[0]) is list: self.words = self.words[0]    #if list was passed as argument for words
		print (self.words)
		self.output={}
		
		for self.number,self.link in enumerate(self.links):
			print("Working for link "+str(self.number+1)+" of "+str(len(self.links)))
			self.r  = requests.get(self.link)
			self.data = self.r.text
			self.soup = BeautifulSoup(self.data,features="html.parser")
			self.description = self.soup.find(True, {"class": "section-description"})  #search in description field of olx or otodom
			if(self.description is None): self.description = self.soup.find(True, {"class": "clr lheight20 large"})
			
			self.output_partial=[]
			hitcount=0
			for self.word in self.words:					
				if re.search(self.word,self.soup.text):
					hitcount+=1
					self.output_partial.append(re.findall(".{25}"+self.word+".{25}",self.soup.text))      #save link and word with chars around it
					
			if and_or=="or": self.output.update({self.link:self.output_partial})
			if and_or=="and" and hitcount==len(self.words): self.output.update({self.link:self.output_partial})
			
		print("Done.")
		return self.output