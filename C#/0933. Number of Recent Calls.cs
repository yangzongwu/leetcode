public class RecentCounter {

    Queue<int> requests=new Queue<int>();
    public RecentCounter() {
        
    }
    
    public int Ping(int t) {
        if (requests.Count()==0){
            requests.Enqueue(t);
            return 1;
        }
        else{
            while (requests.Count()!=0 && t-requests.Peek()>3000){
                requests.Dequeue();
            }
            requests.Enqueue(t);
            return requests.Count();
        }
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.Ping(t);
 */
