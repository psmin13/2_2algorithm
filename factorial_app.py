import time

# 반복문으로 n! 계산. n<0이면 ValueError 발생
def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀로 n! 계산. n<0이면 ValueError 발생
def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

# 실행 결과와 경과 시간(초) 을 반환. (예외는 전파)
def run_with_time(func, n: int):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# 테스트 데이터
TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# 메뉴 화면 출력
def print_menu():
    print("\n===== Factorial Tester =====")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")

# 메뉴 화면 동작
def main():
    while True:
        print_menu()
        choice = input("선택: ")

        if choice == "q":
            print("종료합니다.")
            break

        elif choice in ["1", "2", "3"]:
            n_str = input("n 값(정수, 0 이상)을 입력하세요: ")
            if not n_str.isdigit():
                print("정수(0 이상의 숫자)만 입력하세요.")
                continue
            n = int(n_str)

            try:
                if choice == "1":
                    result, t = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {result} ([반복] 시간: {t:.6f}초)")

                elif choice == "2":
                    result, t = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {result} ([재귀] 시간: {t:.6f}초)")

                elif choice == "3":
                    result1, t1 = run_with_time(factorial_iter, n)
                    result2, t2 = run_with_time(factorial_rec, n)
                    print(f"[반복] {n}! = {result1} ([반복] 시간: {t1:.6f}초)")
                    print(f"[재귀] {n}! = {result2} ([재귀] 시간: {t2:.6f}초)")
                    print("결과 일치 여부:", "일치" if result1 == result2 else "불일치")

            except ValueError as e:
                print("오류:", e)
            except RecursionError:
                print("RecursionError")

        elif choice == "4":
            for n in TEST_DATA:
                print(f"\nn = {n}")
                try:
                    result1, t1 = run_with_time(factorial_iter, n)
                    result2, t2 = run_with_time(factorial_rec, n)
                    print(f"[반복] {n}! = {result1} ([반복] 시간: {t1:.6f}초)")
                    print(f"[재귀] {n}! = {result2} ([재귀] 시간: {t2:.6f}초)")
                    print("결과 일치 여부:", "일치" if result1 == result2 else "불일치")
                except RecursionError:
                    print("RecursionError")

        else:
            print("잘못된 입력.")

if __name__ == "__main__":
    main()
