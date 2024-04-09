Kết nối với server thông qua mật khẩu cho trước, sau đó tìm checksum và tìm file có checksum tương ứng với file checksum cho trước:
```
ctf-player@pico-chall$ sha256sum files/* | grep fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7  files/87590c24
```
Sau đó giải mã bằng tool cho trước:
```
ctf-player@pico-chall$ ./decrypt.sh files/87590c24 
picoCTF{trust_but_verify_87590c24}
```
Flag: `picoCTF{trust_but_verify_87590c24}`
