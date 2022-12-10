# class Animal:
#     def eat(self):
#         return 'Yum..'
#
#
# class Dog(Animal):
#     def bark(self):
#         return 'Woof!'

#
# class Cat(Animal):
#     def meow(self):
#         return 'Meow..'
#
#
# snoopy = Dog()
# print(snoopy.bark())
# print(snoopy.eat())


#
# class Robot:
#     def move(self):
#         return 'moves..'

#
# class CleanRobot(Robot):
#     def clean(self):
#         return 'Clean!'

#
# class PlayRobot(Robot):
#     def play(self):
#         return 'play..'
#
#
# myrebot = PlayRobot()
# print(myrebot.play())
# print(myrebot.move())


# #make a super robot with lots of mixed abilities
# # --------- COMPOSITION -----------------


# class Dog:
#     def bark(self):
#         return 'Woof!'
#
#
# class Robot:
#     def move(self):
#         return 'moves..'
#
#
# class CleanRobot:
#     def clean(self):
#         return 'Clean!'
#
#
# class SuperRobot:
#     def __init__(self):
#         self.ob1 = Dog()
#         self.ob2 = Robot()
#         self.ob3 = CleanRobot()
#
#     def play_game(self):
#         return 'Chess is best!'
#
#     def bark(self):
#         return self.ob1.bark()
#
#     def move(self):
#         return self.ob2.move()
#
#     def clean(self):
#         return self.ob3.clean()
#
#
# henry = SuperRobot()
# print(henry.bark())
# print(henry.move())
# print(henry.clean())
#
# # #------ Conclusion ----------
# # # Use composition when you can
# # # Use inheritance when you must
