from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "1954702850:AAFsQB-FOFY0SxaAgn7eAZzmcegeHxogpNI"  # Bot token

PROJECT_NAME = "aiogramtelegrambot12" # Webhook

WEBHOOK_HOST = f"https://{PROJECT_NAME}.herokuapp.com"
WEBHOOK_PATH = '/webhook/' + BOT_TOKEN
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

ADMINS = [1343692719, ]  # adminlar ro'yxati