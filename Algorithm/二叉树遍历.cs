```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp3
{
    public class Node
    {
        public int val;
        public Node left;
        public Node right;
        public Node(int x)
        {
            val = x;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = { 1, 2, 3, 4, 5, 6, 7 };
            Node tree = GenTree(a, 0, a.Length - 1);
            DFS(tree);//4213657

            BFS(tree);
        }

        static IList<List<Node>> pathes;
        static void BFS(Node tree)
        {
            pathes = new List<List<Node>>();
            List<Node> primer = new List<Node> { tree };
            Queue<List<Node>> queue = new Queue<List<Node>>();
            queue.Enqueue(primer);

            while (queue.Count() > 0)
            {
                List<Node> cur = queue.Dequeue();
                Node tail = cur[cur.Count() - 1];
                if(tail.left==null && tail.right == null)
                {
                    pathes.Add(cur);
                }
                if (tail.left != null)
                {
                    List<Node> list = new List<Node>(cur);
                    list.Add(tail.left);
                    queue.Enqueue(list);
                }
                if (tail.right != null)
                {
                    List<Node> list = new List<Node>(cur);
                    list.Add(tail.right);
                    queue.Enqueue(list);
                }
            }
        }

        static Node GenTree(int[] a, int li, int hi)
        {
            if (hi < li) return null;
            int mi = li + (hi - li) / 2;
            Node node = new Node(a[mi]);
            node.left = GenTree(a, li, mi - 1);
            node.right = GenTree(a, mi + 1, hi);
            return node;

        }

        static void DFS(Node node)
        {
            if (node == null) return;
            System.Console.Write(node.val);
            DFS(node.left);
            DFS(node.right);
        }

    }

}
 ```
