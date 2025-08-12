#include <iostream>
#include <vector>
#include <map>

using namespace std;




int main()
{
    vector<int> list;
    int a = 5;
    list.push_back(a);
    list[0] = 0;
    cout << list[0];
    return 0;
}

