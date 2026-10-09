---
title: "Linux Laboratory – Part 1 & Part 2"
subtitle: "GIK2NV – Data storage and management technologies"
date: "[DATE]"
author:
  - "[Name 1] – [DU-ID]"
  - "[Name 2] – [DU-ID]"
  - "[Name 3] – [DU-ID]"
---

**Video recording:** [YouTube link]

# Part 1 – User Management

All commands are run as root (`sudo`). The full script is `part1_setup.sh`.

Naming used:

| Department | Group | Admin | Users |
|---|---|---|---|
| Engineering | Engineering | eng_admin | eng_user1, eng_user2 |
| Sales | Sales | sales_admin | sales_user1, sales_user2 |
| HR | HR | hr_admin | hr_user1, hr_user2 |

## 1. Create a directory at the root (/) for each department

We change to the root of the file system and create one directory per department.

```
cd /
sudo mkdir /Engineering /Sales /HR
```

Verification: `ls -ld /Engineering /Sales /HR`

[SCREENSHOT]

## 2. Create a group for each department

```
sudo groupadd Engineering
sudo groupadd Sales
sudo groupadd HR
```

Verification: `getent group Engineering Sales HR`

```
Engineering:x:30002:
Sales:x:30003:
HR:x:30004:
```

[SCREENSHOT]

## 3. Create an administrative user for each department

`-m` creates a home directory, `-s /bin/bash` gives a Bash login shell (3a) and `-g` sets the department group as the user's **primary** group (3b).

```
sudo useradd -m -s /bin/bash -g Engineering eng_admin
sudo useradd -m -s /bin/bash -g Sales sales_admin
sudo useradd -m -s /bin/bash -g HR hr_admin
```

Verification: `id eng_admin` and `getent passwd eng_admin`

```
uid=30033(eng_admin) gid=30002(Engineering) groups=30002(Engineering)
eng_admin:/bin/bash
```

[SCREENSHOT]

## 4. Create two additional users for each department

Same options as for the admins: Bash login shell (4a) and the department as primary group (4b).

```
sudo useradd -m -s /bin/bash -g Engineering eng_user1
sudo useradd -m -s /bin/bash -g Engineering eng_user2
sudo useradd -m -s /bin/bash -g Sales sales_user1
sudo useradd -m -s /bin/bash -g Sales sales_user2
sudo useradd -m -s /bin/bash -g HR hr_user1
sudo useradd -m -s /bin/bash -g HR hr_user2
```

Verification: `id <user>` for every user, and `tail -9 /etc/passwd`

```
uid=30036(eng_user1) gid=30002(Engineering) groups=30002(Engineering)
uid=30037(eng_user2) gid=30002(Engineering) groups=30002(Engineering)
uid=30038(sales_user1) gid=30003(Sales) groups=30003(Sales)
uid=30039(sales_user2) gid=30003(Sales) groups=30003(Sales)
uid=30040(hr_user1) gid=30004(HR) groups=30004(HR)
uid=30041(hr_user2) gid=30004(HR) groups=30004(HR)
```

[SCREENSHOT]

## 5. Secure the department directories

**5a.** The department admin is set as owner and the department group as group owner:

```
sudo chown eng_admin:Engineering /Engineering
sudo chown sales_admin:Sales /Sales
sudo chown hr_admin:HR /HR
```

**5b–5e.** Permissions are set with one command: `chmod 1770`

| Digit | Meaning | Objective |
|---|---|---|
| 1 | sticky bit – only a file's owner can delete it | 5c |
| 7 | owner (admin) rwx – full access | 5b |
| 7 | group (department users) rwx – full access | 5d |
| 0 | others – no permissions at all | 5e |

```
sudo chmod 1770 /Engineering /Sales /HR
```

Verification: `ls -ld /Engineering /Sales /HR` – the `T` at the end shows the sticky bit.

```
drwxrwx--T 2 eng_admin   Engineering 4096 /Engineering
drwxrwx--T 2 hr_admin    HR          4096 /HR
drwxrwx--T 2 sales_admin Sales       4096 /Sales
```

Tests:

```
# Department user can create files in their folder (5d)
su - eng_user1 -c 'touch /Engineering/u1file && echo created'
created

# Another user in the department cannot delete it (sticky bit, 5c)
su - eng_user2 -c 'rm -f /Engineering/u1file'
rm: cannot remove '/Engineering/u1file': Operation not permitted

# A user from another department has no access (5e)
su - eng_user1 -c 'ls /Sales'
ls: cannot open directory '/Sales': Permission denied
```

[SCREENSHOT]

## 6. Create a document in each department directory

**6b.** The file contains exactly one line:

