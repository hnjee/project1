class CustomPager:
    # 클래스변수
    # numer=1
    
    # 생성자
    # self -> this
    def __init__(self, page, kind, search):
        # 멤버변수선언
        self.page=page
        self.kind=kind
        self.search=search
        self.startNum=1
        self.lastNum=2
        self.range=range(1,2)
        # 이전 Block 유무
        self.pre=False
        # 다음 Block 유무
        self.next=True

    def makePage(self, totalPage):
        # 한페이지당 보여줄 글의 갯수
        perPage=2

        # 한 블럭당 출력할 번호의 갯수
        perBlock=2

        # 전체 블럭
        totalBlock = totalPage // perPage # 5/2 = 2
        if totalPage % perPage !=0 :
            totalBlock+=1

        # page번호로 현재 블럭번호     
        curBlock = self.page // perBlock
        if self.page % perBlock != 0 :
            curBlock +=1

        # curBlock으로 startNum, lastNum
        self.startNum = (curBlock-1)*perBlock+1
        self.lastNum = curBlock*perBlock

        if curBlock == totalBlock :
            self.lastNum = totalPage
            self.next=False

        self.lastNum =self.lastNum+1

        self.range = range(self.startNum, self.lastNum)

        # 현재블럭이 1보다 크면 이전 유무
        if curBlock>1 :
            self.pre=True
            self.startNum = self.startNum-1