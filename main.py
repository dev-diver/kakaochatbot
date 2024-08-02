import os
import json
from openai import OpenAI
from pprint import pprint

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

model3 = "gpt-3.5-turbo-1106"
model4 = "gpt-4-0613"

template = """
Q: 카페테리아에 사과가 23개 있었습니다. 점심 식사로 20개를 사용하고 6개를 더 사서 2개를 나눠주었다면 사과가 몇 개 남았나요?
A: 사과가 23개 있었고, 점심 식사로 20개를 사용하였으므로 23-20 = 3개가 남았습니다. 그리고 6개를 더 사서 3 + 6 = 9개가 되었습니다. 2개를 나눠주었으므로 9-2 = 7 개가 남았습니다. 따라서 사과가 7개 남았습니다.

Q: 주차장에 차가 3대 있고, 2대의 차가 더 들어왔습니다. 이제 주차장에는 몇 대의 차가 있나요?
A: 주차장에 이미 차가 3대 있습니다. 2대가 더 들어왔습니다. 이제는 3+2=5대의 차가 있습니다.
답은 5입니다.

Q: 서버실에 컴퓨터가 5대 있었습니다. 월요일부터 목요일까지 매일 5대의 컴퓨터가 추가로 설치되었고 어제 1대를 받았습니다. 이제 서버실에는 몇 대의 컴퓨터가 있을까요?
"""

context = [
    {"role": "user", "content": template},
]

response = client.chat.completions.create(
    model=model4, 
    messages=context,
    temperature = 0,
    top_p=0,
).model_dump()
print(template)
pprint(response)