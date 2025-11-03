# 🐍 Venom Bot - Complete Setup Guide

## ⚡ Quick Setup (15 Minutes)

Follow these exact steps to get your bot running.

---

## 📋 What You Need

- [ ] Telegram account
- [ ] GitHub account (free)
- [ ] Replit account (free)
- [ ] 15 minutes

---

## 🎯 Step 1: Get API Credentials (5 min)

### 1.1 Get Telegram API ID and Hash

1. Open browser, go to: **https://my.telegram.org/auth**
2. Enter your phone number (with country code): +1234567890
3. Click "Next"
4. Enter code from Telegram app
5. Click "API Development Tools"
6. Fill form:
   - App title: Venom Bot
   - Short name: venombot
   - Platform: Other
7. Click "Create application"

*📝 SAVE THESE:*

API_ID: _____________ (number like 12345678)
API_HASH: _____________ (string like 1a2b3c4d5e6f...)


---

## 📦 Step 2: Upload to GitHub (3 min)

### 2.1 Create Repository

1. Go to: **https://github.com/new**
2. Repository name: venom-crypto-bot
3. Description: Crypto trading signals bot
4. Choose: *Public*
5. ✅ Check "Add README file"
6. Click "Create repository"

### 2.2 Upload Files

1. Click "Add file" → "Upload files"
2. Drag these 7 files:
   - main.py
   - utils.py
   - keep_alive.py
   - requirements.txt
   - .env.example
   - .gitignore
   - README.md
3. Commit message: Initial Venom Bot setup
4. Click "Commit changes"

✅ *Done!* Your code is on GitHub.

---

## 🖥 Step 3: Deploy to Replit (5 min)

### 3.1 Import from GitHub

1. Go to: *https://replit.com*
2. Sign in (can use GitHub account)
3. Click "Create Repl" (big blue button)
4. Select "Import from GitHub" tab
5. Paste: https://github.com/YOUR_USERNAME/venom-crypto-bot
   - Replace YOUR_USERNAME with your GitHub username
6. Click "Import from GitHub"
7. Wait 30 seconds for import

### 3.2 Add Secrets (CRITICAL)

1. In Replit, click *"Tools"* on left sidebar
2. Click *"Secrets"* (lock icon)
3. Add Secret #1:
   - Key: API_ID
   - Value: [your api_id number from step 1]
   - Click "Add new secret"

4. Add Secret #2:
   - Key: API_HASH
   - Value: [your api_hash string from step 1]
   - Click "Add new secret"

*That's it!* Only 2 secrets needed. Bot token and channel IDs are already in code.

### 3.3 Run Bot

1. Click *"Run"* button (big green play button at top)
2. Wait for installation (1-2 minutes)
3. Watch console for messages

*Expected Output:*

INFO - 🐍 Starting Venom Crypto Trading Bot...
INFO - ✅ Keep-alive server started
INFO - ✅ Posted menu to Venom channel
INFO - 🚀 Venom Bot is running and monitoring channels...
INFO - 📡 Monitoring 5 signal channels
INFO - 📢 Posting to channel: -1003206076824


✅ *Success!* Bot is running.

---

## ✅ Step 4: Verify (2 min)

### 4.1 Check Your Channel

1. Open Telegram
2. Go to your channel: *@VenomCryptoTradingBot*
3. You should see a message from bot with buttons
4. Click buttons to test

### 4.2 Test Features

Try clicking:
- [ ] "Live Trading Charts" - Opens chart menu
- [ ] "BTC/USDT" - Opens TradingView
- [ ] "Trading Strategies" - Shows strategies
- [ ] "Help" - Shows info

All working? *Perfect!* ✅

---

## 🔄 Step 5: Keep Running 24/7 (5 min)

Replit free tier sleeps after inactivity. Use UptimeRobot to keep it alive.

### 5.1 Get Your Replit URL

1. In Replit, click *"Webview"* tab (next to Console)
2. Copy URL from address bar
   - Looks like: https://venom-crypto-bot.yourusername.repl.co

### 5.2 Setup UptimeRobot

1. Go to: *https://uptimerobot.com*
2. Click "Sign Up Free"
3. Verify email
4. Click "Add New Monitor"
5. Settings:
   - *Monitor Type:* HTTP(s)
   - *Friendly Name:* Venom Bot
   - *URL:* [paste your Replit URL]
   - *Monitoring Interval:* 5 minutes
