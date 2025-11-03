# 🔧 Venom Bot - Troubleshooting Guide

## 🆘 Common Issues & Solutions

---

## 1. Bot Won't Start

### Symptoms
- Replit shows errors immediately
- Console says "Module not found"
- Bot crashes on startup

### Solutions

*A. Missing Dependencies*
bash
# In Replit Shell, run:
pip install -r requirements.txt


*B. Missing Secrets*
1. Check Tools → Secrets
2. Verify API_ID exists
3. Verify API_HASH exists
4. Values should have no quotes

*C. Wrong Secret Format*

✅ Correct:
API_ID = 12345678
API_HASH = 1a2b3c4d5e6f789...

❌ Wrong:
API_ID = "12345678"
API_HASH = '1a2b3c4d...'


*D. Syntax Errors*
- Check main.py for typos
- Ensure all quotes match
- Check indentation

---

## 2. Bot Starts But No Menu in Channel

### Symptoms
- Bot runs without errors
- Nothing appears in channel
- Console shows "running"

### Solutions

*A. Bot Not Admin*
1. Open your Telegram channel
2. Go to Channel Info → Administrators
3. Click "Add Administrator"
4. Search: @VenomCryptoTradingBot
5. Grant "Post Messages" permission

*B. Wrong Channel ID*
Verify in main.py line ~20:
python
YOUR_CHANNEL_ID = -1003206076824

Must have minus sign!

*C. Permission Issue*
1. Remove bot from channel
2. Re-add as admin
3. Restart Replit bot

---

## 3. No Signals Being Forwarded

### Symptoms
- Bot running fine
- Menu works
- But no signals appear

### Solutions

*A. Wait for Signals*
- Source channels don't post 24/7
- May take hours for first signal
- Check source channels manually

*B. Bot Not in Source Channels*
Your bot is already joined! But verify:
1. Go to each source channel
2. Check if bot is member
3. Bot should see all messages

*C. Signal Pattern Mismatch*
Source channels may use different format.

Edit main.py SIGNAL_PATTERNS:
python
'buy': r'\b(buy|long|entry|CUSTOM_WORD)\b',


*D. Test Manually*
Send test message to one of YOUR channels:

BUY Signal
BTCUSDT
Entry: 45000
Target 1: 46000
Stop Loss: 44000


---

## 4. Buttons Not Working

### Symptoms
- Menu appears
- Clicking buttons does nothing
- Or gives error

### Solutions

*A. Old Message*
- Delete old menu messages
- Restart bot to post fresh menu
- Try with new message

*B. Callback Error*
Check console for errors like:

ERROR - Error in callback_handler


*C. Button Data Too Long*
If you edited buttons, keep data short:
python
✅ Good: b"chart_BTC"
❌ Bad: b"very_long_button_data_string"


---

## 5. Charts Not Opening

### Symptoms
- Click chart button
- Nothing happens
- Or link broken

### Solutions

*A. Check URL Format*
In main.py, verify:
python
def get_tradingview_chart(coin):
    base_coin = coin.replace('USDT', '')...
    return f"https://www.tradingview.com/chart/..."


*B. Coin Name Issue*
Some coins need different URL format.
Test manually: https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT

*C. Button Type*
Ensure using Button.url() for external links:
python
Button.url("📈 Open Chart", chart_url)


---

## 6. Bot Stops After Some Time

### Symptoms
- Bot runs fine initially
- Stops after 30-60 minutes
- Replit shows "inactive"

### Solutions

*A. Setup UptimeRobot*
1. Go to uptimerobot.com
2. Add monitor with Replit URL
3. Set interval: 5 minutes
4. This keeps bot alive 24/7

*B. Replit Always On*
Pay $7/month for Replit Always On (optional)

*C. Check Keep-Alive Server*
In console, should see:

✅ Keep-alive server started on port 8080


If missing, check keep_alive.py exists.

---

## 7. Rate Limit Errors

### Symptoms

ERROR - FloodWaitError: Must wait X seconds


### Solutions

*A. Wait*
Telegram limits requests. Bot will auto-wait.

*B. Reduce Activity*
Don't spam buttons. Normal use is fine.

*C. Add Delays*
In main.py, add between actions:
python
await asyncio.sleep(2)


---

## 8. Module Import Errors

### Symptoms

ModuleNotFoundError: No module named 'telethon'


### Solutions

*A. Install Requirements*
bash
pip install -r requirements.txt


*B. Check requirements.txt*
Should contain:

telethon==1.35.0
cryptg==0.4.0
python-dotenv==1.0.0
flask==3.0.0


*C. Replit Auto-Install*
Wait 2 minutes after clicking Run. Replit auto-installs.

---

## 9. Authentication Errors

### Symptoms

