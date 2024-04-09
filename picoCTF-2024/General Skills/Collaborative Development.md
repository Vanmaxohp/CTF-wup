```
ehc_le_dinh_van-picoctf@webshell:~/ColDev$ wget https://artifacts.picoctf.net/c_titan/176/challenge.zip
--2024-03-15 09:41:28--  https://artifacts.picoctf.net/c_titan/176/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.5.42, 3.160.5.71, 3.160.5.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.5.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 24474 (24K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip                                      100%[==============================================================================================================>]  23.90K  --.-KB/s    in 0.001s  

2024-03-15 09:41:28 (29.7 MB/s) - 'challenge.zip' saved [24474/24474]

ehc_le_dinh_van-picoctf@webshell:~/ColDev$ unzip challenge.zip 
Archive:  challenge.zip
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
 extracting: drop-in/.git/refs/heads/main  
   creating: drop-in/.git/refs/heads/feature/
 extracting: drop-in/.git/refs/heads/feature/part-1  
 extracting: drop-in/.git/refs/heads/feature/part-2  
 extracting: drop-in/.git/refs/heads/feature/part-3  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/77/
 extracting: drop-in/.git/objects/77/d6ceca6fe23b57d88cf16f20003e10d6715690  
   creating: drop-in/.git/objects/b9/
 extracting: drop-in/.git/objects/b9/32e8c048154a46d224cd7691c99dc8cb88164a  
   creating: drop-in/.git/objects/eb/
 extracting: drop-in/.git/objects/eb/19d0e3c28278752f0735c4451b885136a24105  
   creating: drop-in/.git/objects/6e/
 extracting: drop-in/.git/objects/6e/17fb3a35364b4f9bb8bef8b5e6a5af2d3e7dfa  
   creating: drop-in/.git/objects/43/
 extracting: drop-in/.git/objects/43/e44dd37ba0c0adc3d78d0b85d699859ec8d75c  
   creating: drop-in/.git/objects/0c/
 extracting: drop-in/.git/objects/0c/d57e0aedc31a1a92e0b79235c818de437cde8e  
   creating: drop-in/.git/objects/7a/
 extracting: drop-in/.git/objects/7a/b4e25c0cd108374b2275fdb1fcdf635e591833  
 extracting: drop-in/.git/objects/7a/7534d2ed05e1637c5ea21d0981646444c2c9f9  
   creating: drop-in/.git/objects/d1/
 extracting: drop-in/.git/objects/d1/f3407cee4479c075997b497fa290ca636fe258  
   creating: drop-in/.git/objects/70/
 extracting: drop-in/.git/objects/70/64732e2fd39d2247bd6ba2ccc4cf9576974d38  
   creating: drop-in/.git/objects/46/
 extracting: drop-in/.git/objects/46/72a5cadb0c545e90d476f0783c9d0874512b0e  
   creating: drop-in/.git/objects/83/
 extracting: drop-in/.git/objects/83/95824cc0ce486d1be9ab874bfedb2cec2ea398  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/main  
   creating: drop-in/.git/logs/refs/heads/feature/
  inflating: drop-in/.git/logs/refs/heads/feature/part-1  
  inflating: drop-in/.git/logs/refs/heads/feature/part-2  
  inflating: drop-in/.git/logs/refs/heads/feature/part-3  
  inflating: drop-in/flag.py         
ehc_le_dinh_van-picoctf@webshell:~/ColDev$ git branch -a

[9]+  Stopped                 git branch -a
ehc_le_dinh_van-picoctf@webshell:~/ColDev$ cd drop-in/
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git branch -a
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git branch feature/part-3
fatal: A branch named 'feature/part-3' already exists.
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git checkout feature/part-3
Switched to branch 'feature/part-3'
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ ls -la
total 8
drwxr-xr-x 3 ehc_le_dinh_van-picoctf ehc_le_dinh_van-picoctf  51 Mar 15 09:44 .
drwxrwxr-x 3 ehc_le_dinh_van-picoctf ehc_le_dinh_van-picoctf  42 Mar 15 09:41 ..
drwxr-xr-x 8 ehc_le_dinh_van-picoctf ehc_le_dinh_van-picoctf 166 Mar 15 09:44 .git
-rw-rw-r-- 1 ehc_le_dinh_van-picoctf ehc_le_dinh_van-picoctf  58 Mar 15 09:44 branch.txt
-rw-rw-r-- 1 ehc_le_dinh_van-picoctf ehc_le_dinh_van-picoctf  55 Mar 15 09:44 flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git checkout feature/part-2
Switched to branch 'feature/part-2'
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ ls
branch.txt  flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano branch.txt 
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py 
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git checkout feature/part-1
Switched to branch 'feature/part-1'
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ ls
branch.txt  flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git checkout main 
Switched to branch 'main'
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge feature/part-1
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git branch -d feature/part-1
Deleted branch feature/part-1 (was 0cd57e0).
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge feature/part-2
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   flag.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        branch.txt
        flagt.txt

no changes added to commit (use "git add" and/or "git commit -a")
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ ls
branch.txt  flag.py  flagt.txt
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git branch -a

[10]+  Stopped                 git branch -a
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   flag.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        branch.txt
        flagt.txt

no changes added to commit (use "git add" and/or "git commit -a")
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git abort
git: 'abort' is not a git command. See 'git --help'.
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge --abort 
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge feature/part-3
Auto-merging flag.py
CONFLICT (content): Merge conflict in flag.py
Automatic merge failed; fix conflicts and then commit the result.
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   flag.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        branch.txt
        flagt.txt

no changes added to commit (use "git add" and/or "git commit -a")
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge --abort 
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ rm flag
rm: cannot remove 'flag': No such file or directory
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ ls
flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge feature/part-2
Auto-merging flag.py
CONFLICT (content): Merge conflict in flag.py
Automatic merge failed; fix conflicts and then commit the result.
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   flag.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        flagt.txt

no changes added to commit (use "git add" and/or "git commit -a")
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git add flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git status
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   flag.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        flagt.txt

ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git commit
[main 60e305e] Merge branch 'feature/part-2'
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git branch -d feature/part-2
Deleted branch feature/part-2 (was 7064732).
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git merge feature/part-3 
Auto-merging flag.py
CONFLICT (content): Merge conflict in flag.py
Automatic merge failed; fix conflicts and then commit the result.
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ nano flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git add flag.py
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git status
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   flag.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        flagt.txt

ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ git commit -m "done"
[main 94b5b39] done
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ python3 
.git/    flag.py  
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$ python3 flag.py 
Printing the flag...
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_2c91ca76}
ehc_le_dinh_van-picoctf@webshell:~/ColDev/drop-in$
```
[Cách xử lý](https://www.w3schools.com/git/git_branch_merge.asp?remote=github)

Flag: `picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_2c91ca76}`
