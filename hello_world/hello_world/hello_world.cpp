#include<iostream>
#include<vector>
using namespace std;
int main()
{
	cout << "Hello, World!" << endl;
	vector<int> v{ 1, 2, 3, 4, 5 };
	for(auto it=v.begin(); it!=v.end(); ++it)
	{
		cout << *it << " ";
	}
	cout << endl << endl;
	return 0;
}