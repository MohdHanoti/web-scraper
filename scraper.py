from bs4 import BeautifulSoup
import requests 

URL="https://en.wikipedia.org/wiki/Petra"



def get_citations_needed_count(URL):
    '''this function will return the number of citations_needed in the website'''
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')

    citation_needed_arr=soup.find_all(title="Wikipedia:Citation needed")
    return len(citation_needed_arr)

def get_citations_needed_report(URL):
    '''this function will return the information that need citations in the website'''

    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    
    citation_needed_arr=soup.find_all(title="Wikipedia:Citation needed")
    counter=0
    obj_citations={}
    for citation in citation_needed_arr:
        counter+=1
        report=citation.parent.parent.parent.text.strip()
        obj_citations[f"citation needed {counter}"]=report
    return (obj_citations)    
        
        


print('citation number in this webcite is : ',get_citations_needed_count(URL))
print(get_citations_needed_report(URL))
