class Golf:
    results = " "
   
    def __init__(self, hole, score, par):
        self.hole = hole
        self.score = score
        self.par = par

    def evaluateAndDisplayScore(self):
        if self.score > self.par:
            Golf.results = "Over Par"
        elif self.score < self.par:
            Golf.results = "Under Par"
        else:
            Golf.results = "At Par"
            
        print("You scored", Golf.results, "on hole#", self.hole, "with a par of", self.par)

score = 0

hole1=Golf(1,score,3)
hole2=Golf(2,score,4)
hole3=Golf(3,score,2)


enterHole=int(input("Enter the hole number:"))
score=int(input("Enter your score:"))

if enterHole == 1:
    hole1.score = score
    hole1.evaluateAndDisplayScore()
elif enterHole == 2:
    hole2.score = score
    hole2.evaluateAndDisplayScore()
elif enterHole == 3:
    hole3.score = score
    hole3.evaluateAndDisplayScore()
