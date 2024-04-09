```
ehc_le_dinh_van-picoctf@webshell:~$ mkdir TimeMac   
ehc_le_dinh_van-picoctf@webshell:~$ cd TimeMac/
ehc_le_dinh_van-picoctf@webshell:~/TimeMac$ wget https://artifacts.picoctf.net/c_titan/160/challenge.zip
--2024-03-15 10:20:06--  https://artifacts.picoctf.net/c_titan/160/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.18, 3.160.5.42, 3.160.5.71, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17740 (17K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip                                      100%[==============================================================================================================>]  17.32K  --.-KB/s    in 0.001s  

2024-03-15 10:20:06 (23.9 MB/s) - 'challenge.zip' saved [17740/17740]

ehc_le_dinh_van-picoctf@webshell:~/TimeMac$ ls     
challenge.zip
ehc_le_dinh_van-picoctf@webshell:~/TimeMac$ unzip challenge.zip 
Archive:  challenge.zip
   creating: drop-in/
  inflating: drop-in/message.txt     
   creating: drop-in/.git/
   creating: drop-in/.git/branches/
  inflating: drop-in/.git/description  
   creating: drop-in/.git/hooks/
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
   creating: drop-in/.git/info/
  inflating: drop-in/.git/info/exclude  
   creating: drop-in/.git/refs/
   creating: drop-in/.git/refs/heads/
 extracting: drop-in/.git/refs/heads/master  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/43/
 extracting: drop-in/.git/objects/43/246218ab4fc7b30e9a9dff073e012316851469  
   creating: drop-in/.git/objects/25/
 extracting: drop-in/.git/objects/25/16effb8d70e33bdd0023629b164a77225e1ec2  
   creating: drop-in/.git/objects/89/
 extracting: drop-in/.git/objects/89/d296ef533525a1378529be66b22d6a2c01e530  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master  
ehc_le_dinh_van-picoctf@webshell:~/TimeMac$ cd drop-in/
ehc_le_dinh_van-picoctf@webshell:~/TimeMac/drop-in$ git log

[11]+  Stopped                 git log
ehc_le_dinh_van-picoctf@webshell:~/TimeMac/drop-in$
```


<img width="324" alt="image" src="https://github.com/Vanmaxohp/picoCTF-2024/assets/90485791/1042c0eb-66f4-48e4-b5cf-5131996f636c">

Flag: `picoCTF{t1m3m@ch1n3_186cd7d7}`