6. Click "Create Monitor"

✅ *Done!* Bot will run 24/7 for free.

---

## 🎉 You're Live!

Your Venom Bot is now:
- ✅ Running 24/7
- ✅ Monitoring 5 signal channels
- ✅ Auto-posting signals
- ✅ Serving your community

---

## 🔍 What to Expect

### Signals Will Appear Like This:


🟢 LONG SIGNAL 🟢
━━━━━━━━━━━━━━━━━━

💎 Pair: BTCUSDT
⚡ Leverage: 10x
📍 Entry: $45000

🎯 Targets:
  • T1: $45500
  • T2: $46000
  • T3: $46500

🛑 Stop Loss: $44500

━━━━━━━━━━━━━━━━━━
📡 Source: Learn 2 Trade
⏰ Time: 2024-11-03 10:30:00 UTC

⚠ DYOR - Not Financial Advice

📊 [View Live Chart] (button)


---

## 🆘 Troubleshooting

### Problem: "Module not found"

*Solution:*
- Wait 2 minutes, Replit is installing
- Or run in Shell: pip install -r requirements.txt

### Problem: Bot not responding

*Solution:*
- Check Secrets are added (API_ID, API_HASH)
- Restart bot (Stop → Run)
- Check console for errors

### Problem: No signals appearing

*Solution:*
- Wait - signals come when sources post
- Check your bot is in source channels
- Check Replit logs

### Problem: "Permission denied" posting to channel

*Solution:*
- Verify bot is admin in channel
- Check "Post Messages" permission enabled
- Verify channel ID is correct in main.py

---

## 📊 Monitor Your Bot

### View Logs in Replit

1. Click "Console" tab
2. Watch for:
   - ✅ Green checkmarks = success
   - ❌ Red errors = problems
   - ℹ Info messages = activity

### Check UptimeRobot

1. Log in to UptimeRobot
2. See uptime percentage
3. Get alerts if bot goes down

---

## 🎨 Customize Later

Once running, you can:

1. *Add more coins* to chart menu
2. *Adjust signal patterns* for your sources
3. *Customize menu text*
4. *Add new features*

See README.md for customization guide.

---

## 🔐 Security Reminders

*Keep Safe:*
- ✅ API credentials in Replit Secrets only
- ✅ Never share bot token
- ✅ Don't commit .env file
- ✅ Keep GitHub repo public or use .gitignore

*Already Secured:*
- ✅ Bot token in main.py (not in Secrets, that's OK for your bot)
- ✅ Channel IDs in main.py
- ✅ .gitignore prevents leaking sessions

---

## 📱 Share Your Channel

Now that bot is running:

1. *Invite members* to @VenomCryptoTradingBot
2. *Pin welcome message* with menu
3. *Add channel description*
4. *Share link* with traders

---

## ✨ Success Checklist

- [x] Got API credentials
- [x] Uploaded to GitHub
- [x] Imported to Replit
- [x] Added Secrets
- [x] Bot running
- [x] Menu in channel
- [x] Buttons working
- [x] UptimeRobot setup
- [x] 24/7 operation

*You did it!* 🎉

---

## 💡 Tips for Success

1. *Let it run* - Signals come when sources post
2. *Check logs daily* - Monitor for errors
3. *Test features* - Make sure everything works
4. *Engage members* - Build community
5. *Stay updated* - Check for issues

---

## 📞 Need Help?

*Check:*
1. Replit console logs (shows errors)
2. README.md (detailed info)
3. This guide (step-by-step)

*Common fixes:*
- Restart bot (Stop → Run)
- Check Secrets are correct
- Verify bot is channel admin
- Wait for dependencies to install

---

## 🚀 You're All Set!

Your Venom Crypto Trading Bot is live!

*What happens now:*
- Bot monitors 5 channels
- Detects trading signals
- Formats them professionally
- Posts to your channel with charts
- Members interact with menu
- Runs 24/7 automatically

*Enjoy!* 🐍

---

*Quick Links:*
- Your Bot: @VenomCryptoTradingBot
- Your Channel: https://t.me/VenomCryptoTradingBot
- Replit: https://replit.com/@yourusername/venom-crypto-bot
- GitHub: https://github.com/yourusername/venom-crypto-bot
- UptimeRobot: https://uptimerobot.com/dashboard

*Total Time:* ~15 minutes  
*Total Cost:* $0 (Free!)  
*Total Value:* Priceless! 