from googletrans import Translator

#1.googletrans의 번역기 제작
translator = Translator()
#2.언어 감지를 원하는 문장을 설정
sentence = input("언어를 입력하세요")
#3.언어를 감지
dest = input("어떤 언어로 번역을 원하시나요?")

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("=================================")
