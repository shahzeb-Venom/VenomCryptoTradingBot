# 🐍 Venom Bot - Quick Reference Card

## 📝 Your Bot Details


Bot Name: @VenomCryptoTradingBot
Bot Token: YOUR BOT TOKEN
Channel ID: YOUR CHANNEL ID
Channel Link: https://t.me/VenomCryptoTradingBot


## 📡 Monitoring These Channels

| Channel ID | Name | Link |
|------------|------|------|
| -1002529586843 | Evening Trader Group | https://t.me/EveningTrader |
| -1002148968919 | Evening Trader Official | https://t.me/EveningTraders |
| -1001263225860 | Learn 2 Trade | https://t.me/learn2tradenews |
| -1002536577425 | CryptoSignals.Org | https://t.me/Cryptosignalsorg_real |
| -1002382045069 | ALTSIGNALS | https://t.me/altsignals_forexfactorynews |

## 🔑 Required Secrets (Replit)


API_ID = [get from my.telegram.org]
API_HASH = [get from my.telegram.org]


## 📦 Files Checklist

- [x] main.py (main bot code)
- [x] utils.py (helper functions)
- [x] keep_alive.py (24/7 server)
- [x] requirements.txt (dependencies)
- [x] .env.example (config template)
- [x] .gitignore (security)
- [x] README.md (documentation)
- [x] SETUP.md (setup guide)
- [x] QUICK_REFERENCE.md (this file)

## ⚡ 3-Minute Deploy

bash
1. Upload to GitHub
2. Import to Replit
3. Add 2 Secrets (API_ID, API_HASH)
4. Click Run
5. Done!


## 🆘 Emergency Fixes

| Problem | Quick Fix |
|---------|-----------|
| Bot offline | Restart Replit |
| No signals | Wait, check logs |
| Can't post | Check bot is admin |
| Module error | Wait 2 min for install |

## 📊 File Locations


GitHub: github.com/[YOU]/venom-crypto-bot
Replit: replit.com/@[YOU]/venom-crypto-bot
Channel: t.me/VenomCryptoTradingBot


## 🔗 Important Links

- *Telegram API:* https://my.telegram.org
- *GitHub:* https://github.com
- *Replit:* https://replit.com
- *UptimeRobot:* https://uptimerobot.com

## 💻 Commands

| Command | Action |
|---------|--------|
| /start | Start bot |
| /menu | Show menu |

## 🎯 Expected Console Output


✅ Keep-alive server started
✅ Posted menu to Venom channel
🚀 Venom Bot is running...
📡 Monitoring 5 signal channels
📢 Posting to channel: -1003206076824


## 🔧 Common Commands (Replit Shell)

bash
# Install dependencies
pip install -r requirements.txt

# Check Python version
python --version

# Run bot manually
python main.py


## 📈 Success Indicators

- ✅ Menu appears in channel
- ✅ Buttons clickable
- ✅ Charts open
- ✅ No errors in console
- ✅ UptimeRobot shows "Up"

## 🎨 Customization Spots

*Add coins (main.py line ~60):*
python
[Button.inline("SHIB/USDT", b"chart_SHIB")]


*Adjust patterns (main.py line ~70):*
python
SIGNAL_PATTERNS = {...}


*Change text (main.py line ~200+):*
python
"🐍 **Welcome to...**"


## 🔐 Security Rules

- ❌ Never share API_HASH
- ❌ Never share bot token publicly
- ✅ Use Replit Secrets
- ✅ Keep .gitignore active

## 📞 Support Steps

1. Check Replit console logs
2. Read error message
3. Check this reference
4. Check SETUP.md
5. Restart and retry

## ⚙ Configuration Summary

*Pre-configured in code:*
- Bot token ✅
- Channel ID ✅
- Source channels ✅
- Menu structure ✅

*You need to add:*
- API_ID (from my.telegram.org)
- API_HASH (from my.telegram.org)

*That's it!* Just 2 values.

## 🎯 Post-Deploy Checklist

- [ ] Bot running in Replit
- [ ] Menu posted in channel
- [ ] All buttons work
- [ ] Charts open correctly
- [ ] UptimeRobot pinging
- [ ] No errors in logs

## 💡 Pro Tips

1. *Monitor logs* first 24 hours
2. *Test all buttons* before sharing
3. *Pin menu message* in channel
4. *Add channel rules* as first message
5. *Invite gradually* to test stability

---

*Everything at a glance!* 📋


Keep this for quick reference.
