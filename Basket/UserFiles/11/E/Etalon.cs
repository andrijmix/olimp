using System;

class Program
{
    static void Main(string[] args)
    {
        string[] inp = Console.ReadLine().Split(' ');
        int n = int.Parse(inp[0]);
        int m = int.Parse(inp[1]);

        int[,] mat = new int[n, m];
        for (int i = 0; i < n; i++)
        {
            string[] row = Console.ReadLine().Split(' ');
            for (int j = 0; j < m; j++)
            {
                mat[i, j] = int.Parse(row[j]);
            }
        }

        int[,] obernena = new int[m, n];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                obernena[j, i] = mat[i, j];
            }
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Console.Write(obernena[i, j] + " ");
            }
            Console.WriteLine();
        }
    }
}