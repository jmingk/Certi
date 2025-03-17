//2027 Samsung expert academy 

using namespace std;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T, n;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            cin >> n;
            if (n % 2 == 1) sum += n;
        }
        cout << "#" << tc << " " << sum << "\n";
    }
    return 0;
}
