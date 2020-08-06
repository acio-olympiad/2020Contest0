.PHONY: all clean input output

all: input output check zip

input:
	# Put any data generation commands here
	g++ -std=c++14 -o casegen gen/casegen.cpp
	python3 gen/gen.py | python3 gen/bootstrap.py
	cp handmade/* .

output: input
	bash ./make-output.sh

check: input

zip: input output check
	zip data.zip *.in *.out

clean:
	-rm casegen
	-rm *.in *.out
	-rm data.zip
