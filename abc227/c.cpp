#include <iostream>
#include <cmath>       

using namespace std;

int main(){
    long long N;
    long long ans;
    ans = 0;
    cin >> N;
    for (int i = 1; i <= pow(N, 1.0 / 3.0);i++){
        long long tmp;
        tmp = int(N / i);
        for (int j = i; j <= pow(N,1.0/2.0);j++){
            int c_max = tmp / j;
            ans = ans + c_max - j + 1;
        }
    }
    cout << ans << endl;
    return 0;
}
