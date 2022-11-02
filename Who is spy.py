import random
import tkinter

class RequirePlayerNumber:
    def __init__(self):
        self.win = tkinter.Tk(className='Are you the spy?')
        self.win.geometry("300x200")
        num = tkinter.IntVar()
        label = tkinter.Label(self.win, width = 35, text = 'Please enter player number >> ')
        self.item = tkinter.Entry(self.win, width = 10, textvariable = num)  #建立一個Entry元件
        btn = tkinter.Button(self.win, width = 10, text = 'Confirm', command = self.Require_Player_Number)
        btn.pack(side = 'bottom')
        label.pack(side = 'left')
        self.item.pack(side = 'left')
        self.win.mainloop()
    
    def Require_Player_Number(self):
        global player_num 
        player_num = self.item.get()
        self.win.destroy()

class SetIdentity:
    def Topic_Selection():
        civilianbase = ['Beard', 'Sparrow', 'Dog', 'Horse', 'Motorcycle', 'Shampoo', 'Milk', 'Ketchup', 'Spiderman', ' butterfly', 'IOS', 'youtube', 'google', 'facebook', 'Air']
        spybase = ['Eyebrow', 'Crow', 'Cat', 'Donkey', 'Electric Car', 'Body wash', 'Soy Milk', 'Mustard', 'Batman', 'Bee', 'Android', 'Youku', 'Baidu', 'Weibo', 'Oxygen']
        topic_num = random.randint(0,14)
        return civilianbase[topic_num], spybase[topic_num]

    def Spy_Selection(player_num):
        spy_num = random.randint(0, player_num - 1)
        return spy_num

    def SetIdentityList(civilian, spy, spy_number, player_num):
        IdentityList = [civilian for i in range(player_num)]
        IdentityList[spy_number] = spy
        return IdentityList


class Check_Identity():
    def __init__(self, identitylist):
        self.identitylist = identitylist
        self.count = 0
        self.win = tkinter.Tk(className='Are you the spy?')
        self.win.geometry("300x200")
        self.label = tkinter.Label(self.win, width = 10, text = 'aaa')
        show_btn = tkinter.Button(self.win, width = 20, text = 'Click to show your identity', command = self.Show_identity)
        hide_btn = tkinter.Button(self.win, width = 20, text = 'Click to hide your identity', command = self.Hide_identity)
        close_btn = tkinter.Button(self.win, width = 10, text = 'Complete', command = self.Close_win)
        show_btn.pack()
        self.label.pack()
        hide_btn.pack()
        close_btn.pack(side = 'bottom')
        self.win.mainloop()

    def Show_identity(self):
        try:
            self.label.config(text = self.identitylist[self.count])
            self.count += 1
        except:
            self.win.destroy()
    def Hide_identity(self):
        self.label.config(text = '')

    def Close_win(self):
        self.win.destroy()
         
class Eliminate():
    def __init__(self, spy_number, spy):
        self.spy_number = spy_number
        self.spy = spy
        self.win = tkinter.Tk(className='Who is spy?')
        self.win.geometry("300x200")
        self.label = tkinter.Label(self.win, width = 35, text = 'Who is spy?')
        ans = tkinter.IntVar()
        self.item = tkinter.Entry(self.win, width = 10, textvariable = ans)
        btn = tkinter.Button(self.win, width = 10, text = 'Confirm', command = self.check)
        self.label.pack()
        self.item.pack()
        btn.pack()
        self.win.mainloop()


    def check(self):
        ans = self.item.get()
        if int(ans) - 1 == spy_number:
            self.label.config(text = 'Correct Answer! The identity is ' + self.spy)
        else:
            self.label.config(text = 'Incorrect')




if __name__=="__main__":
    RequirePlayerNumber()
    civilian, spy = SetIdentity.Topic_Selection()
    spy_number = SetIdentity.Spy_Selection(int(player_num))
    IdentityList = SetIdentity.SetIdentityList(civilian, spy, spy_number, int(player_num))
    print(IdentityList)
    Check_Identity(IdentityList)
    Eliminate(spy_number, spy)

    
    