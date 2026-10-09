#!/bin/bash
# GIK2NV Linux Lab - Part 2
# Interactive user management script.
# Run as root: sudo ./usermgmt.sh

# The script must be run as root since it creates groups, users and directories
if [ "$(id -u)" -ne 0 ]; then
    echo "Error: this script must be run as root (use sudo)."
    exit 1
fi

# a. Create a new group - keep asking until a unique name is given
while true; do
    read -p "Enter a new group name: " groupname
    if [ -z "$groupname" ]; then
        echo "Error: group name cannot be empty. Try again."
        continue
    fi
    getent group "$groupname" > /dev/null
    if [ $? -eq 0 ]; then
        echo "Error: group '$groupname' already exists. Try another group name."
    else
        groupadd "$groupname"
        if [ $? -eq 0 ]; then
            echo "Group '$groupname' created."
            break
        else
            echo "Error: could not create group '$groupname'. Try another group name."
        fi
    fi
done

# b. Create a new user - keep asking until a unique name is given.
#    Bash login shell and the new group as primary group.
while true; do
    read -p "Enter a new username: " username
    if [ -z "$username" ]; then
        echo "Error: username cannot be empty. Try again."
        continue
    fi
    getent passwd "$username" > /dev/null
    if [ $? -eq 0 ]; then
        echo "Error: user '$username' already exists. Try another username."
    else
        useradd -m -s /bin/bash -g "$groupname" "$username"
        if [ $? -eq 0 ]; then
            echo "User '$username' created."
            break
        else
            echo "Error: could not create user '$username'. Try another username."
        fi
    fi
done

# c. Create a password for the user
while true; do
    read -s -p "Enter a password for $username: " password
    echo
    read -s -p "Confirm password: " password2
    echo
    if [ -z "$password" ]; then
        echo "Error: password cannot be empty. Try again."
    elif [ "$password" != "$password2" ]; then
        echo "Error: passwords do not match. Try again."
    else
        echo "$username:$password" | chpasswd
        if [ $? -eq 0 ]; then
            echo "Password set for '$username'."
            break
        else
            echo "Error: could not set password. Try again."
        fi
    fi
done

# d. Ensure the new user is a member of the new group
usermod -aG "$groupname" "$username"
if [ $? -eq 0 ]; then
    echo "User '$username' is a member of group '$groupname'."
fi

# e. Create a directory at the root (/) with the same name as the user
mkdir "/$username"
if [ $? -ne 0 ]; then
    echo "Error: could not create directory /$username."
    exit 1
fi
echo "Directory /$username created."

# f. Set ownership of the directory to the new user and group
chown "$username:$groupname" "/$username"

# g + h. 1770: owner rwx, group rwx, others none, sticky bit set so that
#        only the owner of a file can delete it from the directory
chmod 1770 "/$username"
echo "Ownership and permissions set on /$username."

echo
echo "===== Summary ====="
id "$username"
getent passwd "$username"
ls -ld "/$username"
