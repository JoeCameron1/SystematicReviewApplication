def main(query,sort,number):

        import urllib
        import sys
        import webbrowser

        def convertQuery(query):        #replaces spaces in a string with "+"'s so the string will be suitable for use in a url
            output = ""
            for i in query:
                if i == " ":
                    output += "+"
                else:
                    output += i
            return output

        def searchURL(query,sort,number):           #takes a query, sort type, and number of articles to create a url leading to a list of ID's
            nurl = "esearch.fcgi?db=PubMed&retmax=" + number + "&sort=" + sort + "relevance&term=" + query
            return nurl

        def fetchURL(id):                           #takes a pubmed document ID and creates the url that leads to the document
            nurl = "efetch.fcgi?db=PubMed&id="
            nurl += str(id)
            nurl += "&rettype=fasta&retmode=text"
            return nurl

        def removeBrackets(inp):        #removes anything between and including < > brackets
            out = ""                    #allows processing of the html
            add = 1
            for c in inp:
                if c == "<":
                    add = 0
                elif c == ">":
                    add = 1
                elif add == 1:
                    out += c
            return out
                    
        
        query = convertQuery(query)

        url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"       #base url that all PubMed interaction goes through
        page = urllib.urlopen(url + searchURL(convertQuery(query),sort,number))     #opens page for given query and sets it to 'page' variable
        source = page.read()            #reads the page as a string into a 'source' variable
        page.close()                    #closes the page
        idListStart = source.find("IdList") + 8             #Finds the beginning of the list of ID's
        idListEnd = source.find("</IdList>")                #Finds the end of the list of ID's
        idList = removeBrackets(source[idListStart:idListEnd]).split()  #Removes brackets for the string containing the ID list, and splits into a list of each ID

        urlList = []
        for u in idList:                #generates a new list containing each ID's respective url
            urlList += [fetchURL(u)]
        docList = []
        for s in urlList:               #opens each url, and prints the text on it
            p = urllib.urlopen(url + s)
            source = p.read()
            p.close
            docList += [source]
        return docList

