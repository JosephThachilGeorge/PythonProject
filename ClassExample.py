class Computer:
    def config(self):
        print("100GB","40 inch","200g")

comp1 =Computer()
comp2= Computer()

Computer.config(comp1)
Computer.config(comp2)

# or we can write below code

comp1.config()
comp2.config()