ERROR - Invalid API_ID or API_HASH


### Solutions

*A. Double-Check Credentials*
1. Go to my.telegram.org
2. Click "API Development Tools"
3. Copy exact values
4. Paste in Replit Secrets

*B. No Spaces*

✅ Correct: 12345678
❌ Wrong: 12345678 (with space)


*C. Correct Type*

API_ID should be NUMBER: 12345678
API_HASH should be STRING: 1a2b3c4d...


---

## 10. Signals Format Wrong

### Symptoms
- Signals post but look bad
- Missing info
- Wrong formatting

### Solutions

*A. Adjust Parser*
Edit parse_signal() in main.py:
python
def parse_signal(text):
    # Customize patterns here


*B. Check Source Format*
Look at original signal format in source channel.
Adjust regex patterns to match.

*C. Use utils.py*
For advanced parsing, use SignalParser class in utils.py

---

## 🔍 Debugging Steps

### When Something Goes Wrong:

1. *Read Error Message*
   - Console shows exact error
   - Line number tells where issue is

2. *Check Logs*
   
   Look for:
   ✅ = Success
   ❌ = Error
   ⏳ = Waiting
   

3. *Restart Bot*
   - Stop button in Replit
   - Run button to restart
   - Watch console output

4. *Verify Config*
   - Secrets set correctly
   - Bot is admin in channel
   - All files uploaded

5. *Test Incrementally*
   - Start bot
   - Check menu posts
   - Test one button
   - Check one signal
   - Then test all

---

## 📊 Reading Console Logs

### Good Logs (All Working)

INFO - 🐍 Starting Venom Crypto Trading Bot...
INFO - ✅ Keep-alive server started
INFO - ✅ Posted menu to Venom channel
INFO - 🚀 Venom Bot is running...
INFO - 📡 Monitoring 5 signal channels
INFO - ✅ Posted signal: BTCUSDT - LONG 🟢


### Bad Logs (Problems)

ERROR - Missing environment variable: API_ID
ERROR - Cannot post to channel: Permission denied
ERROR - FloodWaitError: Must wait 60 seconds
ERROR - Module not found: telethon


---

## 🆘 Emergency Reset

If nothing works:

### Full Reset Process

1. *Stop Bot*
   - Click Stop in Replit

2. *Delete Session Files*
   - In Replit Files, delete:
     - venom_bot_session.session
     - user_session.session

3. *Verify Secrets*
   - Tools → Secrets
   - Check API_ID
   - Check API_HASH

4. *Restart Fresh*
   - Click Run
   - Watch console
   - Should start clean

---

## 💻 Useful Shell Commands

bash
# Check if file exists
ls -la

# View file contents
cat main.py

# Check Python version
python --version

# Install package
pip install telethon

# Check installed packages
pip list

# Run bot manually
python main.py


---

## 🔐 Security Issues

### Bot Token Leaked?

1. *Revoke Token*
   - Go to @BotFather
   - Send: /mybots
   - Select bot
   - Choose "API Token"
   - Click "Revoke current token"
   - Get new token

2. *Update Code*
   - Edit main.py
   - Replace BOT_TOKEN with new one
   - Restart bot

### API Credentials Compromised?

1. *Revoke at my.telegram.org*
2. Create new application
3. Update Replit Secrets
4. Restart bot

---

## 📞 Still Stuck?

### Checklist Before Asking for Help

- [ ] Read this entire guide
- [ ] Checked Replit console logs
- [ ] Verified all secrets set
- [ ] Bot is admin in channel
- [ ] Tried restarting bot
- [ ] Waited 2+ minutes for install
- [ ] Tested basic features

### Provide This Info

When seeking help:
1. Exact error message from console
2. Which step failed
3. Screenshots if possible
4. What you already tried

---

## 🎯 Prevention Tips

### Avoid Future Issues

1. *Always Check Logs*
   - Monitor console daily
   - Catch issues early

2. *Test After Changes*
   - Edit code
   - Test immediately
   - Don't make multiple changes at once

3. *Keep Backup*
   - Download files from GitHub
   - Save working version

4. *Update Carefully*
   - Don't update dependencies randomly
   - Test in separate Repl first

5. *Monitor Uptime*
   - Check UptimeRobot dashboard
   - Set up alerts

---

## ✅ Issue Resolution Checklist

- [ ] Identified exact problem
- [ ] Read relevant solution above
- [ ] Applied fix
- [ ] Restarted bot
- [ ] Tested functionality
- [ ] Verified in console logs
- [ ] Issue resolved!

---

*Most issues are solved by:*
1. ✅ Restart bot
2. ✅ Check Secrets
3. ✅ Verify bot is admin
4. ✅ Wait for install
5. ✅ Read error message

*You got this!* 