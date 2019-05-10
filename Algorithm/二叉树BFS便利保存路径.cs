using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            Node root = new Node(0);
            root.left = new Node(1);
            root.right = new Node(2);
            root.left.left = new Node(3);
            root.left.right = new Node(4);

            FindPath T = new FindPath();
            var rep = T.BFSPath(root);
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
        public List<IList<Node>> BFSPath(Node root)
        {
            var result = new List<IList<Node>>();
            if (root == null)
                return result;

            var rootQueue = new Queue<Node>();
            rootQueue.Enqueue(root);
            var rootPathQueue = new Queue<List<Node>>();
            var curList = new List<Node>();
            curList.Add(root);
            rootPathQueue.Enqueue(curList);

            while (rootQueue.Count() != 0)
            {
                int curLength = rootQueue.Count();
                for (int i = 0; i < curLength; i++)
                {
                    Node curRoot = rootQueue.Dequeue();
                    var curRootList = rootPathQueue.Dequeue();
                    if (curRoot.left == null && curRoot.right == null)
                    {
                        result.Add(curRootList);
                    }
                    else
                    {
                        if (curRoot.left != null)
                        {
                            rootQueue.Enqueue(curRoot.left);
                            var curLeftList = new List<Node>();
                            foreach(var curroot in curRootList)
                            {
                                curLeftList.Add(curroot);
                            }
                            curLeftList.Add(curRoot.left);
                            rootPathQueue.Enqueue(curLeftList);
                        }
                        if (curRoot.right != null)
                        {
                            rootQueue.Enqueue(curRoot.right);
                            var curRightList = new List<Node>();
                            foreach (var curroot in curRootList)
                            {
                                curRightList.Add(curroot);
                            }
                            curRightList.Add(curRoot.right);
                            rootPathQueue.Enqueue(curRightList);
                        }
                    }
                }
            }
            return result;
        }
    }
}


