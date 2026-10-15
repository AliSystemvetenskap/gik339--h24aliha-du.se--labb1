---
title: "Linux Lab – Simple Video Script"
subtitle: "GIK2NV · Bilal, Ali, Merat, Hussein"
---

# How it works

- **Ali** shares the Ubuntu window and runs all the commands.
- The speaker reads their **"Say"** text and says **"Ali, run it"**.
- Ali pastes the block, and the speaker explains what is on the screen.
- **"What does it mean?"** under each block helps you understand what you are talking about. Do **not** read it out loud.

| Order | Who | Part |
|---|---|---|
| 1 | Bilal | Intro, folders, groups, admins |
| 2 | Ali | Users, permissions, test |
| 3 | Merat | Secret file, test, the script |
| 4 | Hussein | Runs and tests the script |

# 1. BILAL

## Intro

**Say:** "Hi! We are Bilal, Ali, Merat and Hussein. This is our Linux lab. A company has three new departments: Engineering, Sales and HR. In Part 1 we set up folders, groups and users for them. In Part 2 we made a script that does this automatically."

## Block 1: folders

**Say:** "First we make one folder for each department. Ali, run it."

```
cd /
mkdir /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**What does it mean?** `cd /` goes to the root, the top folder in Linux. `mkdir` makes folders. `ls -ld` shows the folders, so we can see they exist.

**Say:** "Here you can see the three folders. They are in the root of the system."

## Block 2: groups

**Say:** "Now we make one group for each department. Ali, run it."

```
groupadd Engineering
groupadd Sales
groupadd HR
getent group Engineering Sales HR
```

**What does it mean?** A group is like a "team". Everyone in the same department is in the same group. `groupadd` makes the group, and `getent group` shows that it exists.

**Say:** "Here you can see the three groups were created."

## Block 3: bosses (admins)

**Say:** "Now we make one boss, an admin, for each department. Ali, run it."

```
useradd -m -s /bin/bash -g Engineering eng_admin
useradd -m -s /bin/bash -g Sales sales_admin
useradd -m -s /bin/bash -g HR hr_admin
id eng_admin
```

**What does it mean?** `useradd` makes a user.

- `-m` gives the user their own home folder.
- `-s /bin/bash` means the user gets Bash when they log in.
- `-g Engineering` makes Engineering the user's main (primary) group.

`id` shows which group the user has.

**Say:** "useradd makes a new user. -s /bin/bash gives the user a Bash shell. -g puts the user in the department group. Here you can see eng_admin is in the Engineering group. Now Ali takes over."

# 2. ALI

## Block 4: normal users

**Say:** "Now we make two normal users for each department, the same way."

```
useradd -m -s /bin/bash -g Engineering eng_user1
useradd -m -s /bin/bash -g Engineering eng_user2
useradd -m -s /bin/bash -g Sales sales_user1
useradd -m -s /bin/bash -g Sales sales_user2
useradd -m -s /bin/bash -g HR hr_user1
useradd -m -s /bin/bash -g HR hr_user2
grep -E '_admin|_user' /etc/passwd
```

**What does it mean?** The same as before, but for normal employees. `/etc/passwd` is the list of all users, and `grep` finds our 9 users in it.

**Say:** "Here are all nine users. They all end with /bin/bash, so they all have a Bash shell."

## Block 5: permissions

**Say:** "Now we protect the folders."

```
chown eng_admin:Engineering /Engineering
chown sales_admin:Sales /Sales
chown hr_admin:HR /HR
chmod 1770 /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**What does it mean?** `chown` decides who owns the folder: the boss owns it, and the department group belongs to it. `chmod 1770` decides who can do what:

- **1** = sticky bit: only the person who made a file can delete it.
- **7** = the boss can do everything.
- **7** = the department can do everything.
- **0** = everyone else can do nothing.

In `drwxrwx--T`, the `T` means the sticky bit is on.

**Say:** "chown makes the boss the owner of the folder. chmod 1770 sets the rules. The boss and the department can do everything. Everyone else can do nothing. The 1 is the sticky bit. It means only the person who made a file can delete it. You can see the T at the end. That is the sticky bit."

## Block 6: test

**Say:** "Let's test it."

```
su - eng_user1 -c 'touch /Engineering/user1_file && echo "eng_user1: file created"'
su - eng_user2 -c 'rm -f /Engineering/user1_file'
su - eng_user1 -c 'rm /Engineering/user1_file && echo "eng_user1: own file deleted"'
su - sales_user1 -c 'ls /Engineering'
```

**What does it mean?** `su - user -c '...'` runs a command as if you were that user.

1. eng_user1 makes a file. ✅
2. eng_user2 tries to delete it. ❌ Not allowed, because of the sticky bit.
3. eng_user1 deletes his own file. ✅
4. Someone from Sales tries to open the Engineering folder. ❌ Denied.

