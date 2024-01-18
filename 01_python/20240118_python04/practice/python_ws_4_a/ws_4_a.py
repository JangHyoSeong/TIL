# 아래에 코드를 작성하시오.
from conf import settings
from utils import create_url

name = settings.NAME
URL = settings.MAIN_URL

result = create_url.create_url(name, URL)
print(result)