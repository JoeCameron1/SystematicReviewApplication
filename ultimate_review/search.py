import urllib
import sys
import webbrowser
def convertQuery(query):
    output = ""
    for i in query:
        if i == " ":
            output += "+"
        else:
            output += i
    return output

def searchURL(query):
    nurl = "esearch.fcgi?db=PubMed&sort=relevance&term=" + query
    return nurl

def fetchURL(id):
    nurl = "efetch.fcgi?db=PubMed&id="
    nurl += str(id)
    nurl += "&rettype=fasta&retmode=text"
    return nurl

def removeBrackets(inp):
    out = ""
    add = 1
    for c in inp:
        if c == "<":
            add = 0
        elif c == ">":
            add = 1
        elif add == 1:
            out += c
    return out
            

query = sys.argv[1]
query = convertQuery(query)

url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
page = urllib.urlopen(url + searchURL(convertQuery(query)))
print url + searchURL(convertQuery(query))
source = page.read()
page.close()
idListStart = source.find("IdList") + 8
idListEnd = source.find("</IdList>")
idList = removeBrackets(source[idListStart:idListEnd]).split()

urlList = []
for u in idList:
    urlList += [fetchURL(u)]
for s in urlList:
    p = urllib.urlopen(url + s)
    source = p.read()
    p.close
    print source

