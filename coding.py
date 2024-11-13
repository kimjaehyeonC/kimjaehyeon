
def solution(n, x, y):

    if n == 1: 
        pass
    
    if n > 1:
        solution(n-1, x, 6-x-y)
        
    print(f' {n} 을 {x}에서 {y}로')
    
    if n > 1:
        solution(n-1, 6-x-y, y)
     
    return

form = "{}번 원반을 {}에서 {}로 이동"
def move(n, start, to):
    print(form.format(n, start, to))
    
def hanoi(n, start, to , via):
    if n==1:
        move(n, start, to)
        
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1, via, to, start)
    
# n = int(input(' 원반 수 '))

# hanoi(n, 'A', 'C', 'B')

def queen():
    pos = [0] * 8
    flag_a = [False] * 8
    flag_b = [False] * 15
    flag_c = [False] * 15

    cnt = 0
    def put() -> None:
        for i in range(8):
            print(f'{pos[i]:2}', end = '')
        print()
        
    def set(i : int):
        nonlocal cnt
        
        for j in range(8):
            if(not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+7]):
                pos[i] = j
                if i == 7:
                    put()
                    cnt += 1
                else:
                    flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                    set(i+1)
                    flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False
        

    set(0)
    print(cnt)
    
queen()