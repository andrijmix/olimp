using System;

namespace Panko
{
    public class Program
    {
        static void Main(string[] args)
        {
            string number = Console.ReadLine();

            if (number.Length <= 3)
            {
                Console.WriteLine(number);
                return;
            }

            string baseN = number.Remove(number.Length - 3);
            string ost = number.Replace(baseN, " ");
            Console.WriteLine(baseN + ost);

            return;
        }
    }
}