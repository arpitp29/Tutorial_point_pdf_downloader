#   Arpit Padwekar
#   5/13/2017


from bs4 import BeautifulSoup
import urllib2
import os
import errno

url="https://www.tutorialspoint.com/tutorialslibrary.htm"
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def downloadfile(url,filename):
    data = urllib2.urlopen(url).read()
    output = open(os.path.join(os.getcwd() + "\/tutorialpoint_pdfs/" + filename), 'wb')
    output.write(data)
    output.close()

def downloadpdf(url):
    url_list=url.split('/')
    pdf_url="https://www.tutorialspoint.com/"+url_list[1]+"/"+url_list[1]+"_tutorial.pdf";
    try :
        downloadfile(pdf_url,url_list[1]+".pdf")
        print url_list[1]+"  [successful]"
    except:
        print url_list[1] + "  [failed]"

def get_all_names(url):
    res = str(urllib2.urlopen(url).read())
    soup = BeautifulSoup(res, 'html.parser')
    links=[]
    i=0
    for link in soup.findAll('a'):
        href = link.get('href')
        if i>=18 and href.find('index.htm')!=-1:
            links.append(href)
            if href == "/ubuntu/index.htm":
                break
        i = i + 1
    return links

def pdf_downloader(url):
    links=get_all_names(url)
    #print links
    directory = os.getcwd() + "\/tutorialpoint_pdfs";
    make_sure_path_exists(directory)
    for i in range(0,len(links)-1):
        downloadpdf(links[i])

pdf_downloader(url)
