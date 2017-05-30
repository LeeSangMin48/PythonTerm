# -*- coding: cp949 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

##### global
xmlFD = -1
MoviesDoc = None


#### xml 관련 함수 구현
def LoadXMLFromFile():
    fileName = str(input("please input file name to load :"))
    global xmlFD, MoviesDoc
    try:
        xmlFD = open(fileName)
    except IOError:
        print("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print("loading fail!!!")
        else:
            print("XML Document loading complete")
            MoviesDoc = dom
            return dom
    return None


def MoviesFree():
    if checkDocument():
        MoviesDoc.unlink()


def PrintDOMtoXML():
    if checkDocument():
        print(MoviesDoc.toxml())


def PrintMovieList(tags):
    global MoviesDoc
    if not checkDocument():
        return None

    movielist = MoviesDoc.childNodes
    movie = movielist[0].childNodes
    for item in movie:
        if item.nodeName == "book":
            subitems = item.childNodes
            for atom in subitems:
                if atom.nodeName in tags:
                    print("title=", atom.firstChild.nodeValue)




def SearchMovieTitle(keyword):
    global MoviesDoc
    retlist = []
    if not checkDocument():
        return None

    try:
        tree = ElementTree.fromstring(str(MoviesDoc.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    movieElements = tree.getiterator("movie")  # return list type
    for item in movieElements:
        strTitle = item.find("title")
        if (strTitle.text.find(keyword) >= 0):
            retlist.append((item.attrib["ISBN"], strTitle.text))

    return retlist


def MakeHtmlDoc(MovieList):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for movieitem in MovieList:
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        ibsnText = newdoc.createTextNode("ISBN:" + movieitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("Title:" + movieitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # line end

    # append Body
    top_element.appendChild(body)

    return newdoc.toxml()


def printMovieList(blist):
    for res in blist:
        print(res)


def checkDocument():
    global MoviesDoc
    if MoviesDoc == None:
        print("Error : Document is empty")
        return False
    return True
