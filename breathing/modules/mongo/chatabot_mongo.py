from Messi.mongo import db

chatbotdb = db.chatbot



def is_chatbot(chat_id):
    chatbot = chatbotdb.find_one({"chat_id": chat_id})
    if not chatbot:
        return False
    else:
        return True


def add_chatbot(chat_id):
    chatbot = is_chatbot(chat_id)
    if chatbot:
        return
    else:
        return chatbotdb.insert_one({"chat_id": chat_id})


def rm_chatbot(chat_id):
    chatbot = is_chatbot(chat_id)
    if not chatbot:
        return
    else:
        return chatbotdb.delete_one({"chat_id": chat_id})
