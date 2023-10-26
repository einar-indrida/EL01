#!/usr/bin/python3

import sys
import os
import re

file = open(sys.argv[1], "rb")
# outfile = os.open("new-" + sys.argv[1], "w")

lines = file.readlines()

g_regex = re.compile('id="(G[^"]*")')

for i in lines:
    new_line = str(i)
    new_line.replace("<br>", "<br>\n")
    # do we have a 'id="G[^"]*' ?
    #	if yes, grab the G L M sections, if they are there...
    # do we have a <b>.*kafli</b>
    # do we have a <b>.*þáttur</b>

    g_line = g_regex.match(new_line)
    if g_line:
        print("match - g_line: (" + str(g_line.expand) + ")\n")
#     print("g_line: " + g_line + "\n")

    print("line: " + new_line)

sys.exit(0)


# 
# 
# X	mynda sjálfstæðar línur pr. málsgrein (split á <br>)
# •	Soga ígildi G2M1L3 út úr hverri línu og skipta því líka upp í viðeigandi dálka
# •	Koma með tillögu að bókstafa-lyklakerfi byggt á þekkingu hennar á umhverfi laga
# •	Skella fremst í sérhverja línu einkvæmu númeri laganna sem textinn er hluti af
# •	Skoða og eftir atvikum finna reglu varðandi kaflaheiti 
# •	Passa að tína ekki neðanmálsgreinunum sem geyma upplýsingar um breytingar á ákvæðunum
