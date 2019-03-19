public class Solution {
    public int NumUniqueEmails(string[] emails) {
        HashSet<string> emailSet=new HashSet<string>();
        foreach(string email in emails){
            string curEmail=FixEmail(email);
            emailSet.Add(curEmail);
        }
        return emailSet.Count;
    }
    public string FixEmail(string email){
        string[] EmailSplit=email.Split('@');
        string rep="";
        foreach(char num in EmailSplit[0]){
            if (num!='+' && num!='.'){
                rep+=num;
            }
            else if(num=='+'){
                break;
            }
            else if(num=='.'){
                continue;
            }
        }
        return rep+'@'+EmailSplit[1];
    }
}
