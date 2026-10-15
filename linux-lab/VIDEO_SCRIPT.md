---
title: "Linux Lab – Video Script"
subtitle: "GIK2NV · Bilal, Ali, Merat, Hussein"
---

# Quick rundown

1. **Before the call (Ali):** open Ubuntu and run `sudo -i`. If you've practised since the last reset, run the reset block at the end of this document. Then run `clear` and zoom in with Ctrl + scroll.
2. **Start the Teams or Zoom call**, share **only the Ubuntu window** and press **Record**.
3. Each speaker explains a step and says **"Ali, run it"**. Ali pastes the block, and the speaker explains the output.
4. **Stop recording** and watch it once.
5. **Upload to YouTube as Unlisted**, then add the link, last names and DU-IDs to the report, save it as a PDF and submit it on Learn.

| Order | Speaker | Section |
|---|---|---|
| 1 | Bilal | Intro + Part 1 tasks 1–3 |
| 2 | Ali | Part 1 tasks 4–5 |
| 3 | Merat | Part 1 task 6 + the script code |
| 4 | Hussein | Running and testing the script + ending |

# 1. BILAL: intro and tasks 1–3

**Say:** "Hi, we're Bilal, Ali, Merat and Hussein, and this is our Linux lab for GIK2NV. In Part 1 we're Linux admins for a company with three new departments: Engineering, Sales and HR. In Part 2 we write a script that automates user management. First we create one folder per department under root. Ali, run it."

```
cd /
mkdir /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**Say:** "The three folders now exist under root. Next, one group per department. Ali, run it."

```
groupadd Engineering
groupadd Sales
groupadd HR
getent group Engineering Sales HR
```

**Say:** "getent shows the groups exist. Now one admin per department. Ali, run it."

```
useradd -m -s /bin/bash -g Engineering eng_admin
useradd -m -s /bin/bash -g Sales sales_admin
useradd -m -s /bin/bash -g HR hr_admin
id eng_admin
```

**Say:** "-m creates a home folder, -s /bin/bash gives a Bash login shell, and -g sets the department as the primary group. id shows eng_admin's group is Engineering. Ali takes over."

# 2. ALI: tasks 4–5

**Say:** "Now two more users per department."

```
useradd -m -s /bin/bash -g Engineering eng_user1
useradd -m -s /bin/bash -g Engineering eng_user2
useradd -m -s /bin/bash -g Sales sales_user1
useradd -m -s /bin/bash -g Sales sales_user2
useradd -m -s /bin/bash -g HR hr_user1
useradd -m -s /bin/bash -g HR hr_user2
grep -E '_admin|_user' /etc/passwd
```

**Say:** "All nine users have /bin/bash. Now we secure the folders."

```
chown eng_admin:Engineering /Engineering
chown sales_admin:Sales /Sales
chown hr_admin:HR /HR
chmod 1770 /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**Say:** "chown makes the admin the owner and the department the group. In chmod 1770, the 1 is the sticky bit, so only a file's owner can delete it. The two 7s give full access to the admin and to the department, and the 0 means no access for anyone else. The T at the end shows the sticky bit. Let's test it."

```
su - eng_user1 -c 'touch /Engineering/user1_file && echo "eng_user1: file created"'
su - eng_user2 -c 'rm -f /Engineering/user1_file'
su - eng_user1 -c 'rm /Engineering/user1_file && echo "eng_user1: own file deleted"'
su - sales_user1 -c 'ls /Engineering'
```

**Say:** "eng_user1 can create a file. eng_user2 is in the same department but can't delete it, which is the sticky bit. The owner can delete their own file, and Sales can't open Engineering at all. Over to Merat."

# 3. MERAT: task 6 and the script code

**Say:** "Now a confidential file in each folder. Ali, run it."

```
for d in Engineering Sales HR; do echo "This file contains confidential information for the department." > /$d/confidential.txt; done
chown eng_admin:Engineering /Engineering/confidential.txt
chown sales_admin:Sales /Sales/confidential.txt
chown hr_admin:HR /HR/confidential.txt
chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
ls -l /Engineering /Sales /HR
```

**Say:** "Each file has one line of text and the same owner as its folder. In chmod 640, 6 lets the admin read and write, 4 lets the department only read, and 0 gives nobody else access. Let's test it. Ali, run it."

```
su - eng_user1 -c 'cat /Engineering/confidential.txt'
su - eng_user1 -c 'echo changed >> /Engineering/confidential.txt'
su - eng_admin -c 'echo "This file contains confidential information for the department." > /Engineering/confidential.txt && echo "eng_admin: file modified"'
su - sales_user1 -c 'cat /Engineering/confidential.txt'
```

**Say:** "A user can read it but not change it. The admin can change it, and Sales can't even read it. That's Part 1. Now our script. Ali, show it."

```
cd ~
cat usermgmt.sh
```

*(Ali scrolls slowly.)*

**Say:** "read asks for the names, so nothing is hardcoded. getent checks whether the group or user already exists. $? is the exit code of the last command, and 0 means it was found, so we print an error and the loop asks again. useradd creates the user with Bash and the new group. The password is read hidden with read -s and set with chpasswd. usermod -aG adds the user to the group. Then mkdir creates /username, chown sets the owner, and chmod 1770 gives full control to the owner and group, plus the sticky bit. Hussein will run it."

# 4. HUSSEIN: running and testing the script

**Say:** "First, the script must be executable. Ali, run it."

```
chmod -x usermgmt.sh
ls -l usermgmt.sh
chmod +x usermgmt.sh
ls -l usermgmt.sh
```

**Say:** "Without x it can't run. chmod +x makes it executable. Now let's run it."

```
./usermgmt.sh
```

| Ali types | Hussein says |
|---|---|
| `HR` | "HR already exists, so we get an error." |
| `Marketing` | "New name, so the group is created." |
| `eng_admin` | "That user exists, so we get an error." |
| `anna` | "New user, so it's created." |
| `abc123` | "The password is hidden while typing." |
| `wrong` | "They don't match, so it asks again." |
| `abc123` | |
| `abc123` | "The password is set." |

**Say:** "The summary shows anna is in Marketing with a Bash shell, and /anna is owned by her with drwxrwx--T. Let's verify. Ali, run it."

```
grep Marketing /etc/group
grep anna /etc/shadow | cut -c1-30
su - anna -c 'touch /anna/test && ls -l /anna'
su - eng_user1 -c 'ls /anna'
```

**Say:** "anna is a member of Marketing, and her password is saved as a hash. She can use her folder, and others are denied. Both parts work as required. Thanks for watching!"

**Ali stops the recording.**

# Reset (only if you need to start over)

```
for u in eng_admin eng_user1 eng_user2 sales_admin sales_user1 sales_user2 hr_admin hr_user1 hr_user2 anna bob; do userdel -r $u 2>/dev/null; done
for g in Engineering Sales HR Marketing Support; do groupdel $g 2>/dev/null; done
rm -r /Engineering /Sales /HR /anna /bob
clear
```
