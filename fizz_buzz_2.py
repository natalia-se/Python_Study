def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result

def count_correct_outputs(candidate_output, correct_output):
    return sum(1 for a, b in zip(candidate_output, correct_output) if a == b)

# Read input
n, m = map(int, input().split())
candidates_outputs = []
for _ in range(n):
    candidate_output = input().split()
    candidates_outputs.append(candidate_output)

# Generate correct FizzBuzz output
correct_output = fizz_buzz(m)

# Count correct outputs for each candidate
scores = [count_correct_outputs(candidate, correct_output) for candidate in candidates_outputs]

# Find the candidate with the highest score (lowest index in case of a tie)
best_candidate = scores.index(max(scores)) + 1

# Print the result
print(best_candidate)
