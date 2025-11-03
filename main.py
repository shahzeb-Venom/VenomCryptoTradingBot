import os
import asyncio
from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
import re
from datetime import datetime
import logging
from keep_alive import keep_alive

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(_name_)

# Bot Configuration - Your Venom Bot Details
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = '8276232278:AAFaMBBk-8b7RSsVBSN8ymc19cd-EhxmiKM'
YOUR_CHANNEL_ID = -1003206076824  # Venom Crypto Trading Bot channel
SESSION_NAME = 'venom_bot_session'

# Source channels to monitor - All your signal sources
SOURCE_CHANNELS = [
    -1002529586843,  # Evening Trader Group
    -1002148968919,  # Evening Trader Official
    -1001263225860,  # Learn 2 Trade
    -1002536577425,  # CryptoSignals.Org (free)
    -1002382045069   # ALTSIGNALS TRADING SIGNALS
]

# Channel names for display
CHANNEL_NAMES = {
    -1002529586843: "Evening Trader Group",
    -1002148968919: "Evening Trader Official",
    -1001263225860: "Learn 2 Trade",
    -1002536577425: "CryptoSignals.Org",
    -1002382045069: "ALTSIGNALS"
}

# Initialize bot
bot = TelegramClient(SESSION_NAME, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# User client for joining channels (optional - only if you want to use phone auth)
user_client = None

# Menu keyboards
MAIN_MENU = [
    [Button.inline("📊 Live Trading Charts", b"live_charts")],
    [Button.inline("📈 Trading Signals", b"signals"), Button.inline("📰 Crypto News", b"news")],
    [Button.inline("🧠 Expert Predictions", b"predictions"), Button.inline("📊 Data Analysis", b"analysis")],
    [Button.inline("🎯 Trading Strategies", b"strategies")],
    [Button.inline("ℹ Help", b"help")]
]

CHART_MENU = [
    [Button.inline("BTC/USDT", b"chart_BTC"), Button.inline("ETH/USDT", b"chart_ETH")],
    [Button.inline("BNB/USDT", b"chart_BNB"), Button.inline("SOL/USDT", b"chart_SOL")],
    [Button.inline("XRP/USDT", b"chart_XRP"), Button.inline("ADA/USDT", b"chart_ADA")],
    [Button.inline("DOGE/USDT", b"chart_DOGE"), Button.inline("AVAX/USDT", b"chart_AVAX")],
    [Button.inline("DOT/USDT", b"chart_DOT"), Button.inline("MATIC/USDT", b"chart_MATIC")],
    [Button.inline("🔙 Back to Menu", b"main_menu")]
]

STRATEGY_MENU = [
    [Button.inline("📈 Scalping Strategy", b"strat_scalping")],
    [Button.inline("📊 Day Trading", b"strat_day")],
    [Button.inline("🎯 Swing Trading", b"strat_swing")],
    [Button.inline("💎 HODLing Strategy", b"strat_hodl")],
    [Button.inline("🔙 Back to Menu", b"main_menu")]
]

# Signal pattern detection - Updated for your channels
SIGNAL_PATTERNS = {
    'buy': r'\b(buy|long|entry|open\s*long|🟢)\b',
    'sell': r'\b(sell|short|exit|open\s*short|🔴)\b',
    'coin': r'\b([A-Z]{2,10})(USDT|USD|BTC|ETH|PERP|/USDT|/USD)\b',
    'price': r'\$?\d+\.?\d*',
    'target': r'\b(target|tp|take\s*profit|t[0-9])\b',
    'stoploss': r'\b(sl|stop\s*loss|stoploss|stop)\b',
    'leverage': r'\b(leverage|x)\s*:?\s*(\d+)x?\b'
}

async def initialize_user_client():
    """Initialize user client for joining channels (optional)"""
    global user_client
    phone = os.environ.get('PHONE_NUMBER')
    if not phone:
        logger.warning("PHONE_NUMBER not set. Bot will use existing channel memberships.")
        return None
    
    user_client = TelegramClient('user_session', API_ID, API_HASH)
    await user_client.start(phone=phone)
    logger.info("User client initialized")
    return user_client

def parse_signal(text):
    """Parse trading signal from message"""
    text_lower = text.lower()
    signal = {
        'type': None,
        'coin': None,
        'entry': None,
        'targets': [],
        'stoploss': None,
        'leverage': None,
        'original': text
    }
    
    # Detect signal type
    if re.search(SIGNAL_PATTERNS['buy'], text_lower):
        signal['type'] = 'LONG 🟢'
    elif re.search(SIGNAL_PATTERNS['sell'], text_lower):
        signal['type'] = 'SHORT 🔴'
    
    # Extract coin pair
    coin_match = re.search(SIGNAL_PATTERNS['coin'], text.upper())
    if coin_match:
        signal['coin'] = coin_match.group(0).replace('/', '')
    
    # Extract leverage
    lev_match = re.search(SIGNAL_PATTERNS['leverage'], text_lower)
    if lev_match:
        signal['leverage'] = lev_match.group(2)
    
    # Extract prices
    prices = re.findall(r'\$?(\d+\.?\d*)', text)
    if prices:
        signal['entry'] = prices[0]
        if len(prices) > 1:
            signal['targets'] = prices[1:min(6, len(prices))]  # Max 5 targets
        if len(prices) > 6:
            signal['stoploss'] = prices[-1]
    
    return signal

def format_signal_message(signal, source_channel_id):
    """Format signal for posting"""
    source_name = CHANNEL_NAMES.get(source_channel_id, "Unknown Source")
    
    # Header
    if 'LONG' in str(signal['type']):
        emoji = "🟢"
        signal_type = "LONG"
    else:
        emoji = "🔴"
        signal_type = "SHORT"
    
    message = f"{emoji} *{signal_type} SIGNAL* {emoji}\n"
    message += "━━━━━━━━━━━━━━━━━━\n\n"
    
    # Coin
    if signal['coin']:
        message += f"💎 *Pair:* {signal['coin']}\n"
    
    # Leverage
    if signal['leverage']:
        message += f"⚡ *Leverage:* {signal['leverage']}x\n"
    
    # Entry
    if signal['entry']:
        message += f"📍 *Entry:* ${signal['entry']}\n"
    
    # Targets
    if signal['targets']:
        message += f"\n🎯 *Targets:*\n"
        for i, target in enumerate(signal['targets'], 1):
            message += f"  • T{i}: ${target}\n"
    
    # Stop Loss
    if signal['stoploss']:
        message += f"\n🛑 *Stop Loss:* ${signal['stoploss']}\n"
    
    # Footer
    message += f"\n━━━━━━━━━━━━━━━━━━\n"
    message += f"📡 *Source:* {source_name}\n"
    message += f"⏰ *Time:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
    message += f"\n⚠ *DYOR - Not Financial Advice*"
    
    return message

def get_tradingview_chart(coin):
    """Generate TradingView chart URL"""
    # Clean coin name
    base_coin = coin.replace('USDT', '').replace('USD', '').replace('BTC', '').replace('ETH', '').replace('PERP', '')
    return f"https://www.tradingview.com/chart/?symbol=BINANCE:{base_coin}USDT"

# Bot Event Handlers

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    """Handle /start command"""
    await event.respond(
        "🐍 *Welcome to Venom Crypto Trading Bot!*\n\n"
        "Your premium crypto signals aggregator!\n\n"
        "📊 *Features:*\n"
        "• Live trading charts\n"
        "• Real-time signals from 5+ sources\n"
        "• Expert predictions\n"
        "• Trading strategies\n"
        "• Market analysis\n\n"
        "🔥 All signals automatically forwarded with charts!\n\n"
        "Choose an option below:",
        buttons=MAIN_MENU
    )

@bot.on(events.NewMessage(pattern='/menu'))
async def menu_handler(event):
    """Show main menu"""
    await event.respond("📱 *Venom Bot Menu*", buttons=MAIN_MENU)

@bot.on(events.CallbackQuery)
async def callback_handler(event):
    """Handle button callbacks"""
    data = event.data.decode('utf-8')
    
    if data == "main_menu":
        await event.edit("📱 *Venom Bot Menu*", buttons=MAIN_MENU)
    
    elif data == "live_charts":
        await event.edit("📊 *Select a coin to view live chart:*", buttons=CHART_MENU)
    
    elif data.startswith("chart_"):
        coin = data.replace("chart_", "")
        chart_url = get_tradingview_chart(f"{coin}USDT")
        await event.answer(f"Opening {coin}/USDT chart...", alert=False)
        await event.respond(
            f"📈 *{coin}/USDT Live Chart*\n\n"
            f"🔗 [Click here to view interactive chart]({chart_url})\n\n"
            f"📊 Professional TradingView analysis",
            buttons=CHART_MENU
        )
    
    elif data == "signals":
        await event.answer("📈 Latest signals are posted automatically in the channel!", alert=True)
    
    elif data == "news":
        await event.edit(
            "📰 *Top Crypto News Sources:*\n\n"
            "• [CoinDesk](https://coindesk.com) - Latest crypto news\n"
            "• [CoinTelegraph](https://cointelegraph.com) - Market updates\n"
            "• [Decrypt](https://decrypt.co) - Web3 news\n"
            "• [The Block](https://theblock.co) - Industry analysis\n"
            "• [CryptoSlate](https://cryptoslate.com) - Data & news\n\n"
            "Stay informed with real-time updates!",
            buttons=[[Button.inline("🔙 Back", b"main_menu")]]
        )
    
    elif data == "predictions":
        await event.edit(
            "🧠 *Top Crypto Analysts to Follow:*\n\n"
            "• @CryptoCapo - Technical analysis\n"
            "• @crypto_birb - Market insights\n"
            "• @Pentosh1 - Trading strategies\n"
            "• @RookieXBT - On-chain analysis\n"
            "• @CryptoCred - Risk management\n\n"
            "⚠ Always do your own research!",
            buttons=[[Button.inline("🔙 Back", b"main_menu")]]
        )
    
    elif data == "analysis":
        await event.edit(
            "📊 *Best Market Analysis Tools:*\n\n"
            "• [CoinMarketCap](https://coinmarketcap.com) - Price tracking\n"
            "• [CoinGecko](https://coingecko.com) - Market data\n"
            "• [Glassnode](https://glassnode.com) - On-chain metrics\n"
            "• [TradingView](https://tradingview.com) - Charts & TA\n"
            "• [DeFi Llama](https://defillama.com) - DeFi analytics\n\n"
            "Make informed trading decisions!",
            buttons=[[Button.inline("🔙 Back", b"main_menu")]]
        )
    
    elif data == "strategies":
        await event.edit("🎯 *Trading Strategies:*", buttons=STRATEGY_MENU)
    
    elif data.startswith("strat_"):
        strategy = data.replace("strat_", "")
        strategies_info = {
            "scalping": "📈 Scalping Strategy**\n\n"
                       "⏱ *Timeframe:* Seconds to minutes\n"
                       "💰 *Targets:* 0.5-2% profit\n"
                       "📊 *Charts:* 1m-5m\n"
                       "⚡ *Style:* High-frequency\n"
                       "🎯 *Best for:* Active traders\n\n"
                       "Quick in, quick out. Requires constant monitoring.",
            "day": "📊 Day Trading Strategy**\n\n"
                  "⏱ *Timeframe:* Hours (same day)\n"
                  "💰 *Targets:* 2-5% profit\n"
                  "📊 *Charts:* 15m-1h\n"
                  "⚡ *Style:* Multiple daily trades\n"
                  "🎯 *Best for:* Part-time traders\n\n"
                  "Close all positions before market close.",
            "swing": "🎯 Swing Trading Strategy**\n\n"
                    "⏱ *Timeframe:* Days to weeks\n"
                    "💰 *Targets:* 5-20% profit\n"
                    "📊 *Charts:* 4h-1D\n"
                    "⚡ *Style:* Trend following\n"
                    "🎯 *Best for:* Patient traders\n\n"
                    "Catch major market swings and trends.",
            "hodl": "💎 HODL Strategy**\n\n"
                   "⏱ *Timeframe:* Months to years\n"
                   "💰 *Targets:* 50-500%+ profit\n"
                   "📊 *Charts:* Weekly/Monthly\n"
                   "⚡ *Style:* Buy & hold\n"
                   "🎯 *Best for:* Long-term believers\n\n"
                   "Diamond hands! Ignore short-term noise."
        }
        await event.edit(
            strategies_info.get(strategy, "Strategy info"),
            buttons=STRATEGY_MENU
        )
    
    elif data == "help":
        await event.edit(
            "ℹ *Venom Bot Help & Commands*\n\n"
            "*Commands:*\n"
            "• /start - Start the bot\n"
            "• /menu - Show main menu\n\n"
            "*Features:*\n"
            "✅ Auto-forwarded signals from 5+ premium sources\n"
            "✅ Real-time chart integration\n"
            "✅ Trading strategies & education\n"
            "✅ Market news & analysis links\n"
            "✅ Expert predictions\n\n"
            "*Signal Sources:*\n"
            "• Evening Trader Group\n"
            "• Evening Trader Official\n"
            "• Learn 2 Trade\n"
            "• CryptoSignals.Org\n"
            "• ALTSIGNALS\n\n"
            "⚠ *Disclaimer:* Not financial advice!\n"
            "Always DYOR (Do Your Own Research)",
            buttons=[[Button.inline("🔙 Back", b"main_menu")]]
        )

# Monitor source channels for signals
@bot.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def signal_forwarder(event):
    """Forward signals from source channels"""
    try:
        message_text = event.message.text or event.message.message
        if not message_text:
            return
        
        # Check if message contains signal keywords
        text_lower = message_text.lower()
        signal_keywords = ['buy', 'sell', 'long', 'short', 'entry', 'signal', 'tp', 'target', 'leverage']
        
        if any(word in text_lower for word in signal_keywords):
            # Parse signal
            signal = parse_signal(message_text)
            
            # Check if it's a valid signal
            if signal['coin'] and signal['type']:
                # Get source channel ID
                source_id = event.chat_id
                
                # Format message
                formatted_msg = format_signal_message(signal, source_id)
                
                # Get chart
                chart_url = get_tradingview_chart(signal['coin'])
                
                # Post to your channel
                await bot.send_message(
                    YOUR_CHANNEL_ID,
                    formatted_msg + f"\n\n📊 [View Live Chart]({chart_url})",
                    buttons=[[Button.url("📈 Open TradingView Chart", chart_url)]]
                )
                
                logger.info(f"✅ Posted signal: {signal['coin']} - {signal['type']} from {CHANNEL_NAMES.get(source_id, 'Unknown')}")
    
    except Exception as e:
        logger.error(f"❌ Error forwarding signal: {e}")

async def post_menu_to_channel():
    """Post permanent menu to channel"""
    try:
        await bot.send_message(
            YOUR_CHANNEL_ID,
            "🐍 *Venom Crypto Trading Bot*\n\n"
            "Welcome to your premium signals channel!\n\n"
            "📊 *Features:*\n"
            "• Real-time signals from 5+ sources\n"
            "• Live trading charts\n"
            "• Expert analysis & predictions\n"
            "• Trading strategies\n\n"
            "Click buttons below to explore:",
            buttons=MAIN_MENU
        )
        logger.info("✅ Posted menu to Venom channel")
    except Exception as e:
        logger.error(f"❌ Error posting menu: {e}")

async def main():
    """Main function"""
    logger.info("🐍 Starting Venom Crypto Trading Bot...")
    
    # Start keep-alive server
    keep_alive()
    logger.info("✅ Keep-alive server started")
    
    # Initialize user client if needed (optional)
    if os.environ.get('PHONE_NUMBER'):
        await initialize_user_client()
    
    # Post menu to channel
    await post_menu_to_channel()
    
    logger.info("🚀 Venom Bot is running and monitoring channels...")
    logger.info(f"📡 Monitoring {len(SOURCE_CHANNELS)} signal channels")
    logger.info(f"📢 Posting to channel: {YOUR_CHANNEL_ID}")
    
    await bot.run_until_disconnected()

if _name_ == '_main_':
    asyncio.run(main())