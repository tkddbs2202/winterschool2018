import random

ans1="자! 해보세요"
ans2="됬네요,이사람아"
ans3="뭐라고 다시한번생각해 보세요"
ans4="모르니 두려운것 입니다"
ans5="칠푼인가요?? 제정신이 아니군요"
ans6="해도 그만, 안해도 그만, 아니겠어요?"
ans7="당신이라면 할수 있어요"
ans8="맞아요"

print("mymagic8에오신 것을 환영합니다")

q=input("질문 입력하고 엔터\n")
print("고민중...\n"*4)
choice= random.randint(1,8)
if choice==1:
    choice=ans1
elif choice==2:
     answer=ans2
elif choice==3:
     answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
else:
    answer=ans8

print(answer)

input("\n\n 마치려면 엔터키를 누르세요\n")
