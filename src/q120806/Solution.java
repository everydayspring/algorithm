package q120806;

// 두 수의 나눗셈
// https://school.programmers.co.kr/learn/courses/30/lessons/120806

class Solution {
    public int solution(int num1, int num2) {
        double answer = 0;

        answer = (double) num1 / (double) num2;
        answer *= 1000;

        return (int)answer;
    }
}