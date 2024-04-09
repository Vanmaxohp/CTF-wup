Tải file về, ta có 1 file pdf, mở ra xem:
<img width="960" alt="image" src="https://github.com/Vanmaxohp/picoCTF-2024/assets/90485791/12df628e-5156-45d2-b900-f47b0fce2230">

Ta có phần 2 của flag: `1n_pn9_&_pdf_90974127}`

Đề bài hint là có thể giải bài này bằng cách mở file theo cách khác, mở file bằng HxD, thấy có signature của png:
<img width="960" alt="image" src="https://github.com/Vanmaxohp/picoCTF-2024/assets/90485791/00bea273-3139-4524-a3f0-fb8e26892b3c">

Đổi đuôi file thành .png và mở ra xem:
<img width="45" alt="image" src="https://github.com/Vanmaxohp/picoCTF-2024/assets/90485791/c5dfbc69-178e-409e-935e-7c39a2117d7e">

Ta có phần đầu của flag: `picoCTF{f1u3n7_`
Ghép lại: `picoCTF{f1u3n7_1n_pn9_&_pdf_90974127}`
