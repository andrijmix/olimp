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

            int n = int.Parse(Console.ReadLine());
            string rez = "", line = Console.ReadLine();

            for (int i = 0; i < n; i++)
            {
                rez += line + " ";
            }
            rez.TrimEnd(' ');
            Console.WriteLine(rez);
        }
    }
}