
#include <cstdio>
#include <cstdlib>
#include <time.h>
#include <set>
#include <utility>
#include <queue>
#include <vector>
using namespace std;
int n,m,k,d;
vector<int> g[100005];
int bandwidth[100005];
int dist[100005];
bool pushed[100005];


// taken from full to determine the actual value of k- make the test a little stronger
int decision(int x){
    if (bandwidth[1] < x) return 0;
    // printf("%d\n", bandwidth[1]);
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


typedef pair<int,int> pii;
vector<pii> final_edges;
set<pii> all_edges;

// one line: 
/*
subtask
max_bandwidth
disconnect_starting_node - boolean, if true, starting node is disconnected (10% of cases)
high_starting_node_bandwidth - boolean, if true, starting node's bandwidth is max_bandwidth (10% of cases)
bump_k_target - boolean, if true, then once a stronger K is determined, it will increment K if possible (50% of cases)
n
m
k - will bump up this value to a stronger value
d
*/

int main() {
    // freopen("test.in", "r", stdin);
    srand(time(NULL)); 
    int subtask;
    int max_bandwidth;
    int disconnect_starting_node;
    int high_starting_node_bandwidth;
    int bump_k_target;
    scanf("%d %d %d %d %d", &subtask, &max_bandwidth, &disconnect_starting_node, &high_starting_node_bandwidth, &bump_k_target);
    scanf(" %d %d %d %d", &n, &m, &k, &d);
    // printf("%d %d\n",subtask, max_bandwidth);
    // printf("????");
    // generate the edges
    if (!disconnect_starting_node){
        for (int i = 2; i <= min(n,m+1); i++){
            int a = rand() % (i-1);
            a++;
            final_edges.push_back({a,i});
            all_edges.insert(make_pair(a,i));
            all_edges.insert(make_pair(i,a));
            g[a].push_back(i);
            g[i].push_back(a);
        }
    }
    
    while (final_edges.size() < m){
        int a = rand() % n + 1;
        int b = rand() % n + 1;
        if (b == a || all_edges.find(make_pair(a,b)) != all_edges.end()) continue;
        if (disconnect_starting_node && (a == 1 || b == 1)) continue;
        all_edges.insert(make_pair(a,b));
        all_edges.insert(make_pair(b,a));
        final_edges.push_back({a,b});
        g[a].push_back(b);
        g[b].push_back(a);
    }
    for (int i = 1; i <= n; i++){
        bandwidth[i] = rand() % max_bandwidth + 1;
    }
    if (high_starting_node_bandwidth){
        bandwidth[1] = 1;
    }
    else{
        bandwidth[1] = max_bandwidth;
    }

    int lo = 0;
    int hi = 1000000;
    int best = 0;
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
    if (disconnect_starting_node){
        // eh do stuff, keep original k
    }
    else{
        k = decision(best);
        if (bump_k_target){
            k = min(k+1,n);
        }
    }

    // printf("%d\n", best);
    printf("%d %d %d %d\n", n, m, k, d);
    printf("%d ", bandwidth[1]);
    for (int i = 2; i <= n; i++){
        printf(" %d", bandwidth[i]);
    }
    printf("\n");
    for (pii cur : final_edges){
        printf("%d %d\n", cur.first, cur.second);
    }
}
