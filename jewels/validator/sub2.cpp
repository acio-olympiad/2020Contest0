#include "common.h"
#include <algorithm>

int main() {
	Checker c{}; c.validate();
	bool prev_red = c.S.back() == 'r' && c.N > 1;
	for(int i = 0; i < c.N; ++i){
		if(c.S[i] == 'r'){
			ensuref(!prev_red, "Adjacent red beads");
			prev_red = true;
		}else 
			prev_red = false;
	}
	ensuref(count(c.S.begin(), c.S.end(), 'r') == 2, "There are not 2 red beads");
	return 0;
}
