with open('test2.txt', 'r') as f:
    print(f.tell())  # 0が帰ってくる
    print(f.read(1))  # Aが帰ってくる
    # Dをしゅつ録したい場合は
    f.seek(12)
    print(f.read(1))
    # またAを二文字読み込みたくなったら
    f.seek(1)
    print(f.read(2))
# seekはファイルの特定の箇所を読み込みたい時に便利なメソッド
