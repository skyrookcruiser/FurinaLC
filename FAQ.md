# Frequently Asked Question
### 1. Is this safe to use?
No. Don't expect me to try convincing you or something. Use it, or don't. I don't care.

### 2. How do I mod/customize identity skills, play as ricardo etc.?
This is just a private server, not a modding tool. 

### 3. I get a server error when I do X ingame!
X is probably not implemented. Feel free to implement it and make a pull request.

### 4. Are there commands?
Yes. You can use them through the coupon menu. Current commands are such:

(Note: they aren't case sensitive, as limbus client automatically uppercases the input when sending to the server)

- SYNC

    This command will update your owned stuff, making sure it's up to date with the latest limbus stuff. Of course, you'll have to update the submodule (LimbusStaticData) first. How? Just go ask ChatGPT "How do I sync a git submodule"

- P

    Usage example is like this "P10101L50G4". This will set a personality (identity) with an id of 10101 to level 50 and gacksung (uptie) 4.

- E

    Does the same like P, except it's for egos, and you can only change gacksung. Example: "E20101G4".

- I

    This command is used to update an item count. For example, "I11C100", will make you have 100 of item with the id 11.

- U

    This command is used to update user info. Example: "U1L100S100" will make a user with uid 1 be level 100 and have 100 stamina. (The uid doesn't actually matter btw)
