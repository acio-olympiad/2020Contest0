#include "common.h"

int main() {
	Checker c{}; c.validate();
	ensuref(c.D == c.N, "D != N");
	ensuref(c.N <= 1000, "N does not match sub3 bounds");
	ensuref(c.M <= 1000, "M does not match sub3 bounds");
	return 0;
}
