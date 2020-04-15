public class Solution {
    public IList<string> ReadBinaryWatch(int num) {
        IList<string> rep=new List<string>();
        for(int h=0;h<=Math.Min(num,3);h++){
            if(h>=num-5){
                string[] hours=GetHoursList(h);
                string[] mimutes=GetMimutesList(num-h);
                foreach(string hour in hours){
                    foreach(string mimute in mimutes){
                        rep.Add(hour+":"+mimute);
                    }
                }
            }
        }
        return rep;
    }
    public string[] GetHoursList(int num){
        switch(num){
            case 0:
                return new string[]{"0"};
                break;
            case 1:
                return new string[]{"1","2","4","8"};
                break;
            case 2:
                return new string[]{"3","5","9","6","10"};
                break;
            default:
                return new string[]{"7","11"};
                break;
                
        }
        
    }
    public string[] GetMimutesList(int num){
        switch(num){
            case 0:
                return new string[]{"00"};
                break;
            case 1:
                return new string[]{"01","02","04","08","16","32"};
                break;
            case 2:
                return new string[]{"03", "05", "06", "09", "10", "12", "17", "18", 
                                    "20", "24", "33", "34", "36", "40", "48"};
                break;
            case 3:
                return new string[]{"07", "11", "13", "14", "19", "21", "22", "25",
                                    "26", "28", "35", "37", "38", "41", "42", "44",
                                    "49", "50", "52", "56"};
                break;
            case 4:
                return new string[]{"15", "23", "27", "29", "30", "39", "43", "45", 
                                    "46", "51", "53", "54", "57", "58"};
                break;
            default:
                return new string[]{"31","47","55","59"};
                break;
    }
}
}
