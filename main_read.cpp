#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
    int M;
    double score1, score2, sum, avg;
    string stuName;
    ifstream ifs;


    ifs.open("students.txt");


    if (!ifs)
    {
        cout << "Error opening file" << endl;
        exit(0);
    }


    ifs >> M;
    cout << "Total " << M << " students" << endl;


    for (int i = 0; i < M; i++)
    {
        ifs >> stuName >> score1 >> score2;
        sum = score1 + score2;
        avg = sum / 2.0;
        cout << "Student Name: " << stuName
             << " score1: " << score1
             << " score2: " << score2
             << " Sum: " << sum
             << " Avg: " << avg << endl;
    }
    ifs.close();
    return 0;
}