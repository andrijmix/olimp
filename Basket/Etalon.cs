using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter two numbers separated by a space (e.g., '2 4'):");
        string input = Console.ReadLine();

        // Розділяємо вхідний рядок на дві частини
        string[] numbers = input.Split(' ');

        // Конвертуємо розділені рядки в цілі числа
        int num1 = int.Parse(numbers[0]);
        int num2 = int.Parse(numbers[1]);

        // Розраховуємо суму
        int sum = num1 + num2;

        // Виводимо суму
        Console.WriteLine($"Сума {num1} і {num2} дорівнює {sum}.");
    }
}
