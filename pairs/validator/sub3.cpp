#include "common.h"

int main() {
	Checker c{}; c.validate();
	ensuref(c.B == MAX_A, "B does not match sub3 bounds");	
	return 0;
}
