default: show

SRC=2018-04-05_BCP_talk

edit:
	atom $(SRC).py

html:
	python3 $(SRC).py $(SRC).html

page:
	python3 $(SRC).py
	cat /tmp/wiki.txt |pbcopy
	open https://URL.net/cgi-bin/index.cgi/Presentations/$(SRC)?action=edit

show: html
	open -a safari $(SRC).html

github:
	git commit -am' adding notes'
	git push
