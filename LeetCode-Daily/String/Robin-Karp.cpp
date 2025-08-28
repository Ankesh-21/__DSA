#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
class RobinKarp{
    const int Prime = 101;
    ll getHash(string s){
        ll hash = 0;
        for (int i = 0; i < s.size();i++){
            hash += (s[i] - 'a' + 1) * pow(Prime,i);
        }
        return hash;
    }
public:
    ll updateHash(string s,ll hash,int exclude,int include,string &a){
        if (exclude != -1){
            hash -= (s[exclude]-'a' + 1);
            hash /= pow(Prime,exclude);
        }
        hash += (s[include]-'a' + 1) * pow(Prime,a.size() - 1);

        return hash;
    }
    ll myHash(string a){
        return getHash(a);
    }
}; 

int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    string a = "abc";
    string b ="abcabcabc";

    RobinKarp *rk = new RobinKarp();
    ll Hash_a = rk->myHash(a);
    cout << "A string hash value: "<<Hash_a<<endl;
    int cnt = 0;
    int i = 0;
    ll Hash = 0;
    for (int j = 0; j < b.size();j++){
        if (j -i + 1 > a.size()){
            cout<<"Current Hash value: "<<Hash<<endl;
            // Hash = updateHash(b,Hash,-1,j);
            if (Hash == Hash_a){
                cnt += 1;
            }
            // i += 1;
            Hash = rk->updateHash(b,Hash,i,j,a);
            i += 1;
        }
        else{
            Hash = rk->updateHash(b,Hash,-1,j,a);
        }
    }
    cout << cnt << endl;
}
