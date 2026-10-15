---
title: "Kommandon att köra – Linux Lab"
---

Kopiera ett block i taget → högerklicka i Ubuntu → Enter. Vänta på "Ali, run it" innan nästa block.

# BILAL

**Block 1 – mappar**

```
cd /
mkdir /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**Block 2 – grupper**

```
groupadd Engineering
groupadd Sales
groupadd HR
getent group Engineering Sales HR
```

**Block 3 – admins**

```
useradd -m -s /bin/bash -g Engineering eng_admin
useradd -m -s /bin/bash -g Sales sales_admin
useradd -m -s /bin/bash -g HR hr_admin
id eng_admin
```

# ALI

**Block 4 – användare**

```
useradd -m -s /bin/bash -g Engineering eng_user1
useradd -m -s /bin/bash -g Engineering eng_user2
useradd -m -s /bin/bash -g Sales sales_user1
useradd -m -s /bin/bash -g Sales sales_user2
useradd -m -s /bin/bash -g HR hr_user1
useradd -m -s /bin/bash -g HR hr_user2
grep -E '_admin|_user' /etc/passwd
```

**Block 5 – rättigheter**

```
chown eng_admin:Engineering /Engineering
chown sales_admin:Sales /Sales
chown hr_admin:HR /HR
chmod 1770 /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**Block 6 – test**

```
su - eng_user1 -c 'touch /Engineering/user1_file && echo "eng_user1: file created"'
su - eng_user2 -c 'rm -f /Engineering/user1_file'
su - eng_user1 -c 'rm /Engineering/user1_file && echo "eng_user1: own file deleted"'
su - sales_user1 -c 'ls /Engineering'
```

# MERAT

**Block 7 – hemliga filer**

```
for d in Engineering Sales HR; do echo "This file contains confidential information for the department." > /$d/confidential.txt; done
chown eng_admin:Engineering /Engineering/confidential.txt
chown sales_admin:Sales /Sales/confidential.txt
chown hr_admin:HR /HR/confidential.txt
chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
ls -l /Engineering /Sales /HR
```

**Block 8 – test**

```
su - eng_user1 -c 'cat /Engineering/confidential.txt'
su - eng_user1 -c 'echo changed >> /Engineering/confidential.txt'
su - eng_admin -c 'echo "This file contains confidential information for the department." > /Engineering/confidential.txt && echo "eng_admin: file modified"'
su - sales_user1 -c 'cat /Engineering/confidential.txt'
```

**Block 9 – visa scriptet** (scrolla långsamt uppåt)

```
cd ~
cat usermgmt.sh
```

# HUSSEIN

**Block 10 – körbart**

```
chmod -x usermgmt.sh
ls -l usermgmt.sh
chmod +x usermgmt.sh
ls -l usermgmt.sh
```

**Block 11 – kör scriptet**

```
./usermgmt.sh
```

Skriv svaren ETT i taget (Enter efter varje):

1. HR
2. Marketing
3. eng_admin
4. anna
5. abc123
6. wrong
7. abc123
8. abc123

**Block 12 – verifiera**

```
grep Marketing /etc/group
grep anna /etc/shadow | cut -c1-30
su - anna -c 'touch /anna/test && ls -l /anna'
su - eng_user1 -c 'ls /anna'
```

# RESET (bara om ni måste börja om)

```
for u in eng_admin eng_user1 eng_user2 sales_admin sales_user1 sales_user2 hr_admin hr_user1 hr_user2 anna bob; do userdel -r $u 2>/dev/null; done
for g in Engineering Sales HR Marketing Support; do groupdel $g 2>/dev/null; done
rm -r /Engineering /Sales /HR /anna /bob
clear
```
