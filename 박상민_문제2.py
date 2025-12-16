def backpack(W, items):
    n = len(items)
    
    A = [[0] * (W + 1) for _ in range(n + 1)]

    # 테이블
    for i in range(1, n + 1):
        name, wt, val = items[i - 1]
        for w in range(0, W + 1):
            if wt > w:
                A[i][w] = A[i - 1][w]
            else:
                with_item = val + A[i - 1][w - wt]
                without_item = A[i - 1][w]
                A[i][w] = max(with_item, without_item)

    # 역추적
    selected = []
    w = W
    for i in range(n, 0, -1):
        if A[i][w] != A[i - 1][w]:
            name, wt, val = items[i - 1]
            selected.append(name)
            w -= wt

    selected.reverse()
    return A[n][W], selected


def main():
    # 물건
    items = [
        ("노트북", 3, 12),
        ("카메라", 1, 10),
        ("책", 2, 6),
        ("옷", 2, 7),
        ("휴대용 충전기", 1, 4),
    ]

    W = int(input("배낭 용량을 입력 하세요 : ").strip())

    max, selected = backpack(W, items)

    print(f"최대 만족도: {max}")
    print(f"선택된 물건: {selected}")


if __name__ == "__main__":
    main()
