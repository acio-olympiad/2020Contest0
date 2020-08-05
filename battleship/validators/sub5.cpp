#include "common.h"

Checker c;

int main() {
	c.validate();
	ensuref(c.N <= 200, "N does not match sub5 bounds");
	ensuref(c.M <= 200, "M does not match sub5 bounds");
	return 0;
}
