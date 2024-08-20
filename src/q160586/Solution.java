package q160586;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        int count = -1;
        int countAll = 0;

        for (int i = 0; i < targets.length; i++) {
            String[] sub = targets[i].split("");
            for (int j = 0; j < sub.length; j++) {
                for (int k = 0; k < keymap.length; k++) {
                    int n = keymap[k].indexOf(sub[j]);
                    if (n != -1 && count == -1) {
                        count = n + 1;
                    } else if (n != -1 && count > n + 1) {
                        count = n + 1;
                    }
                }
                if (count == -1) {
                    countAll = -1;
                    break;
                } else {
                    countAll += count;
                }
                count = -1;
            }
            answer[i] = countAll;
            countAll = 0;
        }
        return answer;
    }
}