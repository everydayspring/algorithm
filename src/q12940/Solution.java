package q12940;

// 최대공약수와 최소공배수
// https://school.programmers.co.kr/learn/courses/30/lessons/12940

class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];


        for(int i = n; i >= 1; i--) {
            if(n % i == 0 && m % i == 0) {
                answer[0] = i;
                break;
            }
        }
        answer[1] = n * m / answer[0];


        return answer;
    }
}