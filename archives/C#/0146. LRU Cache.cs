public class LRUCache {
    public class ListNode{
        public int val;
        public ListNode next;
        public ListNode prev;
        public ListNode(int x){
            val=x;
        }
    }
    
    
    ListNode head=new ListNode(0);
    ListNode tail=new ListNode(0);
    int cnt;
    Dictionary<int,ListNode> myDict=new Dictionary<int,ListNode>();
    Dictionary<ListNode,int> myDict2=new Dictionary<ListNode,int>();
    
    public LRUCache(int capacity) {
        cnt=capacity;
        head.next=tail;
        tail.prev=head;
    }
    
    public int Get(int key) {
        if(myDict.ContainsKey(key)){
            ReorderList(key);
            return myDict[key].val;   
        }
        else{
            return -1;
        }
    }
    
    public void Put(int key, int value) {
        if(myDict.ContainsKey(key)){
            ReorderList(key);
            myDict[key].val=value;
        }
        else{
            if(cnt==0)//capacity full
            {
                DeleteLastList();
                InsertList(key,value);
            }
            else//capacity not full
            {
                cnt--;
                InsertList(key,value);
            }
        }
    }
    
    public void DeleteLastList(){
        ListNode deleteList=tail.prev;
        int key=myDict2[deleteList];
        int tmp=myDict2[deleteList];
        myDict2.Remove(deleteList);
        myDict.Remove(tmp);
        
        ListNode prevprevtail=tail.prev.prev;
        prevprevtail.next=tail;
        tail.prev=prevprevtail;
    }
    public void InsertList(int key, int value){
        ListNode newNode=new ListNode(value);
        myDict[key]=newNode;
        myDict2[newNode]=key;
        ListNode curHeadNext=head.next;
        head.next=newNode;
        newNode.next=curHeadNext;
        curHeadNext.prev=newNode;
        newNode.prev=head;
    }
    
    
    public void ReorderList(int key){
        ListNode curNode=myDict[key];
        ListNode preCurNode=curNode.prev;
        ListNode nextCurNode=curNode.next;
        preCurNode.next=nextCurNode;
        nextCurNode.prev=preCurNode;
        
        ListNode newcurNodeNext=head.next;
        head.next=curNode;
        curNode.next=newcurNodeNext;
        newcurNodeNext.prev=curNode;
        curNode.prev=head;
            
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
