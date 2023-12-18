using System;

class Program
{
    public static void Main(string[] args)
    {
        // зчитування розмірів матриці
        Console.Write("Enter the sizes: ");
        string[] sizes = Console.ReadLine().Split();
        int n = int.Parse(sizes[0]);
        int m = int.Parse(sizes[1]);

        // зчитування елементів матриці
        int[,] a = new int[n, m];
        for (int i = 0; i < n; i++)
        {
            Console.Write("Enter the element in row: ");
            string[] row = Console.ReadLine().Split();
            for (int j = 0; j < m; j++)
            {
                a[i, j] = int.Parse(row[j]);
            }
        }

        // розвернення матриці
        int[,] b = new int[m, n];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                b[j, i] = a[i, j];
            }
        }

        // виведення результуючої матриці
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Console.Write($"{b[i, j]} ");
            }
            Console.WriteLine();
        }
    }
}