class PCB:
    def __init__(self, name, state, super_priority, ntime, rtime=0, link=None):
        self.name = name
        self.state = state
        self.super = super_priority
        self.ntime = ntime
        self.rtime = rtime
        self.link = link

class Scheduler:
    def __init__(self):
        self.ready = None
        self.last = None
        self.current = None

    def sort(self, p):
        if self.ready is None:
            self.ready = p
            self.last = p
        else:
            self.last.link = p
            self.last = p

    def input(self):
        num = int(input("请输入进程个数: "))
        for i in range(num):
            print(f"\n进程号No.{i}:")
            name = input("请输入进程名: ")
            super_priority = int(input("请输入优先数: "))
            ntime = int(input("请输入需要运行时间: "))
            p = PCB(name, 'w', super_priority, ntime)
            self.sort(p)

    def space(self):
        l = 0
        pr = self.ready
        while pr is not None:
            l += 1
            pr = pr.link
        return l

    def disp(self, pr):
        print("\nname\tstate\tsuper\tndtime\truntime")
        print(f"{pr.name}\t{pr.state}\t{pr.super}\t{pr.ntime}\t{pr.rtime}\n")

    def check(self):
        print(f"\n**** 当前运行的进程为: {self.current.name}")
        self.disp(self.current)
        pr = self.ready
        print("\n**** 当前就绪队列状态为:")
        while pr is not None:
            self.disp(pr)
            pr = pr.link

    def destroy(self):
        print(f"\n进程 [{self.current.name}] 运行完毕.")
        self.current = None

    def running(self):
        self.current.rtime += 1
        if self.current.rtime == self.current.ntime:
            self.destroy()
        else:
            self.current.super -= 1
            self.current.state = 'w'
            self.sort(self.current)

    def main(self):
        self.input()
        len = self.space()
        h = 0
        while len != 0 and self.ready is not None:
            input("\n按任意键继续...")
            h += 1
            print(f"\nThe execute number: {h}")
            self.current = self.ready
            self.ready = self.current.link
            self.current.link = None
            self.current.state = 'R'
            self.check()
            self.running()
            len = self.space()
        print("\n\n所有进程已经运行完毕.")

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.main()
