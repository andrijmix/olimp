using System;
using System.Collections.Generic;

class Program
{
	public static void Main()
	{
		Console.WriteLine(CountPermutations(Console.ReadLine()));
	}

	public static int CountPermutations(string input)
	{
		HashSet<string> permutations = new HashSet<string>();
		Permute("", input, permutations);
		return permutations.Count;
	}

	public static void Permute(string prefix, string remaining, HashSet<string> permutations)
	{
		int n = remaining.Length;
		if (n == 0)
			permutations.Add(prefix);
		else
			for (int i = 0; i < n; i++)
				Permute(prefix + remaining[i], remaining.Substring(0, i) + remaining.Substring(i + 1), permutations);
	}
}