import sys

scores = []
print("=== Player Score Analytics ===")
try:
    if (len(sys.argv) < 2):
        raise ValueError(f"No scores provided. Usage: python3 {sys.argv[0]} "
                         f"<score1> <score2> ...")
    for i in range(1, len(sys.argv)):
        try:
            score = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            raise ValueError(f"Invalid score '{sys.argv[i]}'. "
                             "Scores must be numeric values.")
except ValueError as ve:
    print(ve)
    sys.exit(1)

if scores:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
