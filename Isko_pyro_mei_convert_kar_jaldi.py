{
    "name": "Obanai",
    "description": "Telegram Group Management Bot made madee with pyrogram library in python.",
    "repository": "https://github.com/kokushibo17/Obanai",
    "logo": "https://commons.wikimedia.org/wiki/File:Obanai.jpg",
    "keywords": [
    "python",
    "telegram",
    "bot",
    "telegram-bot",
    "pyrogram"
    ],
    "repository": "https://github.com/kokushibo17/Obanai",
    "stack": "container",
    "env": {
        "BOT_TOKEN": {
            "description": "paste your telegram bot token made using @botfather",
            "required": true
		
	},
	    
	 "ASSISTANT_ID": {
            "description": "enter I'd of which uh have used to string (Id) Go to rose bot And Type /id..",
            "value": ""
        },    
		
	"STRING_SESSION": {
            "description": "fill with the telethon session string from any sting session generator bot",
            "required": true	
        },
	    
	"SUPPORT": {
            "description": "Fill there your group username else leave",
            "required": false,
            "value": ""
        },
        "CHANNEL": {
            "description": "Fill there your Channel username else leave",
            "required": false,
            "value": ""
        },
	    
        "API_ID": {
            "description": "API_ID of your Telegram Account my.telegram.org/apps",
            "required": true
        },
        "API_HASH": {
            "description": "API_HASH of your Telegram Account my.telegram.org/apps",
            "required": true
        },
        "SUDO_USERS_ID": {
            "description": "Sudo users have full access to everythin, don't trust anyone... ex:- 123456 654321 123456",
            "required": true
        },
        "LOG_GROUP_ID": {
            "description": "For logs channel to note down important bot level events, recommend to make this public. ex: '-123456'",
            "required": true
        },
        "GBAN_LOG_GROUP_ID": {
            "description": "gban logs. ex: '-123456'",
            "required": true
        },
        "WELCOME_DELAY_KICK_SEC": {
            "value": "300",
            "required": true
        },
        "MONGO_URL": {
            "description": "Get From Here. https://telegra.ph/How-To-get-Mongodb-URI-04-06",
            "required": true
        },
        "ARQ_API_URL": {
            "description": "For Music Downloading And Many More Things... Don't change this value",
            "value": "https://thearq.tech",
            "required": true
		
	},	
		
	"OWNER_USERNAME": {
            "description": "your profile username without@!",
            "required": true,
            "value": ""
        	
        },
        "MESSAGE_DUMP_CHAT": {
            "description": "Chat_id of the group where useless things will go",
            "required": true
        },
	    
	     
        "DATABASE_URL": {
            "description": "Fill database from elephantsql.com",
            "required": true,
            "value": ""
		
	},	
        "ARQ_API_KEY": {
            "description": "Get this from @ARQRobot.",
            "required": true
        },
        "RSS_DELAY": {
            "description": "Delay in which RSS will send updates in chat",
            "value": "300",
            "required": true
        },
	    
	"DEV_USERS": {
            "description": "Dev Access Of Your Bot (Id) Go to rose-bot And Type /id..",
            "value": ""
		
	},
	    
	"OWNER_ID":{
		"description": "Owner id of bot",
		"required":true
	}
    }
}
