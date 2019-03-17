public class Solution {
    public int NumRookCaptures(char[][] board) {
        int rowA=0;
        int columnA=0;
        bool flag=false;
        for(int r=0;r<board.Length;r++){
            for (int c=0;c<board[0].Length;c++){
                if (board[r][c]=='R'){
                    rowA=r;
                    columnA=c;
                    flag=true;
                    break;
                }
            }
            if (flag==true){break;}
        }
        int result=0;
        
        int row=rowA-1;
        int column=columnA;
        while(row>=0){
            if(board[row][column]=='B'){
                break;
            }
            else if(board[row][column]=='p'){
                result+=1;
                break;
            }
            else{
                row-=1;
            }
        }
        
        row=rowA;
        column=columnA-1;
        while(column>=0){
            if(board[row][column]=='B'){
                break;
            }
            else if(board[row][column]=='p'){
                result+=1;
                break;
            }
            else{
                column-=1;
            }
        }
        
        row=rowA+1;
        column=columnA;
        while(row<board.Length){
            if(board[row][column]=='B'){
                break;
            }
            else if(board[row][column]=='p'){
                result+=1;
                break;
            }
            else{
                row+=1;
            }
        }
        
        row=rowA;
        column=columnA+1;
        while(column<board[0].Length){
            if(board[row][column]=='B'){
                break;
            }
            else if(board[row][column]=='p'){
                result+=1;
                break;
            }
            else{
                column+=1;
            }
        }
        
        return result;
    }
}
