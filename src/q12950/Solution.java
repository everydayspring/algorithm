package q12950;

// 햏렬의 덧셈
// https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=java

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = arr1;

        for(int i = 0; i < arr1.length; i++) {
            for(int j = 0; j < arr1[0].length; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }
}