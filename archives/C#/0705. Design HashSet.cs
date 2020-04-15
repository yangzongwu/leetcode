public class MyHashSet {

    Dictionary<int,int> mySet=new Dictionary<int,int>();
    /** Initialize your data structure here. */
    public MyHashSet() {
        
    }
    
    public void Add(int key) {
        if(!mySet.ContainsKey(key)){
            mySet[key]=1;
        }
    }
    
    public void Remove(int key) {
        if(mySet.ContainsKey(key)){
            mySet[key]-=1;
            if (mySet[key]==0){
                mySet.Remove(key);
            }
        }
        
    }
    
    /** Returns true if this set contains the specified element */
    public bool Contains(int key) {
        return mySet.ContainsKey(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */
