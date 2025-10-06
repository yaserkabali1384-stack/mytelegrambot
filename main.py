from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatMember
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# ---------------------------
# لینک‌ها و شناسه‌ها
# ---------------------------
CHANNEL_ID = "@safe99_bet"  # یا آی‌دی کانال مثل -1001234567890
CHANNEL_LINK = "https://t.me/safe99_bet"
ADMIN_LINK = "@Lionbettt1"
FORM_LINK = "YOUR_FORM_LINK_HERE"
SITE_LINK = "YOUR_SITE_LINK_HERE"

# ---------------------------
# پیام‌ها برای هر دکمه
# ---------------------------
messages = {
    "آموزش": f"""💡 *آموزش شارژ و برداشت حساب*

سلام! 👋
اینجا می‌تونی راحت شارژ حساب و برداشت موجودی رو یاد بگیری.  
تمام مراحل ساده و با جزئیات توضیح داده شده.  

برای آموزش بیشتر حتما به کانال سر بزن:  
[🔗 کانال آموزش]({CHANNEL_LINK})
""",

    "ادمین": f"""📩 *ارتباط با ادمین*

سلام! 👋
برای خرید اشتراک یا حل مشکل، مستقیم با ادمین در ارتباط باش.  
[🔗 پیام به ادمین]({ADMIN_LINK})
""",

    "ویژه": f"""🌟 *بخش ویژه اعضا*

این قسمت مخصوص اعضای ویژه است.  
برای دسترسی یا خرید اشتراک با ادمین در ارتباط باش:  
[🔗 جزئیات بیشتر]({ADMIN_LINK})
""",

    "فرم": f"""📝 *فرم رایگان امروز*

سلام! 👋
اینجا می‌تونی فرم رایگان امروز رو پر کنی و از مزایا و آموزش‌های ویژه بهره‌مند بشی.  
[🔗 دسترسی به فرم]({FORM_LINK})
""",

    "سایت": f"""🌐 *بهترین سایت ایرانی و خارجی*

سلام! 👋
در این بخش می‌تونی به بهترین سایت‌های ایرانی و خارجی دسترسی داشته باشی و از امکانات ویژه‌شون بهره‌مند بشی.  
[🔗 مشاهده سایت‌ها]({SITE_LINK})
"""
}

# ---------------------------
# تابع بررسی عضویت
# ---------------------------
async def check_membership(user_id, context: ContextTypes.DEFAULT_TYPE):
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status in [ChatMember.MEMBER, ChatMember.ADMINISTRATOR, ChatMember.OWNER]:
            return True
        return False
    except:
        return False

# ---------------------------
# فرمان /start
# ---------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    is_member = await check_membership(user_id, context)
    
    if not is_member:
        keyboard = [[InlineKeyboardButton("عضو شدن در کانال", url=CHANNEL_LINK)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "سلام! برای استفاده از ربات باید ابتدا عضو کانال ما شوی.", 
            reply_markup=reply_markup
        )
        return
    
    keyboard = [
        [InlineKeyboardButton("📚 آموزش", callback_data="آموزش")],
        [InlineKeyboardButton("💬 ارتباط با ادمین", callback_data="ادمین")],
        [InlineKeyboardButton("🌟 بخش ویژه اعضا", callback_data="ویژه")],
        [InlineKeyboardButton("📝 فرم رایگان امروز", callback_data="فرم")],
        [InlineKeyboardButton("🌐 بهترین سایت ایرانی و خارجی", callback_data="سایت")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=reply_markup)

# ---------------------------
# پاسخ به دکمه‌ها
# ---------------------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    msg = messages.get(query.data, "گزینه نامعتبر!")
    await query.edit_message_text(text=msg, parse_mode='Markdown')

# ---------------------------
# اجرای ربات
# ---------------------------
async def main():
    TOKEN = "8360083922:AAHLolbBTs5LYMY7rVDja_Q-KUeZP6mhfjo"
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    
    print("Bot is running...")
    await app.run_polling()

import asyncio
asyncio.run(main())