**Say:** "User 1 can make a file. User 2 is in the same department, but he cannot delete it. That is the sticky bit. User 1 can delete his own file. And a Sales user cannot open the Engineering folder. Over to Merat."

# 3. MERAT

## Block 7: secret file

**Say:** "Now we put a secret file in each folder. Ali, run it."

```
for d in Engineering Sales HR; do echo "This file contains confidential information for the department." > /$d/confidential.txt; done
chown eng_admin:Engineering /Engineering/confidential.txt
chown sales_admin:Sales /Sales/confidential.txt
chown hr_admin:HR /HR/confidential.txt
chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
ls -l /Engineering /Sales /HR
```

**What does it mean?** The first line writes one sentence into a file, in all three folders. `chown` makes the file owned by the same boss and group as the folder. `chmod 640` means:

- **6** = the boss can read and change it.
- **4** = the department can only read it.
- **0** = everyone else can do nothing.

**Say:** "We made a file with one sentence in each folder. The boss owns it. chmod 640 means the boss can read and change it, the department can only read it, and others can do nothing."

## Block 8: test

**Say:** "Let's test it. Ali, run it."

```
su - eng_user1 -c 'cat /Engineering/confidential.txt'
su - eng_user1 -c 'echo changed >> /Engineering/confidential.txt'
su - eng_admin -c 'echo "This file contains confidential information for the department." > /Engineering/confidential.txt && echo "eng_admin: file modified"'
su - sales_user1 -c 'cat /Engineering/confidential.txt'
```

**What does it mean?**

1. A normal user reads the file. ✅
2. The same user tries to change it. ❌
3. The boss changes the file. ✅
4. Someone from Sales tries to read it. ❌

**Say:** "A normal user can read the file, but cannot change it. The boss can change it. Sales cannot even read it. That was Part 1."

## Block 9: the script

**Say:** "Now Part 2, our script. Ali, show it."

```
cd ~
cat usermgmt.sh
```

**What does it mean?** `cat` shows what is in the file. Ali scrolls slowly while you explain. The script does the same thing we did by hand, but automatically:

1. It asks for a group name and checks if it already exists. If it does, it shows an error and asks again.
2. It asks for a username and checks it the same way.
3. It asks for the password two times.
4. It puts the user in the group.
5. It makes a folder with the user's name and sets the permissions (1770).

`$?` is the "answer" from the last command: 0 means it worked or was found.

**Say:** "This is our script. It asks for a group name. If the name already exists, it shows an error and asks again. We check this with getent and the special variable dollar question mark. It tells us if the last command worked. Then it does the same for the username. Then it asks for a password two times. Then it makes a folder with the user's name and gives it the right permissions. Nothing is hardcoded. You can type any name. Hussein will run it."

# 4. HUSSEIN

## Block 10: make the script executable

**Say:** "First, the script must be executable. Ali, run it."

```
chmod -x usermgmt.sh
ls -l usermgmt.sh
chmod +x usermgmt.sh
ls -l usermgmt.sh
```

**What does it mean?** `x` means the file can run as a program. First we remove the x (`-rw-r--r--`), then we add it (`-rwxr-xr-x`).

**Say:** "First there is no x, so we cannot run it. chmod +x adds the x. Now we can run the script."

## Block 11: run the script

**Say:** "Now let's run it."

```
./usermgmt.sh
```

Ali types the answers one at a time. Hussein says:

| Ali types | Hussein says |
|---|---|
| HR | "HR already exists. We get an error, and it asks again." |
| Marketing | "Marketing is new, so the group is made." |
| eng_admin | "This user already exists. Error again." |
| anna | "Anna is new, so the user is made." |
| abc123 | "The password is hidden when we type." |
| wrong | "The passwords are not the same, so it asks again." |
| abc123 | |
| abc123 | "Now the password is set." |

**Say:** "At the end we see a summary. Anna is in the Marketing group, and she has a folder called /anna."

## Block 12: check

**Say:** "Let's check that everything worked. Ali, run it."

```
grep Marketing /etc/group
grep anna /etc/shadow | cut -c1-30
su - anna -c 'touch /anna/test && ls -l /anna'
su - eng_user1 -c 'ls /anna'
```

**What does it mean?**

1. Anna is a member of the Marketing group.
2. Anna has a saved password. It shows as a code (a hash), not as real text.
3. Anna can make files in her folder. ✅
4. Others cannot open her folder. ❌

**Say:** "Anna is in the Marketing group. Her password is saved. She can use her folder, and other users cannot. So everything works. Thank you for watching!"

**Ali stops the recording.**

# Reset (only if you need to start over)

```
for u in eng_admin eng_user1 eng_user2 sales_admin sales_user1 sales_user2 hr_admin hr_user1 hr_user2 anna bob; do userdel -r $u 2>/dev/null; done
for g in Engineering Sales HR Marketing Support; do groupdel $g 2>/dev/null; done
rm -r /Engineering /Sales /HR /anna /bob
clear
```
