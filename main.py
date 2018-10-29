import json
#Get the json data in the correct form
f = open("data.txt", "r")
jsontxt = f.read()
jsonstuff = jsontxt.decode("utf-8", "ignore")
jsonstuff = jsonstuff.encode('ascii', 'ignore')
datastore = json.loads(str(jsonstuff))
f.close()
#Create a file to write to.
filename = datastore["data"].get("title").replace(".","-")
print filename
output = open(filename+".txt", "w")
output.write("")
output.close()
output = open(filename+".txt", "a")
#Print each answer block
numb = 0
print "There is " + str(len(datastore["data"]["questions"])) + " questions in this assignment."
for x in datastore["data"]["questions"]:
    #loops for each question
    numb += 1
    output.write("Question number is: " + str(numb) + "\n")
    numbq = 0
    for z in x["answer"]:
        numbq += 1
        output.write("     Question part #"+str(numbq)+":" + "\n")
        try:
            ans = z.get("text")
            anstype = type(ans).__name__

            if anstype == "list":
                #do stuff to get the text out of this
                for y in ans:
                    ans2 = y.get("text")
                    ans2 = ans2.split("\n")
                    for w in ans2:
                        if "marks=0" in ans2:
                            pass
                        else:
                            output.write("         Answer is: " + w + "\n")
            elif anstype == "unicode":
                ans = ans.replace(";", " or ")
                output.write("         Answer is: "+ ans + "\n")
        except:
            pass
    output.write("\n")
output.close()