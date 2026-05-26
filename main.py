import telebot
import os

# Вставь свой токен сюда или задай через переменную окружения
BOT_TOKEN = os.getenv("BOT_TOKEN", "8918670807:AAHFkCF8kemTCIVlbeLfmRkPUd6gk3wdKVo")

bot = telebot.TeleBot(BOT_TOKEN)

# Эмодзи кубика, которое Telegram отправляет как dice
DICE_EMOJI = "🎲"

@bot.message_handler(content_types=["dice"])
def handle_dice(message):
    """
    Срабатывает на любой dice-объект (🎲 🎯 🏀 ⚽ 🎳 🎰).
    Фильтруем только кубик 🎲 и сразу отвечаем выпавшим значением.
    Значение берём из message.dice.value — Telegram сам его уже знает
    в момент отправки, анимация нам не нужна.
    """
    dice = message.dice

    # Реагируем только на кубик 🎲
    if dice.emoji != DICE_EMOJI:
        return

    value = dice.value  # число от 1 до 6

    dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    face = dice_faces.get(value, "🎲")

    bot.reply_to(
        message,
        f"{face} Выпало: <b>{value}</b>",
        parse_mode="HTML",
    )


if __name__ == "__main__":
    print("Бот запущен. Ожидание кубиков...")
    bot.infinity_polling(skip_pending=True)
