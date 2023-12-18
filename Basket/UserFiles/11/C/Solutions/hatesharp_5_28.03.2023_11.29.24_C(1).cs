using System;

namespace olimpC
{
    class Progmam
    {
        static void Main(string[] args)
        {
            uint a = 0, b = 0;
            try
            {
                do
                {
                    Console.Clear();
                    Console.Write("Enter first grade of olympiad \"TheBestProgerInTheWorld\" participant   : ");
                    a = Convert.ToUInt32(Console.ReadLine());
                    Console.Write("Enter second grade of olympiad \"TheBestProgerInTheWorld\" participant   : ");
                    b = Convert.ToUInt32(Console.ReadLine());
                } while (a > 100 || b > 100); //оскільки використовується 100 бальна система числення згідно прикладу
                Console.WriteLine("Real olympiad participants: " + (a + b));
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);

            }



        }
    }
}