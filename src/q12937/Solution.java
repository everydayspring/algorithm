package q12937;

// 짝수와 홀수
// https://school.programmers.co.kr/learn/courses/30/lessons/12937

class Solution {
    public String solution(int num) {
        String answer = "Odd";

        if(num % 2 == 0) {
            answer = "Even";
        }

        return answer;
    }
}
