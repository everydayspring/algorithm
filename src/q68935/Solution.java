package q68935;

// 3진법 뒤집기
// https://school.programmers.co.kr/learn/courses/30/lessons/68935

class Solution {
    public int solution(int n) {
        int answer = 0;
        String str = "";

        while(n >= 1){
            str += Integer.toString(n % 3);
            n = n / 3;
        }

        answer = Integer.parseInt(str,3);

        return answer;
    }
}