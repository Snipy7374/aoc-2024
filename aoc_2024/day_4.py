# ugly solutions, classes can be used to handle these better (especially in the first part where there is
# a lot of redundancy)

def xmas_counter(data: list[str]) -> int:
    counter = 0

    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "X":
                # check right
                right = "X"
                for i in range(1, 4):
                    if (char + i) >= len(data[line]):
                        break

                    right += data[line][char + i]

                # check left
                left = "X"
                for i in range(1, 4):
                    if (char - i) < 0:
                        break

                    left += data[line][char - i]

                # check up
                up = "X"
                for i in range(1, 4):
                    if (line - i) < 0:
                        break

                    up += data[line - i][char]
 
                # check down
                down = "X"
                for i in range(1, 4):
                    if (line + i) >= len(data):
                        break

                    down += data[line + i][char]

                # check diagonal (nord-ovest)
                no = "X"
                for i in range(1, 4):
                    if (line - i) < 0 or (char - i) < 0:
                        break

                    no += data[line - i][char - i]
                
                # check diagonal (nord-est)
                ne = "X"
                for i in range(1, 4):
                    if (line - i) < 0 or (char + i) >= len(data[line - i]):
                        break

                    ne += data[line - i][char + i]
                
                # check diagonal (sud-ovest)
                so = "X"
                for i in range(1, 4):
                    if (line + i) >= len(data) or (char - i) < 0:
                        break

                    so += data[line + i][char - i]
                
                # check diagonal (sud-est)
                se = "X"
                for i in range(1, 4):
                    if (line + i) >= len(data) or (char + i) >= len(data[line + i]):
                        break

                    se += data[line + i][char + i]
                
                if right == "XMAS":
                    counter += 1
                if left == "XMAS":
                    counter += 1
                if up == "XMAS":
                    counter += 1
                if down == "XMAS":
                    counter += 1
                if no == "XMAS":
                    counter += 1
                if ne == "XMAS":
                    counter += 1
                if so == "XMAS":
                    counter += 1
                if se == "XMAS":
                    counter += 1

    return counter


# pt2 solution
def mas_x_counter(data: list[str]) -> int:
    counter = 0

    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "A":
                x = False
                y = False

                if (line - 1) < 0 or (char - 1) < 0:
                    continue

                if (line + 1) >= len(data) or (char + 1) >= len(data[line + 1]):
                    continue

                if (
                    data[line - 1][char - 1] == "M"
                    and data[line + 1][char + 1] == "S"
                ) or (
                    data[line - 1][char - 1] == "S"
                    and data[line + 1][char + 1] == "M"
                ):
                    x = True
                
                if (
                    data[line - 1][char + 1] == "M"
                    and data[line + 1][char - 1] == "S"
                ) or (
                    data[line - 1][char + 1] == "S"
                    and data[line + 1][char - 1] == "M"
                ):
                    y = True

                if x and y:
                    counter += 1

    return counter
