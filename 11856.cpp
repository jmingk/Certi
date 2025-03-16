// Samsung Expert sw Academy No.11856

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
 
using namespace std;
 
int main() {
 
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
 
 
    int T = 0;
    int tc = 0;
 
 
    cin >> T;
 
    for (tc = 0; tc < T; tc++) {
        string str; 
        cin >> str;
        sort(str.begin(), str.end());
        if (str[0] == str[1] && str[1] != str[2] && str[2] == str[3]) {
            cout << "#" << tc + 1 << ' ' << "Yes" << '\n';
        }
        else cout << "#" << tc + 1 << ' ' << "No" << '\n';
    }
     
 
    return 0;
}
