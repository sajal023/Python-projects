row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
index = print("where do you want to put prize : ")
column_no = (index[0])
row_no = (index[1])

map[row_no - 1][column_no - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")