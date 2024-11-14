def grade_marks(score):
    if score >= 60:
        return 'Passed'
    else:
        return 'Failed'
def main():
    score = int(input("Enter score: "))
    if score <0 or score >= 100:
        print("Score must be between 0 and 100")
    else:
        print(f"Your score is: {score}")
if __name__ == "__main__":
    main()