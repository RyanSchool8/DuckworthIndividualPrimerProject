#!/usr/bin/python

import os
import traceback

def Parse_QS(query_string=""):
    qd = query_string.split("&")
    qd = (var_eq_val.split("=") for var_eq_val in qd)
    dict={}
    for sublist in qd:
        dict[sublist[0]] = sublist[1]
    return dict


def insert_div(content):
    print("<div>Inserting div</div>")
    print("<div>%s</div>" %(content))

print("Content-type:text/html\n\n")

try:
    query_string = os.environ["QUERY_STRING"]
    if query_string:
        query_dict = Parse_QS(query_string)
        print("<html>")
        print("<header></header>")
        print("<head>")
        print("<title>CGI Test</title>")
        print('<link rel="stylesheet" type="text/css" href="../style.css">')
        print("</head>")
        print("<body>")
        if query_dict["firstname"].lstrip() != "":
            print("<h2>")
            print("Welcome %s!" % (query_dict["firstname"]))
            print("</h2>")
        else:
            print("<h2>")
            print("You didn't supply a name!")
            print("</h2>")
        print("<div>")
        print("You have stated that you are %s." %(query_dict["gender"]))
        #for entry in os.envir      on.keys():
        #    print("<b>%20s</b>: %s <br><br>" % (entry, os.environ[entry]))
        print("</div>")
        print("<div>")
        if query_dict["gender"] == "male":
            print('<img src="../images/male.jpg" alt="Male Gender Symbol" style="width:320px">')
        else:
            print('<img src="../images/female.jpg" alt="Female Gender Symbol" style="width:235px">')
        print("</div>")
        if query_dict["sports"] == "yes":
            print("<h3> You have indicated you like sports, so here is a half-time show from everyone's favorite talking sponge!</h3>")
            print('<iframe width="560" height="315" src="https://www.youtube.com/embed/2K6S0LHeG8k" frameborder="0" allowfullscreen></iframe>')
        else:
            print("<h3> You have indicated you are not partial to sports, so here is a Bob Ross video!</h3>")
            print('<iframe width="420" height="315" src="https://www.youtube.com/embed/pw5ETGiiBRg" frameborder="0" allowfullscreen></iframe>')
            print('<div>And remember: "We don\'t make mistakes; we just have happy accidents."<br>- Bob Ross</div>')
        print("</body>")
        print("<footer></footer>")
        print("</html>")

except Exception:
    print("")
    print(traceback.format_exc())
