using System;

namespace olimpiada
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter grams: ");
            long grams = long.Parse(Console.ReadLine());
            if (grams > 0)
            {
                if (grams > 1000)
                {

                    Console.WriteLine((grams / 1000) + " " + (grams % 1000) + "g");
                }
                else
                {
                    Console.WriteLine(grams + "g");
                }
            }
            else
            {
                Console.WriteLine("Grams can't be less then 0");
            }
        }
    }
}
