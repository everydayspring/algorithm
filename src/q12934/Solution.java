package q12934;

// 정수 제곱근 판별
// https://school.programmers.co.kr/learn/courses/30/lessons/12934

class Solution {
    public long solution(long n) {
        long answer = n;

        for(long i = 1; i * i <= n; i++){
            if(i * i == n){
                answer = (i + 1) * (i + 1);
            }
        }
        if(answer == n) answer = -1;

        return answer;
    }
}