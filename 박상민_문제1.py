def stairs_count(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    p = [0] * (n + 1)
    p[1] = 1
    p[2] = 2
    for i in range(3, n + 1):
        p[i] = p[i - 1] + p[i - 2]
    return p[n]


def main():
    n = int(input("계단의 개수를 입력하시오: ").strip())
    way = stairs_count(n)
    print(f"{n}개의 계단을 오르는 방법의 수는 {way}가지입니다.")


if __name__ == "__main__":
    main()
