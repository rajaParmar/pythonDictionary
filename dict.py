from bs4 import BeautifulSoup
import urllib.request as ur
word=input()
link="http://www.dictionary.com/browse/"+word
source=ur.urlopen(link).read()
soup=BeautifulSoup(source,"lxml")
#print(soup.prettify())
divs=soup.find_all("div",class_="def-content")
#print(divs)
no_of_result=0
result=[]
for ele in divs:
	no_of_result=no_of_result+1
	result.append(ele.get_text()[2:-2])
	if(no_of_result==3):
		break

for i in result:
	print(i)


