#include "common.h"

Checker c;

int main() {
	c.validate();
	ensuref(c.N == 1, "N does not match sub1 bounds");
	return 0;
}
