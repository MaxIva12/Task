import sys
import statistics

def min_moves(nums):
    if not nums:
        return 0
    mean_num = int(statistics.median(nums))
    moves = 0
    for num in nums:
        moves += abs(num - mean_num)
    return moves

def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        nums = [int(line.strip()) for line in f]
    min_moves_count = min_moves(nums)
    print(min_moves_count)

if __name__ == '__main__':
    main()
