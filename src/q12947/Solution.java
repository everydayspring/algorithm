package q12947;

// 하샤드 수
// https://school.programmers.co.kr/learn/courses/30/lessons/12947

class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int num = 0;

        String[] strArr = Integer.toString(x).split("");
        for (String s : strArr) {
            num += Integer.parseInt(s);
        }

        if(x % num != 0) {
            answer = false;
        }

        return answer;
    }
}