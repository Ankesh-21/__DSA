#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
class RobinKarp{
public:
    const Prime = 101;
    ll getHash(string s){
        ll hash = 0;
        for (int i = 0; i < s.size();i++){
            hash += s[i] * pow(Prime,i);
        }
        return hash;
    }
    ll updateHash(string s,ll hash,int exclude,int include){
        hash -= s[exclude];
        hash /= pow(Prime,exclude);
        hash += s[include] * pow(Prime,include);

        return hash;
    }
}; 

int main(){
    string a = "abc";
    string b ="abcabcabc";

    RobinKarp Rk = new RobinKarp();
    int i = 0;
    for (int j = 0; j < b.size();j++){
        if (j - i + 1 == a.size()){
            ll b_hash = RK.getHash(b.substr(i,j));
            if (b_hash == a_hash){
                cnt ++;
            }
            RK.updateHash(b,b_hash,i,j);
        }
    }
    cout << cnt << endl;
}
