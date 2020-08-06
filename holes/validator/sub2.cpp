#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.A == 1 && c.B == 1, "A or B does not match sub2 bounds");
	return 0;
}
