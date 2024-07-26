package q120831;

// 짝수의 합
// https://school.programmers.co.kr/learn/courses/30/lessons/120831

class Solution {
    public int solution(int n) {
        int answer = 0;

        for(int i  = 2; i <= n; i+=2){
            answer += i;
        }
        return answer;
    }
}
