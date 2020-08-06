#ifndef COMMON_H
#define COMMON_H
#include "testlib.h"
#include "bounds.h"
using namespace std;

typedef pair<int,int> pii;

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

struct Checker {
	int N, M, K, D;
	vector<int> B{0}, U, V;
	set<pii> edges;
	void validate() {
		registerValidation();
		N = inf.readInt(MIN_N, MAX_N, "N");
		inf.readSpace();
		M = inf.readInt(MIN_M, MAX_M, "M");
		inf.readSpace();
		K = inf.readInt(MIN_K, N, "K");
		inf.readSpace();
		D = inf.readInt(MIN_D, MAX_D, "D");
		inf.readEoln();
		for (int i = 0; i < N; i++) {
			int b_i = inf.readInt(MIN_b_i, MAX_b_i, "b_i");
			B.push_back(b_i);
			if(i!=N-1)inf.readSpace();
		}
		inf.readEoln();
        for(int i = 0; i < M; ++i){
			int u = inf.readInt(1, N, "u");
			inf.readSpace();
			int v = inf.readInt(1, N, "v");
			ensuref(u != v, "u == v, self loop");
			ensuref(!edges.count({u,v}), "Duplicate edge");
			U.push_back(u);
			V.push_back(v);
			edges.insert({u,v});
			edges.insert({v,u});
			inf.readEoln();
		}
		inf.readEof();
	}
};

#endif
