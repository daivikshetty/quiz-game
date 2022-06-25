from data import question_data


class QuizBrain:

    def __init__(self,qn_list):
        self.q_num=0
        self.q_list=qn_list

    def questions_left(self):
        if self.q_num < len(question_data):
            return True
        else:
            return False

    pts=0

    def ask_qn(self):
        cur_qn=self.q_list[self.q_num]
        self.q_num+=1
        ans=input(f"Q{self.q_num}:{cur_qn.text}(True/False)?")
        crt=question_data[self.q_num-1]['answer']

        if self.check_ans(ans,crt):
            print("Correct!")
            self.pts+=1
            print(f"{self.pts}/{self.q_num}")

        else:
            print("Wrong!")
            print(f"{self.pts}/{self.q_num}")


    def check_ans(self, user_ans, crt_ans):
        if user_ans==crt_ans:
            return True
        else:
            return False
