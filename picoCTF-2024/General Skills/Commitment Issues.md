Tải file về và uzip:
```
ehc_le_dinh_van-picoctf@webshell:~/git$ unzip challenge.zip.2
Archive:  challenge.zip.2
   creating: drop-in/
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
   creating: drop-in/.git/objects/ba/
 extracting: drop-in/.git/objects/ba/e247ddd9f730bb7a2a9425d4616b116bc7b07b  
   creating: drop-in/.git/objects/68/
 extracting: drop-in/.git/objects/68/df36301019ecc05a65a4e87a754c83411ac925  
   creating: drop-in/.git/objects/87/
 extracting: drop-in/.git/objects/87/b85d7dfb839b077678611280fa023d76e017b8  
   creating: drop-in/.git/objects/d5/
 extracting: drop-in/.git/objects/d5/52d1ecd2d83fa2e65b6724d1ff73b45a7d59b7  
   creating: drop-in/.git/objects/0c/
 extracting: drop-in/.git/objects/0c/1ab266b7a3a1cd099bb509f82b7a2d03aecd03  
   creating: drop-in/.git/objects/8d/
 extracting: drop-in/.git/objects/8d/c51806c760dfdbb34b33a2008926d3d8e8ad49  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master  
 extracting: drop-in/message.txt
```
Truy cập vào thư mục drop-in/ sau đó kiểm tra phiên bản bằng `git log`
Check out phiên bản lúc flag được tạo:
```
ehc_le_dinh_van-picoctf@webshell:~/git$ cd drop-in/
ehc_le_dinh_van-picoctf@webshell:~/git/drop-in$ git log

[1]+  Stopped                 git log
ehc_le_dinh_van-picoctf@webshell:~/git/drop-in$ git checkout 87b85d7dfb839b077678611280fa023d76e017b8
Note: switching to '87b85d7dfb839b077678611280fa023d76e017b8'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 87b85d7 create flag
ehc_le_dinh_van-picoctf@webshell:~/git/drop-in$ ls
message.txt
ehc_le_dinh_van-picoctf@webshell:~/git/drop-in$ cat message.txt 
picoCTF{s@n1t1z3_ea83ff2a}
```
Mở file ra là có flag
