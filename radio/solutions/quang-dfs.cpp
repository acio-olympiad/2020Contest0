// should only get subtasks 1-3

#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int n,m,k,d;
vector<int> g[100005];
int bandwidth[100005];
int dist[100005];
bool seen[100005];

void dfs( int pos, int cur_depth,int x){
    seen[pos] = true;
    dist[pos] = cur_depth;
    if (cur_depth == d) return;
    for (int tgt : g[pos]){
        if (bandwidth[tgt] >= x && !seen[tgt]){
            dfs(tgt,cur_depth+1,x);
        }
    }
}

int decision(int x){
    if (bandwidth[1] < x) return 0;
    for (int i = 1; i <= n; i++){
        dist[i] = 1e9;
        seen[i] = false;
    }
    dfs(1,0,x);
    int cnt = 0;
    for (int i = 1; i <= n; i++){
        cnt += seen[i];
    }
    return cnt;
}

int main(){
    scanf("%d %d %d %d", &n,&m,&k,&d);
    for (int i =1 ; i <= n; i++){
        scanf("%d", &bandwidth[i]);
    }
    for (int i = 1; i <= m; i++){
        int a,b;
        scanf("%d %d", &a, &b);
        g[a].push_back(b);
        g[b].push_back(a);
    }
    int best = 0;
    int lo = 0;
    int hi = 1000000;
    while (lo <= hi){ 
        int mid = (lo + hi)/2;
        if (decision(mid) >= k){
            best = mid;
            lo = mid + 1;
        }
        else{
            hi = mid - 1;
        }
    }
    printf("%d\n", best);
}
