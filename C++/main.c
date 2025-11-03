#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> computeNext(const string& p) {
int m = p.length();
vector<int> next(m, 0);
int j = 0;

for (int i = 1; i < m; i++) {
while (j > 0 && p[i] != p[j]) {
j = next[j - 1];
}

if (p[i] == p[j]) {
j++;
}

next[i] = j;
}
return next;
}

int main() {
    string s, p;
    cin >> s >> p;

    int n = s.length();
    int m = p.length();

    if (m > n) {
        cout << "no" << endl;
        return 0;
    }

    if (m == 0) {
        cout << 1 << endl;
        return 0;
    }

    vector<int> next = computeNext(p);

    int j = 0;
    for (int i = 0; i < n; i++) {

        while (j > 0 && s[i] != p[j]) {
            j = next[j - 1];
        }

        if (s[i] == p[j]) {
            j++;
        }

        if (j == m) {
            cout << (i - m + 2) << endl;
            return 0;
        }
    }

    cout << "no" << endl;

    return 0;
}
