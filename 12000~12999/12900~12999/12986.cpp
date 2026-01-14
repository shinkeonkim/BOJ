/*
[12986: 화려한 마을2](https://www.acmicpc.net/problem/12986)

Tier: Platinum 2 
Category: data_structures, segtree, offline_queries, mo
*/

#include <iostream>
#include <list>
#include <algorithm>

#define KKKK 200000

using namespace std;

int N,K,M,SQRT,ANS,ANS_M,L_1,R_1,L_2,R_2,last;
int A[440000];
int cnt_Mo[440000];
int cnt[440000];
int number_cnt[440000];
int answer[440000];


struct QUERY {
    int l,r,order;
} Q[440000];

bool compare(QUERY a, QUERY b) {
    if(a.l/SQRT < b.l/SQRT) return true;
    else if(a.l/SQRT == b.l/SQRT) {
        if(a.r < b.r) return true;
    }
    return false;
}

void add(int idx) {
    int d = number_cnt[A[idx]];
    cnt[d]--;
    cnt_Mo[d/SQRT]--;
    
    number_cnt[A[idx]]++;
    
    d = number_cnt[A[idx]];
    cnt[d]++;
    cnt_Mo[d/SQRT]++;
}  

void sub(int idx) {
    int d = number_cnt[A[idx]];
    cnt[d]--;
    cnt_Mo[d/SQRT]--;

    number_cnt[A[idx]]--;
    
    d = number_cnt[A[idx]];
    cnt[d]++;
    cnt_Mo[d/SQRT]++;

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
  
    cin >> N;
    if(N==0) return 0;
    cin >> M;
    for(SQRT = 1; SQRT*SQRT <=N; SQRT++);
    for(int x = 1; x <= N; x++) {
        cin >> A[x];
        A[x] += KKKK;
    }
    for(int x=0; x<=N; x++) cnt[x] = cnt_Mo[x]=0;
    int testcase = 0;
    for(int testcase = 0; testcase<M; testcase++) {
        cin >> Q[testcase].l >> Q[testcase].r;
        Q[testcase].order = testcase;
        if(Q[testcase].l > Q[testcase].r) {
            Q[testcase].l ^= Q[testcase].r;
            Q[testcase].r ^= Q[testcase].l;
            Q[testcase].l ^= Q[testcase].r;
        }
    }

    sort(Q,Q+M,compare);

    cnt_Mo[0] = cnt[0] = 430000;
    L_1 = 1;
    R_1 = 1;
    add(1);
    for(int x=0; x<M; x++) {;
        L_2 = Q[x].l;
        R_2 = Q[x].r;
        // cout<<L_2 <<" " << R_2<<"\n";
        while(L_2 < L_1) {
            add(--L_1);
            // cout<<"add "<<L_1<<"\n"; 
        }
        while(R_1 < R_2) {
            add(++R_1);
            // cout<<"add "<<R_1<<"\n";
        }
        while(L_1 < L_2) {
            sub(L_1++);
            // cout<<"sub "<<L_1-1<<"\n";
        }
        while(R_2 < R_1) {
            sub(R_1--);
        }
        
        ANS_M = (N+1)/SQRT;
        while(cnt_Mo[ANS_M] == 0) ANS_M--;
        ANS = min(N,SQRT*(ANS_M+1));
        while(cnt[ANS] == 0) ANS--;
        answer[Q[x].order]=ANS;
        
        L_1 = Q[x].l;
        R_1 = Q[x].r;
    }
    for(int x=1; x<=N; x++) number_cnt[A[x]] = 0;
    for(int x=0; x<M; x++) {
        cout<<answer[x]<<"\n";
    }
    

}