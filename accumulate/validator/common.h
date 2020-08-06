#ifndef COMMON_H
#define COMMON_H
#include "testlib.h"
#include "bounds.h"

struct Checker {
	int N, K, a[100005];
	void validate() {
		registerValidation();
		N = inf.readInt(MIN_N, MAX_N, "N");
		inf.readSpace();
		K = inf.readInt(MIN_K, N-1, "K");
		inf.readEoln();
		for (int i = 1; i <= N; i++) {
			a[i] = inf.readInt(MIN_A, MAX_A, "a[i]");
			if (i < N) inf.readSpace();
			else inf.readEoln();
		}
		inf.readEof();
	}
};

#endif
