import itertools
import numpy as np


def lcs(X, Y):
    # find the length of the strings

    m = len(X)

    n = len(Y)
    # else:
    #     n = len(X)
    #     m = len(Y)
    #     # TMP = X
    # X = Y
    # Y = TMP

    # declaring the array for storing the dp values

    table = [[0] * (n + 1) for i in range(m + 1)]
    lexical_table = [[""] * (n + 1) for i in range(m + 1)]
    paths = []
    lexical_table_reprs = []
    table_reprs = []
    for i in range(1, m + 1):
        # s = [[str(e) for e in row] for row in table]
        # ls = [str(row) for row in lexical_table]
        # lens = [max(map(len, col)) for col in zip(*s)]
        # fmt = " ".join("{{:{}}}".format(x) for x in lens)
        # t = [fmt.format(*row) for row in s]
        # table_reprs.append("\n".join(t))
        # lexical_table_reprs.append("\n".join(ls))
        for j in range(1, n + 1):
            if i == 0 or j == 0:
                table[i][j] = ""
                lexical_table[i][j] = ""
            elif X[i - 1] == Y[j - 1]:
                lexical_table[i][j] = f"{lexical_table[i - 1][j - 1]}{X[i - 1]}"
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                # paths.append(f"{X[i-1]} and {Y[j-1]}")
                # print(f"{table[i - 1][j]}|{table[i][j - 1]}")
                if table[i - 1][j] > table[i][j - 1]:
                    tmp = f"{X[i-1]} {Y[j-1]}\n"
                    # paths.append(f"({i-1}, {j})\ncomparing: {X[i-1]} and {Y[j-1]}")
                    tmp1 = np.array(table)
                    if (tmp1 == 0).all():
                        s = ["EMPTY TABLE"]
                    else:
                        s = [[e for e in row] for row in table]

                    ls = [str(row) for row in lexical_table]
                    # lens = [max(map(len, col)) for col in zip(*s)]
                    # fmt = " ".join("{{:{}}}".format(x) for x in lens)
                    # t = [fmt.format(*row) for row in s]
                    table_reprs.append(s)
                    # table_reprs.append("\n".join(t))
                    lexical_table_reprs.append("\n".join(ls))
                    table[i][j] = table[i - 1][j]
                    lexical_table[i][j] = lexical_table[i - 1][j]
                else:
                    tmp = f"({i-1}, {j})"
                    tmp1 = np.array(table)
                    if (tmp1 == 0).all():
                        s = ["EMPTY TABLE"]
                    else:
                        s = [[e for e in row] for row in table]

                    ls = [str(row) for row in lexical_table]

                    # lens = [max(map(len, col)) for col in zip(*s)]
                    # fmt = " ".join("{{:{}}}".format(x) for x in lens)
                    # t = [fmt.format(*row) for row in s]

                    table_reprs.append(s)
                    lexical_table_reprs.append("\n".join(ls))
                    table[i][j] = table[i][j - 1]
                    lexical_table[i][j] = lexical_table[i][j - 1]
                paths.append(f"path:{tmp}\n")
                continue

    print(
        f"The following format is how I copied and filled in my tables:\n\n```\n\t[chosen value from table]\t[path taken]\n\n\t[Table Representation]\n```\n"
    )
    column_labels = list(X)
    row_labels = list(Y)

    # print(column_labels)
    # for t in table_reprs:
    #     print(" ".join(["-", *row_labels]))
    #     for row in t:
    #         if len(column_labels) > t.index(row):
    #             tmp = column_labels[t.index(row)]
    #         else:
    #             tmp = "X"
    #         print(tmp, end=" ")
    #         for item in row:
    #             print(item, end=" ")
    #         print()

    # for tb, p in zip(table_reprs, paths):
    #     if "EMPTY" in tb:
    #         print("EMPTY")
    #         # print(p, "".join(tb), end=f"\n")
    #     else:
    #         print(p)
    #         for t in tb:
    #             print(t)
    # print(p, "\n".format(x for x in tb), end=f"\n")

    print(f"LONGESET LEXICAL PATTERN {lexical_table[m][n]}")
    for l in ["-", *column_labels]:
        print(l, end="      ")
    print()
    for row in table_reprs[len(table_reprs) - 1]:
        ind = table_reprs[len(table_reprs) - 1].index(row)
        if row_labels[ind] != None or row_labels[ind] != 0:
            print(row_labels[ind], end="      ")
        for i in row:
            print(i, end="      ")
        print("\n")

    max_lengths = max([max(len(x) for x in f) for f in lexical_table]) + 1
    spacer = max_lengths * " "
    # print(max(max_lengths))

    from xlwt import Workbook

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet("Sheet 1")
    i, j = 0, 0
    for lex in lexical_table:
        for l in lex:
            if l is "":
                print(" ", end=spacer)
            else:
                print(l, end=(max_lengths - len(l)) * " ")
            sheet1.write(i, j, str(l))
            j += 1
        print("")
        i += 1
    for p in paths:
        print(p)
    # dirctions = [[None] * len(table_reprs[0]) * table_reprs[0]]
    # i, j = m, n
    # xi = table[i]
    # yj = table[i][j]
    # if (xi == yj):
    #     b[i][j] = diagonalUpLeftArrow

    # else :
    #     if (c[i - 1][j] >= c[i][j - 1])
    #         b[i][j] = upArrow
    #     else
    #         b[i][j] = rightArrow

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return table[m][n]


# end of function lc
