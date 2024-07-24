package q120806;

// 두 수의 나눗셈
// https://school.programmers.co.kr/learn/courses/30/lessons/120806

public class
Solution {
    int solution(int num1, int num2) {
        float answer = (float)num1 / (float)num2;
        answer *= 1000;
        return (int)answer;
    }
}
