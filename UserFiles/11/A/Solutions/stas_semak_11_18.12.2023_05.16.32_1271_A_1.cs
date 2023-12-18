using System;
using System.Linq;

namespace ConsoleApp33
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList().ForEach(token =>
            {
                var num = int.Parse(token);
                if (num % 7 == 0 && num % 5 != 0) Console.Write($"{num} ");
            });
        }
    }
}