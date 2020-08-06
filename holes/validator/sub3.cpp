#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.W == 1, "W does not match sub3 bounds");
	return 0;
}
