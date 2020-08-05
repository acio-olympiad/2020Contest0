#ifndef COMMON_H
#define COMMON_H
#include "testlib.h"
#include "bounds.h"
using namespace std;

struct Checker {
	int N, M, K;
	int grid[1005][1005];
	void validate() {
		registerValidation();
		N = inf.readInt(MIN_N, MAX_N, "N");
		inf.readSpace();
		M = inf.readInt(MIN_M, MAX_M, "M");
		inf.readSpace();
		K = inf.readInt(MIN_K, MAX_K, "K");
		inf.readEoln();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				grid[i][j] = inf.readInt(MIN_A, MAX_A, "a[i][j]");
				if (j < M-1) inf.readSpace();
				else inf.readEoln();
			}
		}
		inf.readEof();
	}
};
#endif