```
echo "This file contains confidential information for the department." > /Engineering/confidential.txt
echo "This file contains confidential information for the department." > /Sales/confidential.txt
echo "This file contains confidential information for the department." > /HR/confidential.txt
```

**6a.** Same ownership as the directory:

```
sudo chown eng_admin:Engineering /Engineering/confidential.txt
sudo chown sales_admin:Sales /Sales/confidential.txt
sudo chown hr_admin:HR /HR/confidential.txt
```

**6c.** `chmod 640` – owner (admin) read + write, group read only, others nothing:

```
sudo chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
```

Verification: `ls -l /Engineering /Sales /HR`

```
-rw-r----- 1 eng_admin Engineering 64 confidential.txt
-rw-r----- 1 hr_admin HR 64 confidential.txt
-rw-r----- 1 sales_admin Sales 64 confidential.txt
```

Tests:

```
# Department user can read
su - eng_user1 -c 'cat /Engineering/confidential.txt'
This file contains confidential information for the department.

# Department user cannot modify
su - eng_user1 -c 'echo x >> /Engineering/confidential.txt'
-bash: /Engineering/confidential.txt: Permission denied

# Admin can modify
su - eng_admin -c 'echo "This file contains confidential information for the department." > /Engineering/confidential.txt && echo admin-write-ok'
admin-write-ok

# User from another department cannot read
su - sales_user1 -c 'cat /Engineering/confidential.txt'
cat: /Engineering/confidential.txt: Permission denied
```

[SCREENSHOT]

# Part 2 – User Management Script

## How the script works

The script `usermgmt.sh` is interactive and does not hardcode any names – the administrator types in the group name, username and password when it runs. Step by step:

0. **Root check** – the script stops with an error if it is not run as root, since all following commands need root.
1. **(a) Create group** – a `while` loop asks for a group name. `getent group <name>` looks the name up; the special variable `$?` holds the exit code of the previous command (0 = found). If the group already exists an error is printed and the loop asks again. Otherwise `groupadd` creates it and `$?` is checked again to confirm success.
2. **(b) Create user** – same loop pattern with `getent passwd <name>`. A unique name is created with `useradd -m -s /bin/bash -g <group> <user>`: Bash login shell and the new group as primary group.
3. **(c) Password** – the password is read twice with `read -s` (hidden input). If empty or not matching, the admin tries again. It is set with `chpasswd`.
4. **(d) Group membership** – `usermod -aG <group> <user>` also adds the user as a member of the group (listed in `/etc/group`).
5. **(e) Directory** – `mkdir /<username>` creates a directory at the root with the same name as the user.
6. **(f) Ownership** – `chown <user>:<group> /<username>`.
7. **(g + h) Permissions** – `chmod 1770`: owner rwx, group rwx (full control), others none, plus the sticky bit so only a file's owner can delete it.
8. **Summary** – prints `id`, the `/etc/passwd` entry and `ls -ld` of the directory as proof.
9. **(i) Executable** – the script is made executable with `chmod +x usermgmt.sh` and run as `sudo ./usermgmt.sh`.

Logical order matters: the group must exist before the user (because it is the user's primary group), and the user and group must exist before `chown` on the directory.

## Script implementation

[SCREENSHOT of `cat usermgmt.sh` / the script in the editor]

## Testing

Test run that covers every branch: an existing group (`HR`), an existing user (`eng_admin`), a password mismatch, and finally valid input.

```
$ ls -l usermgmt.sh
-rwxr-xr-x 1 root root ... usermgmt.sh          <- (i) executable

$ sudo ./usermgmt.sh
Enter a new group name: HR
Error: group 'HR' already exists. Try another group name.
Enter a new group name: Marketing
Group 'Marketing' created.
Enter a new username: eng_admin
Error: user 'eng_admin' already exists. Try another username.
Enter a new username: anna
User 'anna' created.
Enter a password for anna:
Confirm password:
Error: passwords do not match. Try again.
Enter a password for anna:
Confirm password:
Password set for 'anna'.
User 'anna' is a member of group 'Marketing'.
Directory /anna created.
Ownership and permissions set on /anna.

===== Summary =====
uid=30042(anna) gid=30005(Marketing) groups=30005(Marketing)
anna:x:30042:30005::/home/anna:/bin/bash
drwxrwx--T 2 anna Marketing 4096 /anna
```

Extra verification:

```
$ grep Marketing /etc/group            # (a, d)
Marketing:x:30005:anna

$ sudo grep anna /etc/shadow           # (c) password hash exists
anna:$y$j9T$...

$ su - anna -c 'touch /anna/test && ls -l /anna'   # (e, f, g)
-rw-r--r-- 1 anna Marketing 0 test
```

[SCREENSHOTS]
