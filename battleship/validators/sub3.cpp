#include "common.h"

Checker c;

int main() {
	c.validate();
	ensuref(c.N <= 30, "N does not match sub3 bounds");
	ensuref(c.M <= 30, "M does not match sub3 bounds");
	return 0;
}
