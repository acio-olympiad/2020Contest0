#include "common.h"
#include <algorithm>

int main() {
	Checker c{}; c.validate();
	for(int i = 0; i < c.N; ++i){
		ensuref(c.skills[i] == i + 1, "s_i != i");
	}
	return 0;
}
