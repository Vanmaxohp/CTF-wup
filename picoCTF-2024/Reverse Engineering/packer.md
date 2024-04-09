Download file về, ta có một file out.
Thử search gg hint `What can we do to reduce the size of a binary after compiling it.`
Ta có được câu trả lời là unpack bằng upx
`upx -d out`
Sau đó strings file đã được unpack và lưu vào 1 file tạm:
```
ehc_le_dinh_van-picoctf@webshell:~/re$ strings -a out > txet.txt
ehc_le_dinh_van-picoctf@webshell:~/re$ nano txet.txt
```
Ta thấy một đoạn mã hex rất đáng ngờ:
<img width="960" alt="image" src="https://github.com/Vanmaxohp/picoCTF-2024/assets/90485791/d1c124d5-1b7f-4c52-9808-257b44baf0ad">

`7069636f
4354467b
5539585f
556e5034
636b314e
365f4231
6e345269
33535f31
61356133
6633397d`
Decode (xoá chữ H), có được flag: `picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_1a5a3f39}`
