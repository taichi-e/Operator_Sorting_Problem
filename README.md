# Problem

数字演算子並び換え問題

以下の条件をみたす式で、1、2、3…… という整数をそれぞれ作りたい。
- 3、4、5、6 の 4 つの数字をそれぞれただ一度だけ用いる。
- 演算子には、+、-、*、/ のいずれかを用いる (重複も可)。
- 演算順序を変更する括弧は自由に用いてよい。
 
例えば、

>(4 - 3) / (6 - 5) = 1
>3 - (4 + 6) / 5 = 1

等で 1 が作れる。同様に、

>4 * 5 - 3 * 6 = 2
>(4 - 3) + (6 - 5) = 2

等で 2 が作れる。
 
(1) 上記のような式を 3、4、5 ……の順番に (可能な限り) 作り、それぞれの式を一つ示せ。
(2) 上記のような式で作れない、最小の正整数を答えよ。

# how to solve it
G. ポリア著「いかにして問題をとくか」の問題解決の原則に従いながらプログラムの作成を問題解決へ取り組んだ。
https://ci.nii.ac.jp/ncid/BC15267137

## 問題を理解する
- 未知のものは何か
  - 使用する ( ) の数
  - 組合せによって作れる最大数
  - 考えられる総パターン数
  - (2)に答えるために必要な計算量
  
- 与えられているものは何か
  - 使用できる数字
  - 演算子の種類と数
  - 2までの数字の作りかた
- 条件は何か
  - 3、4、5、6 の 4 つの数字をそれぞれただ一度だけ用いる
  - 演算子には、+、-、*、/ のいずれかを用いる (重複も可)
  - 演算順序を変更する括弧は自由に用いてよい

- 条件を満足させることは可能か
> yes
- 条件は未知のものを定めるのに十分であるか
> yes
- 条件は余剰であるか
> no
- 条件に矛盾はないか
> yes

## 計画を立てる
- 前にそれをみたことがあるか
> yes. ある決められた数字に自由に演算子を加え10を作る遊び
- 役に立つ定理を知っているか
> ある個数の数字を並べるパターンは階乗の計算で求められる

## 計画
方針として、数字と演算子の組合せとして考えられるパターンを全て調査することで(2)に答える。

(2)への回答方法として、以下の二つが考えられたが、総パターン数がさほど大きくなかったため前者を採用した。
- 数字と演算子の組合せとして考えられるパターンを全て調べる
- 理論上作れないことを示す(ex. 3\*4\*5\*6=360以上の数字は作れない)

4つの数字の並べ方は
>4! = 24

演算子は数字と数字の間にしか入れられないので、3つの演算子が使用される。また、演算子は複数回使うことができるので、
> 4**3 = 64

( )の置き方について、
- ( )を 1 つ使う場合は 5 通り
> (0 + 0) + 0 + 0
> 0 + (0 + 0) + 0
> 0 + 0 + (0 + 0)
> (0 + 0 + 0) + 0
> 0 + (0 + 0 + 0)

- ( )を 2 つ使う場合は 5 通り
> (0 + 0) + (0 + 0)
> ((0 + 0) + 0) + 0
> (0 + (0 + 0)) + 0
> 0 + ((0 + 0) + 0)
> 0 + (0 + (0 + 0))

- ( )を 3 つ使う場合は考えられない

よって総パターン数は、15360 である。
総当たりで計算しても時間はかからないと判断したため、全てのパターンを調べた。
> 24 * 64 * 10 = 15360


# Usage

それぞれのファイルに実行権限を与え、以下のコマンドを実行する。

> ./calc.py | ./sort_sentence.py | ./select_one.py

