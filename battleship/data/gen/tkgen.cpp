#include <iostream>
using namespace std;
int LD[20]={1,10,100,1000,1000,10000,10000,10000,10000,100000,100000,100000,100000,100000,100000,100000,100000};

int logrand() {
    int low = LD[rand()%15];
    return(rand()%(low*9) + low);
}

int rng(int l, int r) {
    return(rand()%(r-l+1) + l);
}

int main() {
    srand(time(NULL)); //reseed by input?
    int N,M, K, type; //which type of rand
    cin >> N >> M >> K >> type;
    printf("%d %d %d\n",N,M,K);
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=M; j++) {
            if (type) { //type = 1 implies logrand
                printf("%d",logrand());
            } else {
                printf("%d",rng(0,1000000));
            }
			if (j < M) printf(" ");
        }
        printf("\n");
    }
}
