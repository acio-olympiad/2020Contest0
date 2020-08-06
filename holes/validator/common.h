#ifndef COMMON_H
#define COMMON_H
#include "testlib.h"
#include "bounds.h"
using namespace std;

struct Checker {
	int L, W, A, B;
	void validate() {
		registerValidation();
		L = inf.readInt(MIN_L, MAX_L, "L");
		inf.readSpace();
		W = inf.readInt(MIN_W, MAX_W, "W");
		inf.readEoln();
		A = inf.readInt(MIN_A, L, "A");
		inf.readSpace();
		B = inf.readInt(MIN_B, W, "B");
		inf.readEoln();
		inf.readEof();
	}
};


#endif
