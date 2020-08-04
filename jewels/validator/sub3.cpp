#include "common.h"

int main() {
	Checker c{}; c.validate();
	ensuref(c.N <= 1000, "N does not match sub3 bounds");
	return 0;
}
