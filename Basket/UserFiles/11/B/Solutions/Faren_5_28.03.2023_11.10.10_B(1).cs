using System;

namespace olimpiada
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a phrase: ");
            string phrase = Console.ReadLine();
            Console.Write("Enter state number : ");
            int state_number = Int32.Parse(Console.ReadLine());
            if (state_number > 0)
            {
                                for (int i = 0; i < state_number; i++)
                {
                    Console.Write(phrase+" ");
                }
            }
            else
            {
                Console.WriteLine("Enter valid state number");
            }
        }
    }
}
