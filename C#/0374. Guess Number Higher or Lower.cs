// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int left=1;
        int right=n;
        while(left<=right){
            int mid=left+(right-left)/2;
            int var=guess(mid);
            if (var==0){return mid;}
            else if(var==-1){right=mid-1;}
            else{left=mid+1;}
        }
        return 0;
    }
};
