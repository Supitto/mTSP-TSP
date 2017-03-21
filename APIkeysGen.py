print "Please insert your Google API Key"
key = raw_input()
f = open("APIkeys.py","w")
f.write("GoogleKey = \""+key+"\"")
f.close()