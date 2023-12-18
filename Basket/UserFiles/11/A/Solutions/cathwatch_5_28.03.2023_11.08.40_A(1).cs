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
            string[] line = Console.ReadLine().Split(' ');
            int a = int.Parse(line[0]), b = int.Parse(line[1]);

            Console.WriteLine(a - b);
        }
    }
}
