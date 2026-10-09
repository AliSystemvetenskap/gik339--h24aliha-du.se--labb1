# Video script (about 8–10 minutes)

Split the parts between the group members so everyone talks. Share your screen with a Linux terminal open, and type the commands as you explain them.

## Person 1: intro and Part 1, tasks 1–4 (about 3 min)
- "This is our Linux lab for GIK2NV. We're the admins for a company with three new departments: Engineering, Sales and HR."
- Type `mkdir /Engineering /Sales /HR` and run `ls -ld`: "One folder per department at the root."
- Type `groupadd` for each department and run `getent group`: "One group per department."
- Type `useradd -m -s /bin/bash -g Engineering eng_admin`:
  - "`-m` creates the home folder."
  - "`-s /bin/bash` gives a Bash login shell."
  - "`-g` makes the department the primary group."
- Create the other users and show the result with `id`.

## Person 2: Part 1, tasks 5–6 (about 3 min)
- `chown eng_admin:Engineering /Engineering`: "The admin is the owner and the department is the group."
- `chmod 1770`:
  - "The 1 is the sticky bit, so only a file's owner can delete it."
  - "7 gives the owner full access, 7 gives the group full access, and 0 means nobody else gets in."
- Run the tests: eng_user2 can't delete eng_user1's file, and sales_user1 gets "Permission denied" on /Engineering.
- Create confidential.txt and run `chmod 640`: "The admin can read and write, the group can only read, and others get nothing."
- Show that the user can read the file but not edit it, the admin can edit it, and other departments are denied.

## Person 3: Part 2, the script (about 3–4 min)
- Open `usermgmt.sh` and walk through it:
  - "The script uses `read` to ask for the names, so nothing is hardcoded."
  - "`getent` checks whether the name exists. `$?` is the exit code of the last command, and 0 means it was found, so we print an error and ask again."
  - "Then useradd with a Bash shell and the new group, chpasswd for the password, and usermod -aG for membership."
  - "Then mkdir /username, chown, and chmod 1770: full control for the owner and the group, plus the sticky bit."
- `chmod +x usermgmt.sh`, then run `./usermgmt.sh`:
  - type HR (error), then Marketing
  - type eng_admin (error), then anna
  - type mismatched passwords, then matching ones
- Verify with `grep Marketing /etc/group`, `id anna` and `ls -ld /anna`.
- "That's our lab. Thanks!"
