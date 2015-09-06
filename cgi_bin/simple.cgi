#!/usr/bin/python

import os
import traceback

def Parse_QS(query_string=""):
    qd = query_string.split("&")
    #insert_div(qd)
    qd = list(var_eq_val.split("=") for var_eq_val in qd)
    #insert_div(qd)
    dict={}
    for sublist in qd:
        print("sublist 0 %s sublist 1 %s" %(sublist[0], sublist[1]))
        dict[sublist[0]] = sublist[1]
        print   (type(sublist))
        print(sublist)
    insert_div(dict)
    return dict


def insert_div(content):
    print("<div>Inserting div</div>")
    print("<div>%s</div>" %(content))

def test():
    print("<div>TEST</div>")

print("Content-type:text/html\n\n")

"""

if True:
    insert_div("1")
    Parse_QS("Name=Roger&Occupation=Gardener")
    #test()

else:

"""
try:
    query_string = os.environ["QUERY_STRING"]
    if query_string:
        query_dict = Parse_QS(query_string)
        print("<html>")
        print("<head>")
        print("<title>CGI Test</title>")
        print("</head>")
        print("<body>")
        if query_dict["firstname"].lstrip() != "":
            print("<div>")
            print("Welcome %s!" % (query_dict["firstname"]))
            print("</div>")
        else:
            print("<div>")
            print("You didn't supply a name!")
            print("</div>")
        print("<h2>Favorite color is %s</h2>")

    print("printing path")
    print(query_string)

    print("<div>")
    for entry in os.environ.keys():
        print("<b>%20s</b>: %s <br><br>" % (entry, os.environ[entry]))
    print("</div>")
    print("<h2>Simple CGI test</h2>")
    print("</body>")
    print("</html>")

except Exception:
    print("")
    print(traceback.format_exc())
