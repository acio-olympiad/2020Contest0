#include <vector>
#include <iostream>

using namespace std;

bool can_do(int L, int K, int D, vector<int> B, vector<vector<int>> edges){
	vector<bool> seen(edges.size());
	vector<int> bfsc, bfsn;
	int cnt = 0;
	seen[1]=1;
	if(B[1] >= L)bfsc.push_back(1),cnt++;
	for(int i = 0; i < D; ++i){
		for(int u: bfsc){
			for(int v: edges[u]){
				if(!seen[v] && B[v] >= L){
					seen[v]=1;
					bfsn.push_back(v);
					cnt++;
				}
			}
		}
		swap(bfsc,bfsn);
		bfsn.clear();
	}
	return cnt >= K;
}

int solve(int N, int M, int K, int D, vector<int> B, vector<int> U, vector<int> V){
	vector<vector<int>> edges(N+1);
	for(int i = 0; i < M; ++i){
		edges[U[i]].push_back(V[i]);
		edges[V[i]].push_back(U[i]);
	}
	int lo=1,hi=1e6+1,mid;
	while(lo!=hi){
		mid=lo+hi>>1;
		if(can_do(mid, K, D, B, edges))lo=mid + 1;
		else hi = mid;
	}
	return lo-1;
}

int N,M,K,D;
vector<int> B,U,V;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin>>N>>M>>K>>D;
    B.resize(N+1);
    U.resize(M);
    V.resize(M);
    for(int i = 1; i <= N; ++i)cin>>B[i];
    for(int i = 0,u,v; i < M; ++i)cin>>U[i]>>V[i];
    cout << solve(N,M,K,D,B,U,V);
}
