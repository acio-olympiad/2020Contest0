#include "common.h"

Checker c;
int main() {
	c.validate();
	for (int i = 2; i <= c.N; i++) {
		ensuref(c.a[i] >= c.a[i-1], "A is not increasing (sub2)");
	}
	return 0;
}
