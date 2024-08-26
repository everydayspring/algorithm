package q161990;

class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {50, 50, 0, 0};

        for (int i = 0; i < wallpaper.length; i++) {
            String[] sub = wallpaper[i].split("");
            for (int j = 0; j < sub.length; j++) {
                if (sub[j].equals("#")) {
                    if (i < answer[0]) {
                        answer[0] = i;
                    }
                    if (j < answer[1]) {
                        answer[1] = j;
                    }
                    if (i + 1 > answer[2]) {
                        answer[2] = i + 1;
                    }
                    if (j + 1 > answer[3]) {
                        answer[3] = j + 1;
                    }
                }
            }
        }
        return answer;
    }
}