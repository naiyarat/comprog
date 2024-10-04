def main():
    scores = input().split()
    max, min = 0, 100
    maxStr, minStr = '', ''
    for score in scores:
        if float(score) < min:
            min, minStr = float(score), score
        if float(score) > max:
            max, maxStr = float(score), score
    scores.remove(maxStr)
    scores.remove(minStr)
    
    final_score = (float(scores[0]) + float(scores[1]))/2
    print(round(final_score, 2))
if __name__ == '__main__':
    main()