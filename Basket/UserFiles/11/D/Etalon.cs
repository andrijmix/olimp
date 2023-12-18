using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string num = Console.ReadLine();

            if (num.Length < 4)
            {
                Console.WriteLine(0 + " " + num);
            }
            else
            {
                for(int i = 0; i < num.Length - 3; i++)
                {
                    Console.Write(num[i]);
                }
                Console.Write(" ");

                for (int i = num.Length - 3; i < num.Length; i++)
                {
                    Console.Write(num[i]);
                }
            }
        }
    }
}