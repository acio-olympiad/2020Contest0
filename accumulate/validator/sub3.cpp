#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.N <= 1000, "N does not adhere to sub3 bounds");
	return 0;
}
