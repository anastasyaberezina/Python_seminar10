import telebot

bot = telebot.TeleBot('5842913333:AAHWUQF7XS2BskfXxpYD9J2dsOhbyKqgBbA')

symb = ''
symb_old = ''

buttons = telebot.types.InlineKeyboardMarkup() # Создаем кнопки калькулятора

buttons.row(   telebot.types.InlineKeyboardButton('CE', callback_data='no'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))
                
buttons.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

buttons.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

buttons.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

buttons.row(   telebot.types.InlineKeyboardButton('.', callback_data='.'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data=','),
                telebot.types.InlineKeyboardButton('=', callback_data='='))

@bot.message_handler(commands=['start'])
def feedback(message):
    global symb
    if symb == '':
        bot.send_message(message.from_user.id, '0', reply_markup=buttons)
    else:
        bot.send_message(message.from_user.id, symb, reply_murkup=buttons)   
        
    
@bot.callback_query_handler(func=lambda call: True)   
def recall(request):
    global symb, symb_old
    data = request.data
    if data == 'no':
        pass
    elif data == 'C':
        symb = ''
    elif data == '<=':
        if symb != '':
            symb = symb[:len(symb)-1]    
    elif data == '=':
        try:
            symb = str(eval(symb))  
        except:
             symb = "ошибка"
    else:
       symb += data   
       
    if (symb != symb_old and symb!='') or ('0' != symb_old and symb == ''):
        if symb == '':
            bot.edit_message_text(chat_id=request.message.chat.id, message_id=request.message.id, text='0', reply_murkup=buttons) 
            symb_old = '0' 
        else:
            bot.edit_message_text(chat_id=request.message.chat.id, message_id=request.message.message_id, text=symb, reply_markup=buttons)     
            symb_old = symb 
    if symb == "ошибка":
        symb = ''    
      

bot.polling(none_stop=False, interval = 0)