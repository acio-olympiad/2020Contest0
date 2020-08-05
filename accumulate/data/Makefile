.PHONY: all clean input output

all: input output check zip

input:
	# Put any data generation commands here
	g++ -std=c++14 -o tkgen gen/tkgen.cpp
	python3 gen/gen.py | python3 gen/bootstrap.py
	cp handmade/* .

output: input
	bash ./make-output-py.sh

check: input

zip: input output check
	zip data.zip *.in *.out

clean:
	-rm tkgen
	-rm *.in *.out
	-rm data.zip
