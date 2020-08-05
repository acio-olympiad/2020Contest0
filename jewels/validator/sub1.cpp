#include "common.h"

int main() {
	Checker c{}; c.validate();
	ensuref(c.N == 4, "N does not match sub1 bounds");
	return 0;
}
