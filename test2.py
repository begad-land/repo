import random

class Question:

    def __init__(self,Qs,Qs_num) -> None:
#the object's attributes are given here
        self.Q=Qs
        self.Qs_num=Qs_num
    
    def display_questions(self):
        Q_num=1
        print(f'\n{self.Qs_num}){self.Q}\n')
        
        

class Answers:

    def __init__(self,As) -> None:
#the object's attributes are given here
        self.As=As
    
    def store_answers(self):
        return self.As

class Choices:
    
    def __init__(self,choices) -> None:

#the object's attributes are given here                           self.choices=choices

    def display_choices(self):
        for choice in self.choices:
            print(f'{choice}\n--------------')

class Clues:
    
    def __init__(self,clues) -> None:

#the object's attributes are given here        self.clues=clues

    def store_clues(self):
        #you can save this in a variable outside the scope of the classes
        return self.clues

class Game:

    def __init__(self,questions,choices,answers,clues) -> None: 
  
#here you're creating an instance or a copy of the object by passing the other classes as arguments to be created in the main class'(Game) init method and passing the mini class' arguments while passing them to the main class

        self.questions=questions
        self.choices=choices
        self.answers=answers
        self.clues=clues
    


Qs_and_As={
                    'whats the coldest planet in our solar system?':(('A. Uranus', 'B. Earth' ,'C. Jupiter', 'D. Neptune'),'A','its the 7th planet in the solar system'),

                    'what is the second most spoken language in the world?':(('A. French', 'B. English' ,'C. Hindi', 'D. Mandrin Chinese'),'D','its asian'),
                      
                    'what is the most abudnant element in the atmosphere':(('A. Francium(Fr)', 'B. Oxygen(O2)', 'C. Nitrogen(N2)', 'D. Hydrogen(H)' ),'C','its used to put out fires '),

                    'whats the name of the island thats also a continent?':(('A. Australia' , 'B. Austria', 'C. Bora Bora' , 'D. Hawaii'),'A','its knwon for the kangroos'),

                    'the second biggest country in the world?':(('A. Canada', 'B. Russia' , 'C. U.S.A' , 'D. India'),'A','they play a lot of hockey'),

                    'what is the hardest substance on Earth':(('A. Platinum', 'B. Titamnium', 'C. Diamond', 'D. Iron'),'C','its always a rank in video games'),

                    'in which country is the longest river in the world?':(('A. France' , 'B. Egypt', 'C. U.S.A', 'D. Brazil' ),'B','they have a long history'),

                    'which planet has the most moons?': (('A. Jupiter', 'B. Mars', 'C. Mercury', 'D. Saturn'),'D','it has rings around it'),

                    'How many elements are in the periodic table?':(('A. 125', 'B. 118', 'C. 117', 'D. 123'),'B','cant hint for that one'),

                    'What is the country that has the second highest population':(('A. India', 'B. U.S.A', 'C. Indonesia' ,'D. China'), 'A','they are asian'),

                    'What is the biggest organ in the human body':(('A. Liver', 'B. Brain', 'C. Skin', 'D. Lungs'),'C','its the first line of defense in your immune system'),

                    'which planet in our solar system is called the "Red planet" ':(('A. Mars','B. Venus','C. Earth','D. Jupiter'),'A','it neighbors earth')
                    }
    
    

Qs_displayed=[]
score=1

while len(Qs_displayed) != 7:

    rand=random.choice(list(Qs_and_As.items()))

    
    if rand in Qs_displayed:
        continue

    Qs_displayed.append(rand)

    game=Game(
        Question(rand[0],len(Qs_displayed)),
        Choices(rand[1][0]),
        Answers(rand[1][1]),
        Clues(rand[1][2]),
            )

    game.questions.display_questions()
    game.choices.display_choices()
    clue=game.clues.store_clues()
    model_answer=game.answers.store_answers()

    guess=input(f'pick A/B/C/D (insert h for a hint) ').upper()

    if guess=='H':
        print(f'{clue}')
        guess=input(f'pick A/B/C/D ').upper()
    
    if guess==model_answer:
        print('correct')
        score+=1

    else:
        print(f'wrong\nanswer:{model_answer}')
    print('--------------------------------')

print(f'score:{score}/{len(Qs_displayed)}\nthanks for playing :)')