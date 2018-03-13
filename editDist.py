import sys


def edit_distance(x, y, memo=None):

    if memo is None:
        memo = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    # initialize first row and column
    for i in range(1, len(y)+1):
        memo[0][i] = i
    for i in range(1, len(x)+1):
        memo[i][0] = i

    # fill rest of matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            delta = 1 if x[i-1] != y[j-1] else 0
            memo[i][j] = min(
                memo[i - 1][j - 1] + delta,
                memo[i - 1][j] + 1,
                memo[i][j - 1] + 1
            )

    return memo[len(x)][len(y)], memo


def optimal_alignment(x, y, memo):

    i, j = len(x), len(y)
    result = ""  # prepend

    while i > 0 and j > 0:

        diag = memo[i-1][j-1]
        left = memo[i][j-1]
        abov = memo[i-1][j]

        # precedence: diagonal > left > above
        if diag <= left and diag <= abov:
            curr = 'M' if x[i - 1] == y[j - 1] else 'R'
        else:
            curr = 'I' if left <= abov else 'D'

        if curr in 'MRD':
            i -= 1
        if curr in 'MRI':
            j -= 1

        result = curr + result

    # edge case: haven't hit (0,0) yet
    result = 'D'*i + 'I'*j + result

    return result


def print_alignment(x, y, alignment):

    i, j = 0, 0
    new_alignment = ""
    for curr in alignment:

        if curr == 'M':
            new_alignment += '|'

        elif curr == 'R':
            new_alignment += ' '

        elif curr == 'I':
            new_alignment += ' '
            x = x[:i] + '-' + x[i:]

        elif curr == 'D':
            new_alignment += ' '
            y = y[:j] + '-' + y[j:]

        i, j = i + 1, j + 1

    return x, y, new_alignment


if __name__ == '__main__':

    # get string from files
    f1 = [line.rstrip('\n') for line in open(sys.argv[1])]
    f2 = [line.rstrip('\n') for line in open(sys.argv[2])]
    a, b = ' '.join(f1), ' '.join(f2)

    # calculate alignment
    edit_dist, memo_map = edit_distance(a, b)
    operations = optimal_alignment(a, b, memo_map)
    a, b, align_row = print_alignment(a, b, operations)

    # split into chunks of 60
    a_split = [a[i:i+60] for i in range(0, len(a), 60)]
    align_split = [align_row[i:i+60] for i in range(0, len(align_row), 60)]
    b_split = [b[i:i+60] for i in range(0, len(b), 60)]

    print('\noptimal alignment:\n')

    for i in range(len(align_split)):
        print(a_split[i])
        print(align_split[i])
        print(b_split[i])
        print('')

    print('edit distance = ' + str(edit_dist) + '\n')
