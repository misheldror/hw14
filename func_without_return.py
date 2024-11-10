#a
def ascending_my(start, end):
    for i in range(start, end + 1):
        print(i, "OK going up")

ascending_my(7, 12)

#b
def details_my(s):
    first_char = s[0]
    middle_char = s[len(s) // 2]
    last_char = s[-1]

    print("First character:", first_char)
    print("Middle character:", middle_char)
    print("Last character:", last_char)

details_my("AI is the best")

#c
def bool_say(b):
    if b:
        print("yes")
    else:
        print("no")

bool_say(True)
bool_say(False)

#d
def zugi_print(numbers):
    for num in numbers:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

zugi_print([14, 14, 15, 10, 2, 3, 5])

#e
def statistics_my(scores):
    if len(scores) == 0:
        print("No valid scores")
        return

    highest_score = max(scores)
    lowest_score = min(scores)
    number_of_scores = len(scores)
    average_score = sum(scores) / number_of_scores

    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Number of scores: {number_of_scores}")
    print(f"Average score: {average_score}")

scores = []
while True:
    score = int(input("Enter a score: "))
    if score == -99:
        break
    elif 0 <= score <= 100:
        scores.append(score)
    else:
        print("Invalid score")

statistics_my(scores)
