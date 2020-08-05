#ifndef COMMON_H
#define COMMON_H
#include "testlib.h"
#include "bounds.h"
using namespace std;

struct Checker {
	int N, A, B;
	vector<int> skills;
	void validate() {
		registerValidation();
		N = inf.readInt(MIN_N, MAX_N, "N");
		inf.readSpace();
		A = inf.readInt(MIN_A, MAX_A, "A");
		inf.readSpace();
		B = inf.readInt(A, MAX_A, "B");
		inf.readEoln();
		for (int i = 0; i < N; i++) {
			int s_i = inf.readInt(MIN_SKILL, MAX_SKILL, "s_i");
			skills.push_back(s_i);
			if(i!=N-1)inf.readSpace();
		}
		inf.readEoln();
		inf.readEof();
	}
};

#endif
