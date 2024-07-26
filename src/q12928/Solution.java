package q12928;

// 약수의 합
// https://school.programmers.co.kr/learn/courses/30/lessons/12928

class Solution {
    public int solution(int n) {
        int answer = 0;

        for(int i = 1; i * i <= n; i++){
            if(i * i == n) {
                answer += i;
            } else if (n % i == 0){
                answer += i;
                answer += (n / i);
            }
        }
        return answer;
    }
}