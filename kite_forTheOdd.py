## Look for nothing
n = 6
m = n // 2 + 1  # Integer division for floor
for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
   if i <= m:
       for k in range(m - i, 0, -1):  # Iterate backwards for spaces
           print(" ", end="")
       for p in range(2 * i - 1, 0, -1):  # Iterate backwards for asterisks
           print("*", end="")
   else:
       for k in range(i - m):  # Iterate for spaces
           print(" ", end="")
       for p in range(n - 2*(i - m)):  # Iterate for asterisks
           print("*", end="")
   print()  # Print a newline after each row

# n = 6, m = Math.floor(n / 2) + 1;
# for (let i = 1; i <= n; i++) {
#     if (i <= m) {
#         for (k = m - i; k > 0; k--) {
#             print(" ");
#         }
#         for (let p = 2 * i - 1; p > 0; p--) {
#             print("*");
#         }
#         println();
#     } else {
#         for (k = i - m; k > 0; k--) {
#             print(" ")
#         } for (p = n - (i - m); p > 0; p--) {
#             print("*")
#         }println();
#     }
# }
