package q82612;

// 부족한 금액 계산하기
// https://school.programmers.co.kr/learn/courses/30/lessons/82612

class Solution {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long priceAll = 0;

        for(int i = 1; i <= count; i++) {
            priceAll += price * i;
        }
        if(priceAll > money) {
            answer = priceAll - money;
        }

        return answer;
    }
}