package q161989;

// 덧칠하기
// https://school.programmers.co.kr/learn/courses/30/lessons/161989

class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;

        int num = section[0];

        for(int se : section) {
            if(num <= se) {
                num = se + m;
                answer++;
            }
        }

        return answer;
    }
}
