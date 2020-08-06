#include "common.h"

int main() {
	Checker c{}; c.validate();
	ensuref(c.D == c.N, "D != N");
	int ans = solve(c.N, c.M, c.K, c.D, c.B, c.U, c.V);
	ensuref(ans <= 2, "answer > 2");
	return 0;
}
