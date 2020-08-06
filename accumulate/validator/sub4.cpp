#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.K == c.N-1, "K does not adhere to sub4 bounds");
	return 0;
}
