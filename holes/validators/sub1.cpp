#include "common.h"

Checker c;
int main() {
	c.validate();
	ensuref(c.L == 12 && c.W == 8 && c.A == 5 && c.B == 2, "This input is not subtask 1");
	return 0;
}
