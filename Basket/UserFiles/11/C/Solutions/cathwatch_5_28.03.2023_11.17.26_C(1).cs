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
            // A
            /*string[] line = Console.ReadLine().Split(' ');
            int a = int.Parse(line[0]), b = int.Parse(line[1]);

            Console.WriteLine(a - b);*/

            // B
            /*int n = int.Parse(Console.ReadLine());
            string rez = "", line = Console.ReadLine();


            for (int i = 0; i < n; i++)
            {
                rez += line + " ";
            }
            rez.TrimEnd(' ');
            Console.WriteLine(rez);*/

            // C
            string[] line = Console.ReadLine().Split(' ');
            int a = int.Parse(line[0]), b = int.Parse(line[1]);

            Console.WriteLine(a + b);
        }
    }
}
