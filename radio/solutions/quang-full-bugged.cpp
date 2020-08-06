#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int n,m,k,d;
vector<int> g[100005];
int bandwidth[100005];
int dist[100005];
bool pushed[100005];


int decision(int x){
    // *** this is the line commented out. Very subtle bug.
    // if (bandwidth[1] < x) return 0;
    for (int i = 1; i <= n; i++){
        dist[i] = 1e9;
        pushed[i] = false;
    }
    queue<int> q;
    q.push(1);
    pushed[1] = true;
    dist[1] = 0;
    while (!q.empty()){
        int cur = q.front();
        q.pop();
        for (int tgt : g[cur]){
            if (pushed[tgt] || bandwidth[tgt] < x) continue;
            pushed[tgt] = true;
            dist[tgt] = dist[cur]+1;
            q.push(tgt);
        }
    }
    int cnt = 0;
    for (int i = 1; i <= n; i++){
        if (dist[i] <= d){
            cnt++;
        }
    }
    return cnt;
}

int main(){
    freopen("radin.txt", "r", stdin);
    freopen("radout.txt", "w", stdout);
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
