Tải file về, dùng exiftool để kiểm tra thì thấy có đoạn code base64 đáng ngờ:
```
ehc_le_dinh_van-picoctf@webshell:~$ exiftool ukn_reality.jpg 
ExifTool Version Number         : 12.40
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2024:03:12 00:05:51+00:00
File Access Date/Time           : 2024:03:13 02:41:07+00:00
File Inode Change Date/Time     : 2024:03:13 02:40:53+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```
Decode bằng Cyberchef, có được flag: `picoCTF{ME74D47A_HIDD3N_3b9209a2}`
