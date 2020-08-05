#include "common.h"

Checker c;

int main() {
	c.validate();
	ensuref(c.N <= 80, "N does not match sub4 bounds");
	ensuref(c.M <= 80, "M does not match sub4 bounds");
	return 0;
}
