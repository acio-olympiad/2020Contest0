#include <cstdio>

int L, W, A, B;

int main() {
	scanf("%d %d %d %d", &L, &W, &A, &B);
	printf("%d\n", (L/A)*(W/B));
}
