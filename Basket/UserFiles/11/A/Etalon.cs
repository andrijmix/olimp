using System;

namespace A
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] a;
            a = Console.ReadLine().Split(' ');
            Console.WriteLine(Int64.Parse(a[0]) - Int64.Parse(a[1]));
        }
    }
}