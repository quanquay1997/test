#!/usr/bin/env python3


def solve(N):
    N = input()
    if N % 2==0:
        print("moi nhap lai gia tri la so le:")
    else :
        print(6*str(N))
    '''Creates a list like this - odd numbers repeat six times.

      ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN]

    Must: use list comprehension
    Tips: list comprehension always create new list
    '''


    result = None

    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    #
    # return result


def main():
    print(solve(20))


if __name__ == "__main__":
    main()
