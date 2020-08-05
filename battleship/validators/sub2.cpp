#include "common.h"

Checker c;

int main() {
	c.validate();
	ensuref(c.N == c.M && c.M == c.K, "N, M, K are not equal (sub2)");
	return 0;
}
