import discord
import os
import random

# 시스템 환경 변수에서 토큰을 읽어옵니다.
TOKEN = os.environ.get('DISCORD_TOKEN')

# 모든 인텐트를 활성화합니다.
intents = discord.Intents.all()

# discord.Client 객체를 생성합니다.
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name}이(가) 성공적으로 로그인했습니다.')

@client.event
async def on_message(message):
    # 봇 자신의 메시지는 무시합니다.
    if message.author == client.user:
        return

    content = message.content.lower()  # 메시지 내용을 소문자로 변환하여 처리합니다.
    
    # '안녕'에 대한 응답
    if content in ['안녕', '!안녕']:
        responses = [
            "(자동 회신) 안녕하세요! 오늘 하루는 어떠셨나요?",
            "(자동 회신) 안녕! 무엇을 도와드릴까요?",
            "(자동 회신) 반가워요! 오늘 기분은 어떠신가요?",
        ]
        response = random.choice(responses)
        await message.channel.send(response)
    
    elif content in ['주인 어디있어?', '주인은?', '주인위치', '주인뭐해?', '주인 위치']:
        weather_responses = [
            "(자동 회신) 주인장은 사정이 있어서 자리를 비운 상태입니다 나중에 연락해주세요."
        ]
        response = random.choice(weather_responses)
        await message.channel.send(response)

    # '날씨'에 대한 응답
    elif content in ['날씨', '!날씨']:
        weather_responses = [
            "(자동 회신) 오늘 날씨는 맑아요. 외출하기 좋은 날씨네요!",
            "(자동 회신) 비가 오고 있어요. 우산을 챙기세요!",
            "(자동 회신) 오늘은 조금 춥네요. 따뜻하게 입으세요!",
        ]
        response = random.choice(weather_responses)
        await message.channel.send(response)

    # '주사위'에 대한 응답
    elif content in ['주사위', '!주사위']:
        dice_roll = str(random.randint(1, 6))
        await message.channel.send(f"(자동 회신) 주사위를 굴렸어요! 결과는 {dice_roll}입니다.")
        
    # '잘가'에 대한 응답
    elif content in ['잘가', '!잘가']:
        responses = [
            "(자동 회신) 안녕히 가세요!",
            "(자동 회신) 다음에 또 만나요!",
            "(자동 회신) 잘 다녀오세요!",
        ]
        response = random.choice(responses)
        await message.channel.send(response)

    # '뭐해'에 대한 응답
    elif content in ['뭐해', '!뭐해']:
        responses = [
            "(자동 회신) 저는 여기 있어요.",
            "(자동 회신) 아무것도 안하고 있어요.",
            "(자동 회신) 뭐든지 물어보세요!",
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # '사랑해'에 대한 응답
    elif content in ['사랑해', '!사랑해']:
        responses = [
            "(자동 회신) 저도 사랑해요!",
            "(자동 회신) 너무 감동적이에요!",
            "(자동 회신) 정말 고마워요!",
        ]
        response = random.choice(responses)
        await message.channel.send(response)
    
    # '배고파'에 대한 응답
    elif '배고파' in content:
        responses = [
            "(자동 회신) 음식을 먹어서 배부르게 해줄까요?",
            "(자동 회신) 맛있는 음식을 먹어보세요!",
            "(자동 회신) 저도 배고파요... 하지만 먹을 수 없어요."
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # '배부르다'에 대한 응답
    elif '배부르다' in content:
        responses = [
            "(자동 회신) 배부르다니 다행이에요!",
            "(자동 회신) 맛있는 걸 많이 먹었나봐요!",
            "(자동 회신) 저도 얼른 배부르게 되었으면 좋겠어요!"
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # '놀자'에 대한 응답
    elif '놀자' in content:
        responses = [
            "(자동 회신) 뭐로 놀까요?",
            "(자동 회신) 무슨 놀이를 하고 싶으세요?",
            "(자동 회신) 저도 놀고 싶어요!"
        ]
        response = random.choice(responses)
        await message.channel.send(response)
    
    # '화장실'에 대한 응답
    elif '화장실' in content:
        responses = [
            "(자동 회신) 화장실이 어디 있는지 알려드릴까요?",
            "(자동 회신) 화장실이 어딘지 모르시겠다면 주위를 둘러보세요!",
            "(자동 회신) 화장실을 찾고 계신가요? 저도 함께 찾아보겠습니다!"
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # '뭐할까?'에 대한 응답
    elif '뭐할까?' in content:
        responses = [
            "(자동 회신) 음... 책을 읽어보는 건 어떠세요?",
            "(자동 회신) 영화나 드라마를 보는 건 어떠세요?",
            "(자동 회신) 음악을 듣는 건 어떠세요?",
            "(자동 회신) 운동을 해보는 건 어떠세요?",
            "(자동 회신) 그림을 그려보는 건 어떠세요?"
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # '즐겁다'에 대한 응답
    elif '즐겁다' in content:
        responses = [
            "(자동 회신) 즐거워하시니 저도 기분이 좋아요!",
            "(자동 회신) 즐거운 일이 있었나봐요! 공유해주세요!",
            "(자동 회신) 즐거워하시는 걸 보니 저도 행복해요!"
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # '우울해'에 대한 응답
    elif '우울해' in content:
        responses = [
            "(자동 회신) 우울한 기분이군요... 저와 이야기해보시는 건 어떨까요?",
            "(자동 회신) 슬픈 일이 있었나봐요... 함께 이야기하면 마음이 조금 풀릴 수 있을 거예요.",
            "(자동 회신) 우울한 감정은 모두가 가끔 느끼는 거예요. 저도 더 힘들지 않게 도와드릴게요!"
        ]
        response = random.choice(responses)
        await message.channel.send(response)

    # '힘내'에 대한 응답
    elif '힘내' in content:
        responses = [
            "(자동 회신) 힘내세요! 당신은 괜찮은 사람이에요.",
            "(자동 회신) 모든 것이 잘 될 거예요. 힘내세요!",
            "(자동 회신) 힘내세요! 저도 당신을 응원합니다."
        ]
        response = random.choice(responses)
        await message.channel.send(response)

    # '봇 사용 도움 응답
    elif content in ['도움', '!도움', '봇사용', '!봇사용']:
        response = "(자동 회신) 안녕하세요! 저는 다양한 명령을 수행할 수 있는 봇입니다.\n\n" \
                   "다음은 몇 가지 사용 가능한 명령어입니다:\n" \
                   "`안녕`, `주인 어디있어?`, `날씨`, `주사위`, `잘가`, `뭐해`, `사랑해`, `배고파`, `배부르다`, `놀자`, `화장실`, `뭐할까?`, `즐겁다`, `우울해`, `힘내`\n\n" \
                   "명령어를 입력하면 제가 해당하는 응답을 해줄 거에요!"
        await message.channel.send(response)

# 봇을 실행합니다.
client.run(TOKEN)
