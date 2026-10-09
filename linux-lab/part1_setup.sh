#!/bin/bash
# GIK2NV Linux Lab - Part 1
# Sets up department directories, groups, users and permissions.
# Run as root: sudo ./part1_setup.sh

# Objective 1: Create a directory at the root (/) for each department
cd /
mkdir /Engineering /Sales /HR

# Objective 2: Create a group for each department
groupadd Engineering
groupadd Sales
groupadd HR

# Objective 3: Create an administrative user for each department
# -m = create home dir, -s = login shell, -g = primary group
useradd -m -s /bin/bash -g Engineering eng_admin
useradd -m -s /bin/bash -g Sales sales_admin
useradd -m -s /bin/bash -g HR hr_admin

# Objective 4: Create two additional users for each department
useradd -m -s /bin/bash -g Engineering eng_user1
useradd -m -s /bin/bash -g Engineering eng_user2
useradd -m -s /bin/bash -g Sales sales_user1
useradd -m -s /bin/bash -g Sales sales_user2
useradd -m -s /bin/bash -g HR hr_user1
useradd -m -s /bin/bash -g HR hr_user2

# Objective 5a: Owner = department admin, group = department group
chown eng_admin:Engineering /Engineering
chown sales_admin:Sales /Sales
chown hr_admin:HR /HR

# Objective 5b-5e: 1770
#   1   = sticky bit -> only a file's owner can delete it (5c)
#   7   = owner (admin) rwx (5b)
#   7   = group (department users) rwx (5d)
#   0   = others no access at all (5e)
chmod 1770 /Engineering /Sales /HR

# Objective 6: Create a document in each department directory
for dept in Engineering Sales HR; do
    echo "This file contains confidential information for the department." > /$dept/confidential.txt
done

# 6a: Same ownership as the directory it is in
chown eng_admin:Engineering /Engineering/confidential.txt
chown sales_admin:Sales /Sales/confidential.txt
chown hr_admin:HR /HR/confidential.txt

# 6c: 640 -> admin read/write, group read only, others nothing
chmod 640 /Engineering/confidential.txt /Sales/confidential.txt /HR/confidential.txt
