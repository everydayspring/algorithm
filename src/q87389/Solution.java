package q87389;

// 나머지가 1이 되는 수 찾기
// https://school.programmers.co.kr/learn/courses/30/lessons/87389

class Solution {
    public int solution(int n) {
        int answer = 0;

        int i = 1;

        while(answer == 0) {
            if(n % i == 1) {
                answer = i;
            }
            i++;
        }

        return answer;
    }
}