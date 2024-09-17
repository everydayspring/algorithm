package q12916;

// 문자열 내 p와 y위 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/12916

class Solution {
    boolean solution(String s) {
        int pCnt = 0;
        int yCnt = 0;

        int leng = s.length();
        int leng2 = s.replace("p", "").replace("P", "").length();

        pCnt = leng - leng2;

        leng2 = s.replace("y", "").replace("Y", "").length();

        yCnt = leng - leng2;

        if(pCnt != yCnt) return false;

        return true;
    }
}
