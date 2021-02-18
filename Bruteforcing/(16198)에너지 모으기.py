N = int(input())
energy = list(map(int, input().split()))


def forward(energy):
    ans = 0
    if len(energy) == 2:
        return 0

    for i in range(1, len(energy) - 1):
        answer = (energy[i - 1] * energy[i + 1])
        a = energy[: i] + energy[i + 1:]
        answer += forward(a)
        if ans < answer:
            ans = answer

    return ans


print(forward(energy))

