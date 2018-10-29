import json

def formatdata(string):
    string = string.replace(";", " or ")
    string = string.replace("\text{}", "")
    #string = string.replace("\frac", " or ")
    

    return string


f = open("data.txt", "r")
jsontxt = f.read()
jsonstuff = jsontxt.decode("utf-8", "ignore")
jsonstuff = jsonstuff.encode('ascii', 'ignore')
datastore = json.loads(str(jsonstuff))
f.close()

print "Title is: " + datastore["data"].get("title")
print "There are %s marks." % datastore["data"].get("marks")

qunumb = 1
for quest in datastore["data"]["questions"]:
    print "Question %s:" % qunumb
    qunumb += 1
    #Calc allowed?
    if type(quest.get("calculator")) == type(None):
        print "Calculator not allowed"
    else:
        print "Calculator allowed"
    
    print "Marks for question: " + str(quest.get("marks"))

    #Get answer data
    try:
        anspart = 1
        for ansdata in quest["answer"]:
            print "Answer part %s:" % anspart
            print "Marks are: %s " % ansdata.get("marks") 
            print "Type of question is %s" % ansdata.get("type")
            if type(ansdata["text"]).__name__ == "list":
                for x in ansdata["text"]:
                    output = x.get("text")
                    output = output.split("\n")
                    for toprint in output:
                        if "marks=0" in toprint:
                            pass
                        else:
                            print "Answer is : " + formatdata(toprint)    
                      
            else:
                toprint = str(ansdata["text"])
                print "Answer is: " + formatdata(toprint)
            anspart += 1
    except AttributeError:
        pass