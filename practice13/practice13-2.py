# この下に、１からnまでの数字が書かれた紙を袋に入れ、１つずつ取り出し、出てきた数字の並び順の考えられるパターン数求める関数Permutation(n)を作成してください
def Permutation(n):
    ret = 1
    for item in range(1,n+1):
        ret = item * ret
    return ret

a = 15
# この下で、変数aと、上記で作成した関数Permutation(n)を使って、15の時の結果を出力してください
# 期待する出力： 1307674368000
print(Permutation(a))