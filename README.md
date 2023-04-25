<div align="center"><img src="./media/discord-bot.png"></div>

---
## **Basic discord bot made in python using discord.py(2.2.2) module.**
**Categories:-**
- **Admin - `[Admin only commands]`**
- **Moderator - `[Moderator only commands]`**
- **Information - `[Information fetching commands]`**
- **Math - `[Mathematical operations]`**
- **Fun - `[Entertainment commands]`**
---
- **To create you own bot from [Discord's Developer Portal](https://discord.com/developers/applications), follow the following steps:-**
1. Create an application at [Discord's Developer Portal](https://discord.com/developers/applications)
2. Goto **OAuth2** > URL **Generator**
3. Select **bot** from **SCOPES** and  **Administrator** from **BOT PERMISSIONS**
4. Copy the url generated below > open on new tab > invite bot to your server
---
- **To clone the files run the bot, follow the following steps:-**
1. Download python from [python.org/downloads](https://www.python.org/downloads/)
2. Install python into your machine
3. Clone repository into your machine
4. Run the following command into your console:-
```bash
-r requirements.txt
```
5. Goto [**config.py**](./config.py) and add details as per your requirements
6. Run the bot using the following command:-
```bash
python main.py
```
7. You can customize the bot's activity by changing the `name="..."` value from the code below in [**main.py**](./main.py)
```py
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Discord.py"))
```