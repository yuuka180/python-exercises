# 0番目が0、1番目が1、
# 2番目は、2つ前の0番目と1番目の数の和、つまり1、
# 3番目は、2つ前の1番目と2番目の数の和、つまり2、
# 4番目は、2つ前の2番目と3番目の数の和、つまり3、
# という数字の列を、フィボナッチ数列(fibonacci)と呼ぶ。
# この下に、n番目のフィボナッチ数を求める関数fibonacci(n)を作成してください
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = 20
# この下で、変数aと、上記で作成した関数fibonacci(n)を使って、20番目のフィボナッチ数を出力してください
# 期待する出力：6765
print(fibonacci(20))