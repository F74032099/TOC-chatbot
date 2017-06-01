from transitions.extensions import GraphMachine
import random

score =0
count =10
logic_count = 6
logic_ans=""
logic_score=0
class TocMachine(GraphMachine):
	ans =""
	
	def __init__(self, **machine_configs):
		self.machine = GraphMachine(
		model = self,
			**machine_configs
	)

	
	def on_enter_user(self, update):
		update.message.reply_text("輸入 help 獲得更多說明")

	
	def is_going_to_description(self, update):
		text = update.message.text
		return text.lower() == 'help'

	def on_enter_description(self, update):
		update.message.reply_text("功能1:英文單字測驗(高中7000字)\n"
								 +"輸入eng開始測驗，測驗共分三個難度。\n"
								 +"答對可到下一個難度，答錯則到倒退一個難度\n"
								 +"功能2:簡單智商測驗\n"
								 +"輸入logic開始測驗\n"
								 +"前三題為數字題，後三題為圖形題。")
		self.go_back(update)

	def is_going_to_level1(self, update):
		text = update.message.text
		return text.lower() == 'eng'
	
	def on_enter_level1(self, update):
		global ans
		f1 = open('voc/level1.txt','r')
		rnd = random.randint(1,len(f1.readlines()))
		f1.close()
		f1 = open('voc/level1.txt','r')
		line = f1.readlines()[rnd-1]
		index = line.find("@")
		ans = line[0:index]
		chi = line[index+2:]
		length = len(ans);
		ques = ans[0]+"___"+ans[length-1]+"  "+chi+"	單字長度:"+str(length)
		update.message.reply_text(str(10-count+1)+'.難度I')
		update.message.reply_text(ques)
		#update.message.reply_text(ans)

		f1.close()

	#def on_exit_level1(self, update):
		#update.message.reply_text("")
		
	def is_going_to_level2(self, update):
		global score
		global count
		text = update.message.text
		if text == ans:
			count = count-1
		return text == ans
	
	def on_enter_level2(self, update):
		global ans
		f1 = open('voc/level2.txt','r')
		rnd = random.randint(1,len(f1.readlines()))
		f1.close()
		f1 = open('voc/level2.txt','r')
		line = f1.readlines()[rnd-1]
		index = line.find("@")
		ans = line[0:index]
		chi = line[index+2:]
		length = len(ans);
		ques = ans[0]+"___"+ans[length-1]+"  "+chi+"	單字長度:"+str(length)
		update.message.reply_text(str(10-count+1)+'.難度II')
		update.message.reply_text(ques)
		#update.message.reply_text(ans)

		f1.close()

	#def on_exit_level2(self, update):
		#update.message.reply_text("Leaving level2")
	
	def is_going_to_level3(self, update):
		global score
		global count
		text = update.message.text
		if text == ans:
			count = count-1
		return text == ans
	
	def on_enter_level3(self, update):
		global ans
		f1 = open('voc/level3.txt','r')
		rnd = random.randint(1,len(f1.readlines()))
		f1.close()
		f1 = open('voc/level3.txt','r')
		line = f1.readlines()[rnd-1]
		index = line.find("@")
		ans = line[0:index]
		chi = line[index+2:]
		length = len(ans);
		ques = ans[0]+"___"+ans[length-1]+"  "+chi+"	單字長度:"+str(length)
		update.message.reply_text(str(10-count+1)+'.難度III')
		update.message.reply_text(ques)
		#update.message.reply_text(ans)

		f1.close()

	#def on_exit_level3(self, update):
		#update.message.reply_text("Leaving level3")
	def wrong_ans(self, update):
		global count
		text = update.message.text
		if text != ans:
			count = count-1
		return text != ans
	##########for go back###########	
	def on_enter_level1_err(self, update):
		self.go_back(update)
		
	def on_enter_level3_correct(self, update):
		self.go_back(update)
		
	def is_going_to_level3_correct(self, update):
		global score
		global count
		text = update.message.text
		if text == ans:
			count = count-1
		return text == ans
	##############################
	def back_to_init(self,update):
		global count
		global score
		text = update.message.text
		if text == ans:
			update.message.reply_text('恭喜你答對了')
			score = score+1
		else:
			update.message.reply_text('你答錯了，正確答案為'+ans)
			
		if count == 1:
			update.message.reply_text('測驗結束，你總共答對了'+str(score)+"題")
			count=10
			score=0
			return True
		return False
	##############################	
	def is_going_to_logic1(self, update):
		text = update.message.text
		return text.lower() == 'logic'
	
	def on_enter_logic1(self, update):
		global logic_ans
		global logic_count
		update.message.reply_text("請以A B C D回答(大小寫均可)")
		rnd = random.randint(1,10)
		update.message.reply_text("第"+str(6-logic_count+1)+"題")
		f=open('logic/num'+str(rnd)+'.jpg', 'rb')
		update.message.reply_photo(photo=f)
		f.close()
		f1=open('logic/ans.txt','r')
		logic_ans=f1.readlines()[rnd-1]
		logic_ans=logic_ans[0]
		logic_count = logic_count-1
		f1.close()
		
		
	def is_going_to_logic2(self, update):
		global logic_count
		if logic_count == 3:
			global logic_score
			text = update.message.text
			if text.lower() == logic_ans.lower():
				update.message.reply_text("恭喜你答對了")
				logic_score = logic_score+1
			else:
				update.message.reply_text("你答錯了，正確答案為"+logic_ans)
			return True
		return False
	
	def on_enter_logic2(self, update):
		global logic_ans
		global logic_count
		update.message.reply_text("請以A B C D回答(大小寫均可)")
		rnd = random.randint(1,9)
		update.message.reply_text("第"+str(6-logic_count+1)+"題")
		f=open('logic/pic'+str(rnd)+'.jpg', 'rb')
		update.message.reply_photo(photo=f)
		f.close()
		f1=open('logic/ans.txt','r')
		logic_ans=f1.readlines()[10+rnd-1]
		logic_ans=logic_ans[0]
		logic_count = logic_count-1
		f1.close();
		
	def user_response(self, update):
		return True
		
	def on_enter_logic1_reply(self, update):
		global logic_score
		text = update.message.text
		if text.lower() == logic_ans.lower():
			update.message.reply_text("恭喜你答對了")
			logic_score = logic_score+1
		else:
			update.message.reply_text("你答錯了，正確答案為"+logic_ans)
		self.go_back(update)
		
	def on_enter_logic2_reply(self, update):
		global logic_score
		text = update.message.text
		if text.lower() == logic_ans.lower():
			update.message.reply_text("恭喜你答對了")
			logic_score = logic_score+1
		else:
			update.message.reply_text("你答錯了，正確答案為"+logic_ans)
		self.go_back(update)
	def logic_to_init(self, update):
		global logic_count
		if logic_count == 0:
			global logic_score
			text = update.message.text
			if text.lower() == logic_ans.lower():
				update.message.reply_text("恭喜你答對了")
				logic_score = logic_score+1
			else:
				update.message.reply_text("你答錯了，正確答案為"+logic_ans)
			logic_count = 6
			update.message.reply_text("測驗結束，你總共答對了"+str(logic_score)+"題")
			logic_score=0
			return True
		return False