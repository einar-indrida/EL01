#!/bin/sh

# run some sed commands....
# we expect only one argument (for now...)

filename=$1
outfile=new-$1

# backup, just in case.... we overwrite previous backupfiles
cp $filename $filename.bak

cat $filename | sed 's;<br>;\n<br>\n;g' > $outfile

exit 0


•	mynda sjálfstæðar línur pr. málsgrein (split á <br>)
•	Soga ígildi G2M1L3 út úr hverri línu og skipta því líka upp í viðeigandi dálka
•	Koma með tillögu að bókstafa-lyklakerfi byggt á þekkingu hennar á umhverfi laga
•	Skella fremst í sérhverja línu einkvæmu númeri laganna sem textinn er hluti af
•	Skoða og eftir atvikum finna reglu varðandi kaflaheiti 
•	Passa að tína ekki neðanmálsgreinunum sem geyma upplýsingar um breytingar á ákvæðunum
