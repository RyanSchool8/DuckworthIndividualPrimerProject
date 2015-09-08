#!/usr/bin/python

import os
import traceback
import urllib,urllib2

def Parse_QS(query_string=""):
    qd = query_string.split("&")
    qd = (var_eq_val.split("=") for var_eq_val in qd)
    dict={}
    for sublist in qd:
        dict[sublist[0]] = sublist[1]
    return dict


def insert_div(content):
    print('<div>%s</div><br>' %(content))

def navigate_to_index():
    print('<a href="../index.html">Click here to navigate back to the index.html file</a></td>')

print("Content-type:text/html\n\n")
print("<html>")
print("<header></header>")
print("<head>")
print("<title>CGI Test</title>")
print('<link rel="stylesheet" type="text/css" href="../stylesheets/style.css">')
print("</head>")
print("<body>")

try:

    query_string = os.environ["QUERY_STRING"]
    if query_string:

        query_dict = Parse_QS(query_string)

        #for entry in os.environ.keys():
        #    print("<b>%20s</b>: %s <br><br>" % (entry, os.environ[entry]))

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

        if query_dict["remote"] == "yes":
            #NOTE: All data used in this section is retrieved from https://public.opencpu.org/ocpu/library/ and is used for educational purposes only.
            response = urllib2.urlopen('https://public.opencpu.org/ocpu/library/')

            #respons_info = response.info()
            data = response.read()
            #print(type(data))
            data = data.split("\n")
            #print(data)
            print('<h4>Here is the remote data that was requested:</h4><br>')
            for num in range(0,5):
                insert_div(data[num])
            response.close()
        else:
            print("<br><br>")
            insert_div("No remote data requested!")
        print("</body>")
        print("<footer></footer>")
        print("</html>")

    else:
        print('<h1>There is no query string! This CGI script requires one.</h1>')
        navigate_to_index()
        print("</body>")
        print("<footer></footer>")
        print("</html>")

except Exception:
    insert_div("Error parsing the query string!")
    navigate_to_index()
    #print(traceback.format_exc())
    print("</body>")
    print("<footer></footer>")
    print("</html>")