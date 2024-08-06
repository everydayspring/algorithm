package q12901;

// 2016년
// https://school.programmers.co.kr/learn/courses/30/lessons/12901

class Solution {
    public String solution(int a, int b) {
        String[] answer = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        int[] month = {4, 0, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3};

        return answer[(b + month[a-1]) % 7];
    }
}