#ifndef COMMON_H
#define COMMON_H
#include "testlib.h"
#include "bounds.h"
using namespace std;

struct Checker {
	int N;
	string S;
	void validate() {
		registerValidation();
		N = inf.readInt(MIN_N, MAX_N, "N");
		inf.readEoln();
		for (int i = 0; i < N; i++) {
			char c = inf.readChar();
			ensuref(c == 'r' || c == 'b', "Unknown bead colour, must be either 'r' or 'b");
			S.push_back(c);
		}
		inf.readEoln();
		inf.readEof();
	}
};

#endif
