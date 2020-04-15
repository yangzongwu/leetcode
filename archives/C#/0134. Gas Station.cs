public class Solution {
    public int CanCompleteCircuit(int[] gas, int[] cost) {
        for(int i=0;i<gas.Length;i++){
            if(CanCompleteCircuit(gas,cost,i))
                return i;
        }
        return -1;
    }
    public bool CanCompleteCircuit(int[] gas, int[] cost,int k){
        if(gas[k]<cost[k])
            return false;
        int len=gas.Length-1;
        int avgGas=0;
        while(k<gas.Length){
            avgGas=avgGas+gas[k]-cost[k];
            if(avgGas>=0){
                k++;
                len--;
            }
            else
                return false;
        }
        
        k=0;
        while(len>=0){
            avgGas=avgGas+gas[k]-cost[k];
            if(avgGas>=0){
                k++;
                len--;
            }
            else
                return false;
        }
        return true;
    } 
}
