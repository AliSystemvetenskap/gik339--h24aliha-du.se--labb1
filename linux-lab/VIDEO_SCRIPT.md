# Video script: Bilal, Ali, Merat, Hussein (about 10–12 minutes)

**Ali shares his screen and pastes every command for the whole video.** Bilal, Merat and Hussein only talk; Ali also talks during his own section.

How each block works:
1. The speaker says what the next step does, then says **"Ali, run it"**.
2. Ali pastes the block and presses Enter.
3. The speaker explains the output on screen.

Ali: keep this file open beside the Ubuntu window, or on your phone, so you can copy each block quickly.

Before recording: run the reset commands (see "How to record") so the system starts empty, then run `sudo -i` so the prompt shows `root@Ali:...#`.

---

## 1. Bilal: intro and Part 1, tasks 1–3 (about 3 min)

**Say:** "Hi, we're Bilal, Ali, Merat and Hussein, and this is our Linux lab for GIK2NV. In Part 1 we're the Linux admins for a company with three new departments: Engineering, Sales and HR. In Part 2 we write a script that automates user management."

**Task 1: folders**
```
cd /
mkdir /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```
**Say:** "First we create one directory per department directly under root, using mkdir. ls -ld shows they exist."

**Task 2: groups**
```
groupadd Engineering
groupadd Sales
groupadd HR
getent group Engineering Sales HR
```
**Say:** "Then one group per department with groupadd. getent shows the groups exist in /etc/group."

**Task 3: admins**
```
useradd -m -s /bin/bash -g Engineering eng_admin
useradd -m -s /bin/bash -g Sales sales_admin
useradd -m -s /bin/bash -g HR hr_admin
id eng_admin
```
**Say:** "Now one admin per department with useradd. -m creates a home directory, -s /bin/bash gives a Bash login shell, and -g sets the department as the primary group. id shows that eng_admin's primary group, gid, is Engineering. Now Ali takes over."

---

## 2. Ali: Part 1, tasks 4–5 (about 3 min)

**Task 4: regular users**
```
useradd -m -s /bin/bash -g Engineering eng_user1
useradd -m -s /bin/bash -g Engineering eng_user2
useradd -m -s /bin/bash -g Sales sales_user1
useradd -m -s /bin/bash -g Sales sales_user2
useradd -m -s /bin/bash -g HR hr_user1
useradd -m -s /bin/bash -g HR hr_user2
grep -E '_admin|_user' /etc/passwd
```
**Say:** "Two more users per department, with the same options: Bash shell and the department as primary group. In /etc/passwd you can see all nine users end with /bin/bash."

**Task 5: ownership and permissions**
```
chown eng_admin:Engineering /Engineering
chown sales_admin:Sales /Sales
chown hr_admin:HR /HR
chmod 1770 /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```
**Say:** "chown makes the admin the owner and the department the group owner. Then chmod 1770:
- The 1 is the sticky bit, so only a file's owner can delete it.
- The first 7 gives the admin full access.
- The second 7 gives the department users full access.
- The 0 means nobody else has any access.

The T at the end of the permissions shows the sticky bit."

**Test**
```
su - eng_user1 -c 'touch /Engineering/user1_file && echo "eng_user1: file created"'
su - eng_user2 -c 'rm -f /Engineering/user1_file'
su - eng_user1 -c 'rm /Engineering/user1_file && echo "eng_user1: own file deleted"'
su - sales_user1 -c 'ls /Engineering'
```
**Say:**
- "eng_user1 can create a file in the folder."
- "eng_user2, who is in the same department, gets 'Operation not permitted' when trying to delete it. That's the sticky bit."
- "The owner can delete their own file."
- "A Sales user gets 'Permission denied' and can't even open the Engineering folder."

"Over to Merat."

---

## 3. Merat: Part 1, task 6, and Part 2 explained (about 3 min)

**Task 6: confidential file**
```
for d in Engineering Sales HR; do echo "This file contains confidential information for the department." > /$d/confidential.txt; done
chown eng_admin:Engineering /Engineering/confidential.txt
chown sales_admin:Sales /Sales/confidential.txt
chown hr_admin:HR /HR/confidential.txt
chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
ls -l /Engineering /Sales /HR
```
**Say:** "We create a file with one line of text in each department folder. It gets the same owner and group as the folder. chmod 640 means:
- 6: the admin can read and write.
- 4: the department can only read.
- 0: nobody else has access."

**Test**
```
su - eng_user1 -c 'cat /Engineering/confidential.txt'
su - eng_user1 -c 'echo changed >> /Engineering/confidential.txt'
su - eng_admin -c 'echo "This file contains confidential information for the department." > /Engineering/confidential.txt && echo "eng_admin: file modified"'
su - sales_user1 -c 'cat /Engineering/confidential.txt'
```
**Say:** "A user can read the file but gets 'Permission denied' when trying to change it. The admin can change it. Another department can't even read it. That's Part 1 done."

**Part 2: show the script**
```
cd ~
cat usermgmt.sh
```
Scroll slowly while talking.

**Say:**
- "This is our Part 2 script. It uses read to ask for the names, so no names are hardcoded."
- "For the group, getent group checks whether the name already exists. The special variable $? holds the exit code of the last command: 0 means it was found. Then we print an error, and the while loop asks again. Otherwise groupadd creates the group."
- "The user step works the same way with getent passwd. useradd gives a Bash shell and the new group as primary group."
- "The password is read twice with read -s, so it's hidden, and it's set with chpasswd."
- "Then usermod -aG makes sure the user is a member of the group. mkdir creates /username at the root, chown sets the owner and group, and chmod 1770 gives full control to the owner and group plus the sticky bit."

"Hussein will run it."

---

## 4. Hussein: Part 2, running and testing (about 3 min)

**Executable**
```
chmod -x usermgmt.sh
ls -l usermgmt.sh
chmod +x usermgmt.sh
ls -l usermgmt.sh
```
**Say:** "Without x the script isn't executable. chmod +x makes it executable. You can see the x in rwxr-xr-x."

**Run it**
```
./usermgmt.sh
```
Type the answers one at a time:

| Type | Say |
|---|---|
| `HR` | "HR already exists, so the script gives an error and asks again." |
| `Marketing` | "Marketing is new, so the group is created." |
| `eng_admin` | "That user already exists, so we get an error." |
| `anna` | "anna is new, so the user is created." |
| `abc123` | "The password is hidden while typing." |
| `wrong` | "The passwords don't match, so it asks again." |
| `abc123` | |
| `abc123` | "Now the password is set." |

**Say:** "The summary shows anna's primary group is Marketing, her shell is bash, and /anna is owned by anna and Marketing with drwxrwx--T."

**Verify**
```
grep Marketing /etc/group
grep anna /etc/shadow | cut -c1-30
su - anna -c 'touch /anna/test && ls -l /anna'
su - eng_user1 -c 'ls /anna'
```
**Say:** "anna is a member of Marketing, and her password is stored as a hash in /etc/shadow. She can create files in her folder, and other users are denied."

**Ending (Hussein, or everyone together):** "So both parts work as required. Thanks for watching!"
