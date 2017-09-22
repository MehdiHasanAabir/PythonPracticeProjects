__author__ = 'Aabir'

''' dependencies '''
import requests 
from bs4 import BeautifulSoup 

addr = requests.get('https://www.nytimes.com')
html = addr.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')

''' will look for all the tags with the css class name'''
storytitle = soup.find_all(class_ = 'story-heading')


'''*find_all() finds passed string argument as an html tag 
   *find_all(tag, class name) '''


for story in storytitle:
    if story.a: #is true then do this
        print(story.a.text.strip())
        
        '''*replace(old, new, position)
        * here a is the tag name. 
        * text attribute will only show text inside a tag
        , not links.
        * here an empty strip() will remove all the white spaces
        or indentations.
        '''
        
    else: 
        print(story.contents[0].strip())
        ''' will show story-heading without the 'a' tag.
        in this example it's h3 tags. All contents inside 
        tags other than 'a' tags will be shown.
        Only contents will be shown. '''
