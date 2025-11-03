# 🐍 Venom Crypto Trading Bot

Your premium Telegram bot that aggregates crypto trading signals from multiple trusted sources and delivers them with professional formatting and live charts.

## 🎯 Features

- ✅ *Auto Signal Forwarding* - Monitors 5 premium signal channels
- ✅ *Smart Signal Parsing* - Detects buy/sell, coins, targets, stop-loss
- ✅ *Interactive Menu System* - Website-like navigation
- ✅ *Live Trading Charts* - TradingView integration for 10+ pairs
- ✅ *Trading Strategies* - Educational content
- ✅ *Crypto News & Analysis* - Curated resources
- ✅ *Professional Formatting* - Clean, emoji-rich messages
- ✅ *24/7 Operation* - Runs continuously on Replit

## 📊 Signal Sources

Your bot monitors these channels:
1. *Evening Trader Group* - Premium trading signals
2. *Evening Trader Official* - Official channel
3. *Learn 2 Trade* - Educational signals
4. *CryptoSignals.Org* - Free signals
5. *ALTSIGNALS* - Trading signals

## 🚀 Quick Setup (15 Minutes)

### Step 1: Get API Credentials

1. Visit https://my.telegram.org/auth
2. Login with your phone
3. Go to "API Development Tools"
4. Create application
5. Save API_ID and API_HASH

### Step 2: Upload to GitHub

1. Go to https://github.com/new
2. Name: venom-crypto-bot
3. Upload all 7 files from this project
4. Commit

### Step 3: Deploy to Replit

1. Go to https://replit.com
2. Click "Import from GitHub"
3. Paste your repo URL
4. Click Import

### Step 4: Add Secrets in Replit

Click "Tools" → "Secrets" and add:


Key: API_ID
Value: [your api_id number]

Key: API_HASH
Value: [your api_hash string]


*Optional* (only if you want phone authentication):

Key: PHONE_NUMBER
Value: +1234567890


### Step 5: Run!

1. Click "Run" button
2. Wait for installation
3. Bot will post menu to your channel
4. Done! 🎉

## 🔧 Configuration

### Pre-configured Settings

These are already set in main.py:
- ✅ Bot Token: 
- ✅ Your Channel ID: 
- ✅ Source Channels: All 5 signal channels configured

### What You Need to Add

Only 2 things in Replit Secrets:
1. API_ID - From my.telegram.org
2. API_HASH - From my.telegram.org

## 📱 Usage

### For Channel Members

Members can interact with buttons:
- *Live Charts* - View TradingView charts
- *Trading Signals* - Auto-posted
- *Crypto News* - Curated sources
- *Expert Predictions* - Top analysts
- *Data Analysis* - Market tools
- *Trading Strategies* - Learn strategies

### For You (Admin)

Signals are automatically:
1. Detected from source channels
2. Parsed for coin, entry, targets, SL
3. Formatted professionally
4. Posted with chart links
5. Attributed to source

## 🔄 Keep Bot Running 24/7

### Option 1: UptimeRobot (Free)

1. Copy your Replit URL from webview
2. Go to https://uptimerobot.com
3. Sign up free
4. Add new monitor (HTTP)
5. Paste Replit URL
6. Set interval: 5 minutes
7. Done! ✅

### Option 2: Replit Always On ($7/month)

1. Go to Replit settings
2. Enable "Always On"
3. Add payment method

## 🎨 Customization

### Add More Coins to Chart Menu

Edit main.py, find CHART_MENU:

python
CHART_MENU = [
    [Button.inline("BTC/USDT", b"chart_BTC")],
    # Add your coin:
    [Button.inline("SHIB/USDT", b"chart_SHIB")],
]


### Adjust Signal Detection

Edit SIGNAL_PATTERNS in main.py to match your sources' format.

### Change Menu Text

Edit the menu responses in callback_handler() function.

## 🆘 Troubleshooting

### Bot Not Starting

bash
# Check environment variables in Replit
# Make sure API_ID and API_HASH are set


### No Signals Forwarding

- ✅ Check bot is in source channels
- ✅ Verify channel IDs in main.py
- ✅ Check Replit logs for errors

### Bot Not Posting to Channel

- ✅ Verify bot is admin in your channel
- ✅ Check channel ID is correct
- ✅ Ensure posting permission enabled

## 📊 File Structure


venom-crypto-bot/
├── main.py              # Main bot (pre-configured)
├── utils.py             # Helper functions
├── keep_alive.py        # 24/7 server
├── requirements.txt     # Dependencies
├── .env.example         # Config template
├── .gitignore          # Security
└── README.md           # This file


## 🔐 Security

- ❌ Never share your bot token
- ❌ Don't commit .env file
- ✅ Use Replit Secrets
- ✅ Keep API credentials private

## ⚠ Disclaimer

*Important:* This bot is for educational purposes only.

- ❌ Not financial advice
- ❌ No profit guarantees
- ✅ Always DYOR (Do Your Own Research)
- ✅ Understand the risks
- ✅ Trade responsibly

## 📞 Support

*Common Issues:*

1. *Module not found*: Replit auto-installs, wait 2 minutes
2. *Bot silent*: Check logs, verify token
3. *No signals*: Check source channels accessible
4. *Rate limited*: Wait 60 seconds, reduce activity

## 🎉 Success Checklist

- [ ] All files uploaded to GitHub
- [ ] Imported to Replit
- [ ] API_ID and API_HASH added to Secrets
- [ ] Bot running (check console)
- [ ] Menu posted in channel
- [ ] Buttons working
- [ ] Charts opening
- [ ] UptimeRobot configured

## 📈 What's Next?

1. ✅ Monitor logs for signals
2. ✅ Test all menu features
3. ✅ Invite members to channel
4. ✅ Get feedback
5. ✅ Enjoy automated signals!

## 🙏 Credits

- Telethon (Telegram library)
- Flask (Web framework)
- Your 5 premium signal sources

---

*Version:* 1.0.0  
*Bot:* @VenomCryptoTradingBot  
*Channel:* -1003206076824  
*Status:* Production Ready


Made with 🐍 for crypto traders
