// testcase의 개수를 생각해보고 문제가 크지 않을 시 하나씩 순회하여 해결
// <algorithm>의 sort()를 통해 vector형을 크기순 정렬가능
// -> 연산시간 최소화위해 사용자제
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int cards, M, num, count, answer;
    vector <int> black_jack, sum;
    cin >> cards >> M;
    for(int i = 0; i < cards; i++){
        cin >> num;
        black_jack.push_back(num);
    }
    
    sort(black_jack.begin(), black_jack.end());

    for(int i = 0; i < cards ;i++){
        count+=black_jack.at(i);
        for(int j = i + 1;j < cards;j++){
            count += black_jack.at(j);
                for(int k = j + 1;k < cards;k++){
                //  count += black_jack.at(k);
                 sum.push_back(black_jack.at(i) + black_jack.at(j) + black_jack.at(k));
            }
        }
    }
    sort(sum.begin(), sum.end());
    vector <int>::iterator iter;
    for(iter = sum.begin();  *iter <= M && iter != sum.end(); iter++){
        answer = *iter;
    }
    cout << answer;
    
}