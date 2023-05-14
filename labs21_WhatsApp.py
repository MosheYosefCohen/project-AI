import ai21
import pywhatkit
ghhfghg
ai21.api_key = '0tdfIwigSDik6RmCGOBnmvR5k9SxXYda'

a = ai21.Completion.execute(
  model="j2-grande-instruct",
  prompt= 'write a sentence in very hugh level english in bvery high level and complicated and deep',
  numResults=1,

  maxTokens=2000,
  temperature=0.7,
  topKReturn=0,
  topP=1,
  countPenalty={
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": True
  },
  frequencyPenalty={
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  presencePenalty={
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  stopSequences=[]
)

print(a['prompt']['text'])
# print(a)
print(a['completions'][0]['data']['text'])

# time delay
# pywhatkit.sendwhatmsg("+972549889177",a['completions'][0]['data']['text'], 15, 35, 15, True, 2)

# grupe
# # pywhatkit.sendwhatmsg_to_group(, a['completions'][0]['data']['text'], 23,55)
# lst = ["+972549889177", "+972538253297", "+972559771087" ]
# for i in lst:
#     pywhatkit.sendwhatmsg_instantly(i,a['completions'][0]['data']['text'])


# intant
pywhatkit.sendwhatmsg_instantly("+972587733360",a['completions'][0]['data']['text'])
