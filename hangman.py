import random
import shutil
import os 

os.getcwd()

path_dir = "/Users/yuiti/hangman/ptyhonStudySpace /hangman.py"
move_dir = "/Users/yuiti/hangman"

shutil.move(path_dir,move_dir)

def hangman():
    
    
    anser = ["dog","cat","bibi"]
    random_number = random.randint(0, 2)
    word = anser[random_number]

    #間違えた回数を記録
    wrong = 0
    
    stages = ["",
              "_____       ",
              "            ",
              "     |      ",
              "     ◯      ",
              "    /|\     ",
              "    / \     "
              "            "
              ]
    
    #答えの文字を記録
    rletters = list(word)
    
    #スコア表じ
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    
    while wrong<len(stages)-1:
        print("\n")
        
        msg = "１文字を予想してね"
        char = input(msg)
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            
        else:
            wrong += 1
            
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
            print("あなたのかち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(rletters))
        
hangman()
    