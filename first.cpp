#include<bits/stdc++.h>
#define ll long long int 
#define pb push_back
using namespace std;
vector< ll > vec[27];
int main()
{
	string s;
	cin>>s;
	ll i,j,k,l=s.length();
	for(i=0;i<l;i++)
	{
		vec[int(s[i])-97].pb(i+1);
	}
	for(i=0;i<26;i++)
	{
		sort(vec[i].begin(),vec[i].end);
	}
	for(i=0;i<26;i++){
		for(j=0;j<vec[i].size();j++){
			for(k=0;k<26;k++){
				
			}
		}
	}
}