#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.L <= 5 && c.W <= 5, "L or W does not match sub4 bounds");
	return 0;
}
