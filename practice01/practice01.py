# 英国数３教科の平均点を求める→以下3つは代入文
eng = 56
jp = 67
math = 43
sci = 32
social = 51
# この下を埋め、英国数３教科の平均点を求め、出力するプログラムを打ち込んでみよう→コメント文
# 期待する出力： 55.333333333333336
avg = (eng + jp + math + sci + social) / 5 #代入文→左側は変数
#変数名は大文字スタートは大体しない(クラス(メソッド)の名前とかは大文字)
#イコールがなく、代入を行わない式→式文
print(avg) #xprint の部分は関数、かっこの中は引数
#print(avg)、print('average = %.1f'%avg)→小数点第一位まで