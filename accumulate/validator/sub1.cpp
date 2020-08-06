#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.K == 1, "K = 1 not maintained (sub1)\n");
	return 0;
}
