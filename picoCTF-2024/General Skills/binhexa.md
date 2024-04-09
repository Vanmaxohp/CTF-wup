```
ehc_le_dinh_van-picoctf@webshell:~$ nc titan.picoctf.net 56491

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 11100110
Binary Number 2: 10011010


Question 1/6:
Operation 1: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 8a5c

Incorrect input. Provide the right input
Enter the binary result: 1000101001011100
Correct!

Question 2/6:
Operation 2: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11111110
Correct!

Question 3/6:
Operation 3: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10000010
Correct!

Question 4/6:
Operation 4: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 110000000
Correct!

Question 5/6:
Operation 5: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 1001101
Correct!

Question 6/6:
Operation 6: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 111001100
Correct!

Enter the results of the last operation in hexadecimal: 1cc

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6862762d}
```

Đơn giản chỉ là vài phép tính nhị phân có thể tính bằng máy tính CASIO hoặc dùng python.
Flag: `picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6862762d}`
