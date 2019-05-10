using System;
using System.Collections.Generic;

namespace ConsoleApp3
{
    public class Program
    {
        static void Main(string[] args)
        {
            Node root = new Node(0);
            root.left = new Node(1);
            root.right = new Node(2);
            root.left.left = new Node(3);
            root.left.right = new Node(4);

            FindPath T = new FindPath();
            var rep = T.DFSPath(root);
            Console.WriteLine(rep);
        }
    }
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

    public class FindPath
    {
        public IList<IList<Node>> DFSPath(Node root)
        {
            List<IList<Node>> rep = new List<IList<Node>>();
            if (root == null)
                return rep;

            List<Node> tmpList = new List<Node>();
            tmpList.Add(root);

            DFSPath(root, rep,tmpList);
            return rep;
        }
        public void DFSPath(Node root, List<IList<Node>> rep, List<Node> tmpList)
        {
            if (root.left == null && root.right == null)
                rep.Add(tmpList);
            if (root.left != null)
            {
                var curLeftList = new List<Node>();
                foreach(var curRoot in tmpList)
                {
                    curLeftList.Add(curRoot);
                }
                curLeftList.Add(root.left);
                DFSPath(root.left, rep, curLeftList);
            }
            if (root.right != null)
            {
                var curRightList = new List<Node>();
                foreach (var curRoot in tmpList)
                {
                    curRightList.Add(curRoot);
                }
                curRightList.Add(root.right);
                DFSPath(root.right, rep, curRightList);
            }
        }
    }
}
 
