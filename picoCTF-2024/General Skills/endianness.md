Truy cập vào server và trả lời câu hỏi:
```
ehc_le_dinh_van-picoctf@webshell:~/git/drop-in$ nc titan.picoctf.net 57272
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: ltxhj
Enter the Little Endian representation: 6a6878746c
Correct Little Endian representation!
Enter the Big Endian representation: 6c7478686a
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_28329f0a}
```
Ở đây, little endian là biểu diễn byte theo chiều từ byte cuối đến byte đầu, tức là sẽ biểu diễn từ byte của chữ j - 6a đến chữ l - 6c. CÒn Big endian thì ngược lại, biểu diễn từ trái sang phải.
