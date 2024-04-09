Đề cho 1 file, cat thì ra một dãy ký tự có vẻ là base64:
`YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg==`
Decode bằng tool trên mạng, ra:
`d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==`
Có vẻ vẫn là base64, decode tiếp:
`wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}`
Lần này thì nhìn có vẻ là ROT, decode bằng [dcode.fr](https://www.dcode.fr/rot-cipher), thì ra được nó là ROT +7:
`picoCTF{caesar_d3cr9pt3d_a47c6d69}`
