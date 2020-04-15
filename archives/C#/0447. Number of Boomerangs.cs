public class Solution {
    public int NumberOfBoomerangs(int[,] points) {
        int rep=0;
        for(int i=0;i<points.GetLength(0);i++){
            for(int j=0;j<points.GetLength(1);j++){
                rep+=GetNumberOfBoomerangs(i,j,points);
            }
        }
        return rep;
    }
    public int GetNumberOfBoomerangs(int i, int j, int[,] points){
        Dictionary<int,int> distancePoint=new Dictionary<int,int>();
        for(int row=i;row<points.GetLength(0);row++){
            for(int column=j;column<points.GetLength(1);column++){
                if(row!=i || column!=j){
                    int tmp=(row-i)*(row-i)+(column-j)*(column-j);
                    if(!distancePoint.ContainsKey(tmp)){
                        distancePoint[tmp]=1;
                    }
                    else{
                        distancePoint[tmp]+=1;
                    }
                }
            }
        }
        int rep=0;
        foreach(KeyValuePair<int,int> pvt in distancePoint){
            rep+=pvt.Value*(pvt.Value-1);
        }
        return rep;
    }
}
