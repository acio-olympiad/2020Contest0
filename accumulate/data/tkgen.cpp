#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N,K,SB;
    cin >> N >> K >> SB;
    if (SB == 1) {assert(K == 1);}
    if (SB == 3) {assert(N <= 1000);}
    if (SB == 4) {assert(K == N-1);}
    vector <int> Vals;
    for (int i=0; i<N; i++) {
        Vals.push_back((rand()-RAND_MAX/2)%100000);
    }
    if (SB == 2) {
        sort(Vals.begin(), Vals.end());
    }
    printf("%d %d\n",N,K);
    for (int i=0; i<N; i++) {
        printf("%d",Vals[i]);
		if (i < N-1) printf(" ");
    }
	printf("\n");
}
