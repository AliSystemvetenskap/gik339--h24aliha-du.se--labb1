---
title: "Linux Lab – Enkelt videomanus"
subtitle: "GIK2NV · Bilal, Ali, Merat, Hussein"
---

# Så funkar det

- **Ali** delar Ubuntu-fönstret och kör alla kommandon.
- Den som pratar läser sin **"Say"**-text på engelska och säger **"Ali, run it"**.
- Ali klistrar in blocket, och personen förklarar vad som syns.
- Under varje block står **"Vad betyder det?"** på svenska, så att alla förstår vad de pratar om. Den texten läser ni **inte** upp.

| Ordning | Vem | Del |
|---|---|---|
| 1 | Bilal | Intro, mappar, grupper, admins |
| 2 | Ali | Användare, rättigheter, test |
| 3 | Merat | Hemlig fil, test, scriptet |
| 4 | Hussein | Kör scriptet och testar |

# 1. BILAL

## Intro

**Say:** "Hi! We are Bilal, Ali, Merat and Hussein. This is our Linux lab. A company has three new departments: Engineering, Sales and HR. In Part 1 we set up folders, groups and users for them. In Part 2 we made a script that does this automatically."

## Block 1: mappar

**Say:** "First we make one folder for each department. Ali, run it."

```
cd /
mkdir /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**Vad betyder det?** `cd /` går till roten, den översta mappen i Linux. `mkdir` skapar mappar. `ls -ld` visar mapparna så vi ser att de finns.

**Say:** "Here you can see the three folders. They are in the root of the system."

## Block 2: grupper

**Say:** "Now we make one group for each department. Ali, run it."

```
groupadd Engineering
groupadd Sales
groupadd HR
getent group Engineering Sales HR
```

**Vad betyder det?** En grupp är som ett "lag". Alla som jobbar på samma avdelning ska vara i samma grupp. `groupadd` skapar gruppen, och `getent group` visar att den finns.

**Say:** "Here you can see the three groups were created."

## Block 3: chefer (admins)

**Say:** "Now we make one boss, an admin, for each department. Ali, run it."

```
useradd -m -s /bin/bash -g Engineering eng_admin
useradd -m -s /bin/bash -g Sales sales_admin
useradd -m -s /bin/bash -g HR hr_admin
id eng_admin
```

**Vad betyder det?** `useradd` skapar en användare.

- `-m` ger användaren en egen hemmapp.
- `-s /bin/bash` gör att användaren använder Bash när den loggar in.
- `-g Engineering` gör Engineering till användarens huvudgrupp.

`id` visar vilken grupp användaren har.

**Say:** "useradd makes a new user. -s /bin/bash gives the user a Bash shell. -g puts the user in the department group. Here you can see eng_admin is in the Engineering group. Now Ali takes over."

# 2. ALI

## Block 4: vanliga användare

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

**Vad betyder det?** Samma som förut, fast för vanliga anställda. `/etc/passwd` är listan över alla användare, och `grep` letar fram våra 9 användare.

**Say:** "Here are all nine users. They all end with /bin/bash, so they all have a Bash shell."

## Block 5: rättigheter

**Say:** "Now we protect the folders."

```
chown eng_admin:Engineering /Engineering
chown sales_admin:Sales /Sales
chown hr_admin:HR /HR
chmod 1770 /Engineering /Sales /HR
ls -ld /Engineering /Sales /HR
```

**Vad betyder det?** `chown` bestämmer vem som äger mappen: chefen äger den, och avdelningens grupp hör till den. `chmod 1770` bestämmer vem som får göra vad:

- **1** = sticky bit: bara den som skapat en fil får ta bort den.
- **7** = chefen får göra allt.
- **7** = avdelningen får göra allt.
- **0** = alla andra får ingenting.

I `drwxrwx--T` betyder `T` att sticky bit är på.

**Say:** "chown makes the boss the owner of the folder. chmod 1770 sets the rules. The boss and the department can do everything. Everyone else can do nothing. The 1 is the sticky bit. It means only the person who made a file can delete it. You can see the T at the end. That is the sticky bit."

## Block 6: test

**Say:** "Let's test it."

```
su - eng_user1 -c 'touch /Engineering/user1_file && echo "eng_user1: file created"'
su - eng_user2 -c 'rm -f /Engineering/user1_file'
su - eng_user1 -c 'rm /Engineering/user1_file && echo "eng_user1: own file deleted"'
su - sales_user1 -c 'ls /Engineering'
```

**Vad betyder det?** `su - användare -c '...'` kör ett kommando som om man vore den användaren.

1. eng_user1 skapar en fil. ✅
2. eng_user2 försöker ta bort den. ❌ Det går inte, tack vare sticky bit.
3. eng_user1 tar bort sin egen fil. ✅
4. Någon från Sales försöker öppna Engineering-mappen. ❌ Nekad.

**Say:** "User 1 can make a file. User 2 is in the same department, but he cannot delete it. That is the sticky bit. User 1 can delete his own file. And a Sales user cannot open the Engineering folder. Over to Merat."

# 3. MERAT

## Block 7: hemlig fil

**Say:** "Now we put a secret file in each folder. Ali, run it."

```
for d in Engineering Sales HR; do echo "This file contains confidential information for the department." > /$d/confidential.txt; done
chown eng_admin:Engineering /Engineering/confidential.txt
chown sales_admin:Sales /Sales/confidential.txt
chown hr_admin:HR /HR/confidential.txt
chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
ls -l /Engineering /Sales /HR
```

**Vad betyder det?** Första raden skriver en mening i en fil, i alla tre mapparna. `chown` gör att filen ägs av samma chef och grupp som mappen. `chmod 640` betyder:

- **6** = chefen får läsa och ändra.
- **4** = avdelningen får bara läsa.
- **0** = alla andra får ingenting.

**Say:** "We made a file with one sentence in each folder. The boss owns it. chmod 640 means the boss can read and change it, the department can only read it, and others can do nothing."

## Block 8: test

**Say:** "Let's test it. Ali, run it."

```
su - eng_user1 -c 'cat /Engineering/confidential.txt'
su - eng_user1 -c 'echo changed >> /Engineering/confidential.txt'
su - eng_admin -c 'echo "This file contains confidential information for the department." > /Engineering/confidential.txt && echo "eng_admin: file modified"'
su - sales_user1 -c 'cat /Engineering/confidential.txt'
```

**Vad betyder det?**

1. En vanlig användare läser filen. ✅
2. Samma användare försöker ändra den. ❌
3. Chefen ändrar filen. ✅
4. Någon från Sales försöker läsa den. ❌

**Say:** "A normal user can read the file, but cannot change it. The boss can change it. Sales cannot even read it. That was Part 1."

## Block 9: scriptet

**Say:** "Now Part 2, our script. Ali, show it."

```
cd ~
cat usermgmt.sh
```

**Vad betyder det?** `cat` visar vad som står i filen. Ali scrollar långsamt medan du förklarar. Scriptet gör samma sak som vi gjorde för hand, fast automatiskt:

1. Det frågar efter ett gruppnamn och kollar om det redan finns. Finns det, blir det ett fel och det frågar igen.
2. Det frågar efter ett användarnamn och kollar på samma sätt.
3. Det frågar efter lösenord två gånger.
4. Det lägger användaren i gruppen.
5. Det skapar en mapp med användarens namn och sätter rättigheter (1770).

`$?` är ett "svar" från förra kommandot: 0 betyder att det lyckades eller hittades.

**Say:** "This is our script. It asks for a group name. If the name already exists, it shows an error and asks again. We check this with getent and the special variable dollar question mark. It tells us if the last command worked. Then it does the same for the username. Then it asks for a password two times. Then it makes a folder with the user's name and gives it the right permissions. Nothing is hardcoded. You can type any name. Hussein will run it."

# 4. HUSSEIN

## Block 10: gör scriptet körbart

**Say:** "First, the script must be executable. Ali, run it."

```
chmod -x usermgmt.sh
ls -l usermgmt.sh
chmod +x usermgmt.sh
ls -l usermgmt.sh
```

**Vad betyder det?** `x` betyder att filen får köras som ett program. Först tar vi bort x (`-rw-r--r--`), sedan lägger vi till det (`-rwxr-xr-x`).

**Say:** "First there is no x, so we cannot run it. chmod +x adds the x. Now we can run the script."

## Block 11: kör scriptet

**Say:** "Now let's run it."

```
./usermgmt.sh
```

Ali skriver svaren ett i taget. Hussein säger:

| Ali skriver | Hussein säger |
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

## Block 12: kontrollera

**Say:** "Let's check that everything worked. Ali, run it."

```
grep Marketing /etc/group
grep anna /etc/shadow | cut -c1-30
su - anna -c 'touch /anna/test && ls -l /anna'
su - eng_user1 -c 'ls /anna'
```

**Vad betyder det?**

1. Anna finns med i Marketing-gruppen.
2. Anna har ett lösenord sparat. Det syns som en kod (hash), inte som riktig text.
3. Anna kan skapa filer i sin mapp. ✅
4. Andra kan inte öppna hennes mapp. ❌

**Say:** "Anna is in the Marketing group. Her password is saved. She can use her folder, and other users cannot. So everything works. Thank you for watching!"

**Ali stoppar inspelningen.**

# Reset (bara om ni måste börja om)

```
for u in eng_admin eng_user1 eng_user2 sales_admin sales_user1 sales_user2 hr_admin hr_user1 hr_user2 anna bob; do userdel -r $u 2>/dev/null; done
for g in Engineering Sales HR Marketing Support; do groupdel $g 2>/dev/null; done
rm -r /Engineering /Sales /HR /anna /bob
clear
```
